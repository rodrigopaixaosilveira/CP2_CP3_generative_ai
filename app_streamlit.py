"""Frontend do assistente de atendimento de e-commerce (Streamlit).

Usa o modelo treinado no notebook CP_Ecommerce_SmolLM2_RAG_LoRA_v2.ipynb:
- lê saidas_v2/config_final.json (melhor adaptador LoRA);
- usa o RAG sempre ativado, com top_k = 2 e limiar de similaridade 0,55;
- carrega base_conhecimento.py e chamados_exemplo.py;
- repete exatamente a busca, o prompt e a geração do notebook.

Como rodar localmente (na pasta do projeto, com o .venv ativado):
    streamlit run app_streamlit.py

"""

import json
import os
import sys
import time
from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parent

# Antes de importar o transformers (iguais ao notebook):
os.environ["USE_TF"] = "0"
os.environ["USE_TORCH"] = "1"
os.environ.setdefault("HF_HOME", str(PASTA_PROJETO / "hf-cache"))
sys.path.insert(0, str(PASTA_PROJETO))

import numpy as np
import streamlit as st
import torch
from peft import PeftModel
from sentence_transformers import SentenceTransformer, util
from transformers import AutoModelForCausalLM, AutoTokenizer

from base_conhecimento import RESPOSTA_ENCAMINHAMENTO, RESPOSTA_FORA_DA_BASE, base_conhecimento
from chamados_exemplo import modelos_chamados

# -----------------------------------------------------------------------------
# Configuração
# -----------------------------------------------------------------------------
ARQUIVO_CONFIG = PASTA_PROJETO / "saidas_v2" / "config_final.json"
MAX_NEW_TOKENS = 160
USAR_RAG = True        # o RAG fica sempre ativado
TOP_K = 2              # documentos recuperados pelo RAG
LIMIAR_RAG = 0.55      # limiar de similaridade (escolhido no Experimento 1 do notebook)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
USAR_BF16 = DEVICE == "cuda" and torch.cuda.is_bf16_supported()
# Na CPU (computador sem GPU NVIDIA) o modelo é carregado em
# bfloat16: ocupa metade da memória do float32 e é o mesmo formato usado no treino.
DTYPE = torch.bfloat16 if (USAR_BF16 or DEVICE == "cpu") else torch.float16

documentos_por_id = {doc["id"]: doc for doc in base_conhecimento}
CATEGORIAS = sorted({doc["categoria"] for doc in base_conhecimento}) + ["fora_da_base"]

SYSTEM_PROMPT = f"""Você é um assistente de atendimento de uma loja virtual.
Use somente as informações presentes no contexto.
Não invente políticas, prazos ou procedimentos.
Se o contexto não for suficiente ou não tratar do chamado, use status "sem_informacao".
Valores permitidos:
- categoria: {', '.join(CATEGORIAS)}
- prioridade: baixa, media, alta, critica
- status: respondido, sem_informacao
Retorne somente um JSON válido, sem Markdown e sem explicações adicionais,
com as chaves: categoria, prioridade, equipe, procedimento, fonte e status."""

ROTULO_PRIORIDADE = {"baixa": "🟢 Baixa", "media": "🟡 Média", "alta": "🟠 Alta", "critica": "🔴 Crítica"}

EXEMPLOS = [
    "Meu pedido era para chegar ontem e o rastreio não atualiza.",
    "O fone de ouvido veio sem funcionar o lado esquerdo.",
    "Quero trocar o vestido por um tamanho maior.",
    "Apareceu uma compra de R$ 2.000 que eu não fiz.",
    "Esqueci minha senha e não consigo entrar no app.",
    "Vocês têm vaga de emprego para estoquista?",
]

st.set_page_config(page_title="Atendimento — Loja Virtual", page_icon="🛒", layout="wide")


# -----------------------------------------------------------------------------
# Carregamento (uma vez só; o Streamlit guarda em cache entre as interações)
# -----------------------------------------------------------------------------
def ler_config():
    if not ARQUIVO_CONFIG.exists():
        st.error(
            f"Não encontrei `{ARQUIVO_CONFIG.relative_to(PASTA_PROJETO)}`. "
            "Rode o notebook `CP_Ecommerce_SmolLM2_RAG_LoRA_v2.ipynb` até a seção 14 para treinar e salvar o modelo."
        )
        st.stop()
    return json.loads(ARQUIVO_CONFIG.read_text(encoding="utf-8"))


@st.cache_resource(show_spinner="Carregando o modelo treinado e a base de conhecimento...")
def carregar_recursos(modelo_base, modelo_embedding, pasta_adaptador):
    # RAG: índice com o texto de cada documento + 4 perguntas típicas (igual ao notebook)
    embedder = SentenceTransformer(modelo_embedding, device=DEVICE)
    textos_indice, documento_do_texto = [], []
    for posicao, doc in enumerate(base_conhecimento):
        textos_indice.append(f"{doc['titulo']}. {doc['conteudo']}")
        documento_do_texto.append(posicao)
        for frase in modelos_chamados[doc["id"]][:-1]:
            textos_indice.append(frase)
            documento_do_texto.append(posicao)
    embeddings_indice = embedder.encode(textos_indice, normalize_embeddings=True, convert_to_tensor=True)

    # LLM: modelo original + adaptador LoRA do melhor experimento
    tokenizer = AutoTokenizer.from_pretrained(modelo_base)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    base = AutoModelForCausalLM.from_pretrained(modelo_base, torch_dtype=DTYPE, low_cpu_mem_usage=True)
    base.config.pad_token_id = tokenizer.pad_token_id
    modelo = PeftModel.from_pretrained(base.to(DEVICE), pasta_adaptador).to(DEVICE)
    modelo.eval()

    return {
        "embedder": embedder,
        "embeddings_indice": embeddings_indice,
        "documento_do_texto": np.array(documento_do_texto),
        "tokenizer": tokenizer,
        "modelo": modelo,
    }


# -----------------------------------------------------------------------------
# Pipeline: busca → prompt → geração → validação → resposta ao cliente
# -----------------------------------------------------------------------------
def buscar_documentos(recursos, pergunta, top_k, limiar):
    embedding = recursos["embedder"].encode(pergunta, normalize_embeddings=True, convert_to_tensor=True)
    similaridades = util.cos_sim(embedding, recursos["embeddings_indice"])[0].float().cpu().numpy()
    doc_do_texto = recursos["documento_do_texto"]
    notas = np.array([similaridades[doc_do_texto == i].max() for i in range(len(base_conhecimento))])
    ordem = np.argsort(-notas)[:top_k]
    return [{**base_conhecimento[i], "score": float(notas[i])} for i in ordem if notas[i] >= limiar]


def formatar_contexto(documentos):
    if not documentos:
        return "Nenhum documento relevante foi encontrado na base."
    return "\n\n".join(
        f"[{doc['id']}] {doc['titulo']}\n"
        f"{doc['conteudo']}\n"
        f"Categoria: {doc['categoria']} | Prioridade: {doc['prioridade']} | Equipe: {doc['equipe']}\n"
        f"Procedimento: {doc['procedimento']}"
        for doc in documentos
    )


def montar_prompt(tokenizer, chamado, contexto):
    mensagens = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"CONTEXTO:\n{contexto}\n\nCHAMADO:\n{chamado}"},
    ]
    return tokenizer.apply_chat_template(mensagens, tokenize=False, add_generation_prompt=True)


def gerar_texto(recursos, prompt):
    tokenizer, modelo = recursos["tokenizer"], recursos["modelo"]
    entradas = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to(DEVICE)
    with torch.no_grad():
        saida = modelo.generate(
            **entradas,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
    novos = saida[0, entradas["input_ids"].shape[1]:]
    return tokenizer.decode(novos, skip_special_tokens=True).strip()


def extrair_json(texto):
    try:
        objeto = json.loads(texto[texto.index("{"): texto.rindex("}") + 1])
        return objeto if isinstance(objeto, dict) else None
    except (ValueError, json.JSONDecodeError):
        return None


def validar_saida(objeto):
    """Regra de negócio: a fonte só pode ser o ID de um documento da base; senão vira null."""
    if objeto is not None and objeto.get("fonte") not in documentos_por_id:
        objeto["fonte"] = None
    return objeto


def resposta_ao_cliente(objeto):
    if objeto is None:
        return RESPOSTA_ENCAMINHAMENTO
    if objeto.get("status") == "sem_informacao":
        return RESPOSTA_FORA_DA_BASE
    documento = documentos_por_id.get(objeto.get("fonte"))
    return documento["resposta_automatica"] if documento else RESPOSTA_ENCAMINHAMENTO


def responder(recursos, chamado, usar_rag, top_k, limiar):
    inicio = time.perf_counter()
    documentos = buscar_documentos(recursos, chamado, top_k, limiar) if usar_rag else []
    texto = gerar_texto(recursos, montar_prompt(recursos["tokenizer"], chamado, formatar_contexto(documentos)))
    objeto = validar_saida(extrair_json(texto))
    return {
        "texto": texto,
        "json": objeto,
        "resposta_cliente": resposta_ao_cliente(objeto),
        "documentos": [(d["id"], round(d["score"], 3)) for d in documentos],
        "usar_rag": usar_rag,
        "limiar": limiar,
        "tempo_s": time.perf_counter() - inicio,
    }


# -----------------------------------------------------------------------------
# Interface
# -----------------------------------------------------------------------------
def mostrar_resumo(saida):
    objeto = saida["json"]
    if objeto is None:
        st.warning("O modelo não gerou uma resposta válida — chamado encaminhado a um atendente.", icon="⚠️")
        return
    if objeto.get("status") == "sem_informacao":
        st.info("Fora da base de conhecimento — chamado encaminhado a um atendente.", icon="ℹ️")
        return
    documento = documentos_por_id.get(objeto.get("fonte"))
    colunas = st.columns(4)
    colunas[0].markdown(f"**Categoria**  \n{objeto.get('categoria', '—')}")
    colunas[1].markdown(f"**Prioridade**  \n{ROTULO_PRIORIDADE.get(objeto.get('prioridade'), objeto.get('prioridade', '—'))}")
    colunas[2].markdown(f"**Equipe**  \n{objeto.get('equipe', '—')}")
    colunas[3].markdown(f"**Base usada**  \n{objeto.get('fonte') or '—'}" + (f" — {documento['titulo']}" if documento else ""))


def mostrar_detalhes(saida):
    with st.expander("🔧 Detalhes técnicos (resposta estruturada do modelo)"):
        esquerda, direita = st.columns(2)
        with esquerda:
            st.markdown("**Resposta estruturada**")
            st.json(saida["json"] if saida["json"] is not None else {"erro": "JSON inválido"})
        with direita:
            st.markdown("**Documentos recuperados pelo RAG**")
            if saida["documentos"]:
                for doc_id, score in saida["documentos"]:
                    st.markdown(f"- **{doc_id}** — {documentos_por_id[doc_id]['titulo']} (similaridade {score:.3f})")
            elif saida["usar_rag"]:
                st.markdown(f"_Nenhum documento passou do limiar ({saida['limiar']})._")
            else:
                st.markdown("_RAG desligado._")
            st.markdown("**Texto bruto gerado pelo modelo**")
            st.code(saida["texto"], language="json")
        st.caption(f"⏱️ {saida['tempo_s']:.2f} s · dispositivo: {DEVICE}")


def mostrar_mensagem_assistente(saida):
    with st.chat_message("assistant", avatar="🛒"):
        st.markdown("**Resposta do assistente de atendimento**")
        st.markdown(saida["resposta_cliente"])
        mostrar_resumo(saida)
        mostrar_detalhes(saida)


config = ler_config()
recursos = carregar_recursos(config["modelo_base"], config["modelo_embedding"],
                             str(PASTA_PROJETO / config["adaptador"].replace("\\", "/")))

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Barra lateral: configurações, exemplos e informações do modelo
with st.sidebar:
    if st.button("🗑️ Limpar conversa", use_container_width=True):
        st.session_state.mensagens = []
        st.rerun()

    st.header("💡 Exemplos")
    exemplo_escolhido = None
    for exemplo in EXEMPLOS:
        if st.button(exemplo, use_container_width=True):
            exemplo_escolhido = exemplo

    st.header("🧠 Modelo")
    metricas = config.get("metricas_teste", {})
    st.markdown(
        f"- **LLM:** `{config['modelo_base'].split('/')[-1]}`\n"
        f"- **Adaptador LoRA:** `{config['melhor_experimento']}`\n"
        f"- **Embeddings:** `{config['modelo_embedding'].split('/')[-1]}`\n"
        f"- **Base:** {len(base_conhecimento)} documentos\n"
        f"- **top_k:** {TOP_K}\n"
        f"- **Limiar de similaridade:** {LIMIAR_RAG:.2f}"
    )
    if metricas:
        st.caption(
            f"No teste: JSON válido {metricas.get('json_valido', 0):.0%} · categoria {metricas.get('categoria', 0):.0%} · "
            f"status {metricas.get('status', 0):.0%} · pontuação {metricas.get('pontuacao', 0):.0%}"
        )
    if DEVICE == "cuda":
        st.caption(f"GPU: {torch.cuda.get_device_name(0)}")
    else:
        st.caption("Dispositivo: CPU (sem GPU) — as respostas podem levar alguns segundos a mais.")

# Área principal: conversa
st.title("🛒 Assistente de atendimento — Loja Virtual")
st.caption("SmolLM2-360M ajustado com LoRA + RAG sobre a base de políticas da loja.")

for mensagem in st.session_state.mensagens:
    if mensagem["papel"] == "user":
        with st.chat_message("user"):
            st.markdown(mensagem["texto"])
    else:
        mostrar_mensagem_assistente(mensagem["saida"])

chamado = st.chat_input("Descreva o problema do cliente...") or exemplo_escolhido

if chamado:
    with st.chat_message("user"):
        st.markdown(chamado)
    with st.spinner("Consultando a base e gerando a resposta..."):
        saida = responder(recursos, chamado.strip(), USAR_RAG, TOP_K, LIMIAR_RAG)
    mostrar_mensagem_assistente(saida)
    st.session_state.mensagens.append({"papel": "user", "texto": chamado})
    st.session_state.mensagens.append({"papel": "assistant", "saida": saida})
