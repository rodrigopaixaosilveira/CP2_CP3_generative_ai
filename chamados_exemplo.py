"""Chamados de exemplo usados no treino, na validação, no teste e na demonstração.

- modelos_chamados: 5 formas de escrever cada problema. As 4 primeiras vão para o treino e para o
  índice do RAG; a 5ª fica só para a validação (e para escolher o limiar do RAG).
- chamados_sem_base: perguntas que a base NÃO responde (exemplos negativos). As 2 últimas ficam
  só para a validação.
- casos_teste: 25 chamados inéditos (1 por documento + 5 fora da base), que não aparecem no treino,
  usados só na avaliação final.
- casos_demonstracao: 3 casos para comparar o antes x depois.
"""

modelos_chamados = {
    "DOC-001": [
        "Meu pedido está atrasado e ainda não chegou.",
        "O prazo de entrega já passou e não recebi nada.",
        "O rastreamento está parado há vários dias.",
        "A transportadora não entregou minha encomenda no prazo.",
        "Comprei há duas semanas e o pedido ainda não foi entregue.",
    ],
    "DOC-002": [
        "O produto chegou quebrado.",
        "O aparelho que comprei não liga.",
        "Recebi o item com defeito de fábrica.",
        "A peça veio danificada dentro da caixa.",
        "O produto parou de funcionar depois de poucos dias de uso.",
    ],
    "DOC-003": [
        "Quero trocar a camiseta por outro tamanho.",
        "Me arrependi da compra e quero devolver o produto.",
        "A cor do produto é diferente do que eu esperava, posso trocar?",
        "O tênis ficou pequeno, como faço a troca?",
        "Recebi ontem e não gostei, quero trocar por outro modelo.",
    ],
    "DOC-004": [
        "Devolvi o produto e ainda não recebi meu dinheiro de volta.",
        "Quando o estorno vai aparecer na fatura do cartão?",
        "Paguei com Pix e quero saber quando sai o reembolso.",
        "O valor da devolução ainda não caiu na minha conta.",
        "Quanto tempo demora para receber o reembolso?",
    ],
    "DOC-005": [
        "Quero cancelar meu pedido.",
        "Comprei por engano e preciso desistir da compra antes do envio.",
        "Como faço para cancelar uma compra que acabei de fazer?",
        "Não quero mais o pedido, ele ainda não foi enviado.",
        "O pedido já saiu para entrega, mas quero cancelar.",
    ],
    "DOC-006": [
        "Meu cartão foi recusado na hora de finalizar a compra.",
        "O pagamento não foi aprovado.",
        "Aparece erro no pagamento quando tento pagar com cartão.",
        "Paguei o boleto mas o pedido continua aguardando pagamento.",
        "A compra não é concluída porque o pagamento falha.",
    ],
    "DOC-007": [
        "Meu cupom de desconto não funciona.",
        "O código promocional aparece como inválido.",
        "O desconto do cupom não foi aplicado no carrinho.",
        "Posso usar dois cupons na mesma compra?",
        "O cupom diz que está expirado.",
    ],
    "DOC-008": [
        "Apareceu uma compra que eu não fiz na minha conta.",
        "Acho que invadiram minha conta e fizeram pedidos.",
        "Recebi cobrança de um pedido que não reconheço.",
        "Alguém alterou meu endereço e comprou com meu cartão.",
        "Recebi uma mensagem pedindo minha senha em nome da loja.",
    ],
    "DOC-009": [
        "Preciso mudar o endereço de entrega do meu pedido.",
        "Coloquei o endereço errado na compra.",
        "Me mudei e quero receber o pedido em outro lugar.",
        "Dá para trocar o CEP de entrega depois de comprar?",
        "Esqueci de colocar o número do apartamento no endereço.",
    ],
    "DOC-010": [
        "Quanto custa o frete para o meu CEP?",
        "A partir de quanto o frete é grátis?",
        "Por que o frete ficou tão caro?",
        "Vocês entregam no Brasil todo com frete grátis?",
        "Como calculo o valor da entrega antes de comprar?",
    ],
    "DOC-011": [
        "Recebi um produto diferente do que comprei.",
        "Veio a cor errada no meu pedido.",
        "Faltou um item na minha caixa.",
        "Comprei dois produtos e só chegou um.",
        "Mandaram o modelo errado do celular.",
    ],
    "DOC-012": [
        "Onde encontro a nota fiscal da minha compra?",
        "Não recebi a nota fiscal por e-mail.",
        "Preciso da nota fiscal para a empresa.",
        "Como baixo a NF do meu pedido?",
        "A nota fiscal saiu com meu nome errado.",
    ],
    "DOC-013": [
        "Comprei há 3 meses e o produto parou de funcionar.",
        "Meu liquidificador quebrou depois de seis meses de uso.",
        "Como aciono a garantia do fabricante?",
        "Onde fica a assistência técnica autorizada?",
        "O produto tem garantia depois de um mês?",
    ],
    "DOC-014": [
        "Em quantas vezes posso parcelar?",
        "Tem desconto pagando no Pix?",
        "Quais formas de pagamento vocês aceitam?",
        "Posso parcelar sem juros no cartão?",
        "Qual é o valor mínimo da parcela?",
    ],
    "DOC-015": [
        "Esqueci a senha da minha conta.",
        "Não consigo fazer login no site.",
        "O link para redefinir a senha não funciona.",
        "Minha conta não aceita a senha que eu sempre uso.",
        "Como recupero o acesso à minha conta?",
    ],
    "DOC-016": [
        "Quero excluir minha conta.",
        "Como apago meus dados pessoais do site?",
        "Não quero mais que vocês guardem minhas informações.",
        "Quero exercer meu direito da LGPD.",
        "Como faço para encerrar meu cadastro?",
    ],
    "DOC-017": [
        "Meus pontos da compra ainda não apareceram.",
        "Como funciona o programa de pontos?",
        "Meus pontos venceram?",
        "Como troco meus pontos por desconto?",
        "Quantos pontos eu ganho por compra?",
    ],
    "DOC-018": [
        "O produto que eu quero está esgotado.",
        "Quando o produto volta ao estoque?",
        "Vocês podem reservar um item esgotado para mim?",
        "Aparece indisponível no tamanho que eu preciso.",
        "Como sei quando o produto voltar a ter estoque?",
    ],
    "DOC-019": [
        "O aplicativo fecha sozinho quando abro.",
        "O site fica em branco quando tento entrar.",
        "A página não carrega no meu celular.",
        "O botão de comprar não funciona no site.",
        "O app está travando na tela inicial.",
    ],
    "DOC-020": [
        "Como uso meu vale-presente?",
        "Meu vale-presente ainda está válido?",
        "Posso trocar o vale-presente por dinheiro?",
        "Sobrou saldo no meu vale-presente, o que acontece?",
        "Ganhei um cartão-presente da loja, como funciona?",
    ],
}

chamados_sem_base = [
    "Vocês têm loja física em Campinas?",
    "Vocês estão contratando?",
    "Qual é a melhor televisão para comprar?",
    "Vocês vendem carros?",
    "Como faço para virar revendedor da marca?",
    "Qual o telefone da assessoria de imprensa?",
    "Quando começa a Black Friday?",
    "Vocês patrocinam eventos esportivos?",
    "Vocês alugam produtos?",
    "Qual é o endereço do escritório?",
    "Qual é a história da empresa?",
    "Vocês fazem conserto de bicicletas?",
    "Qual é o CNPJ da empresa?",
    "Qual é a previsão do tempo para amanhã?",
]

casos_teste = [
    {"chamado": "Já passaram dez dias e minha encomenda não apareceu.", "doc": "DOC-001", "categoria": "entrega", "prioridade": "media", "status": "respondido"},
    {"chamado": "A tela do notebook veio trincada.", "doc": "DOC-002", "categoria": "defeito", "prioridade": "alta", "status": "respondido"},
    {"chamado": "A calça não serviu, quero outra numeração.", "doc": "DOC-003", "categoria": "troca", "prioridade": "baixa", "status": "respondido"},
    {"chamado": "Mandei o produto de volta, quando recebo o valor que paguei?", "doc": "DOC-004", "categoria": "reembolso", "prioridade": "media", "status": "respondido"},
    {"chamado": "Desisti da compra que fiz hoje cedo, dá para anular?", "doc": "DOC-005", "categoria": "cancelamento", "prioridade": "media", "status": "respondido"},
    {"chamado": "A transação foi negada no checkout.", "doc": "DOC-006", "categoria": "pagamento", "prioridade": "alta", "status": "respondido"},
    {"chamado": "O código de desconto da newsletter não é aceito.", "doc": "DOC-007", "categoria": "cupom", "prioridade": "baixa", "status": "respondido"},
    {"chamado": "Tem um pedido no meu histórico que eu nunca fiz.", "doc": "DOC-008", "categoria": "fraude", "prioridade": "critica", "status": "respondido"},
    {"chamado": "Errei o número da casa no endereço, ainda dá para corrigir?", "doc": "DOC-009", "categoria": "endereco", "prioridade": "media", "status": "respondido"},
    {"chamado": "Comprando R$ 250 eu pago entrega?", "doc": "DOC-010", "categoria": "frete", "prioridade": "baixa", "status": "respondido"},
    {"chamado": "Pedi uma panela e chegou uma frigideira.", "doc": "DOC-011", "categoria": "pedido_incorreto", "prioridade": "alta", "status": "respondido"},
    {"chamado": "Preciso do documento fiscal para declarar no imposto.", "doc": "DOC-012", "categoria": "nota_fiscal", "prioridade": "baixa", "status": "respondido"},
    {"chamado": "Minha geladeira comprada no ano passado parou de gelar.", "doc": "DOC-013", "categoria": "garantia", "prioridade": "media", "status": "respondido"},
    {"chamado": "Dá para dividir a compra no cartão?", "doc": "DOC-014", "categoria": "parcelamento", "prioridade": "baixa", "status": "respondido"},
    {"chamado": "Não lembro a senha e não consigo entrar.", "doc": "DOC-015", "categoria": "conta", "prioridade": "media", "status": "respondido"},
    {"chamado": "Quero que vocês apaguem todo o meu cadastro.", "doc": "DOC-016", "categoria": "privacidade", "prioridade": "media", "status": "respondido"},
    {"chamado": "Quando os pontos da minha última compra vão cair?", "doc": "DOC-017", "categoria": "fidelidade", "prioridade": "baixa", "status": "respondido"},
    {"chamado": "O fone que eu queria acabou, vai chegar mais?", "doc": "DOC-018", "categoria": "estoque", "prioridade": "baixa", "status": "respondido"},
    {"chamado": "O app não abre desde a última atualização.", "doc": "DOC-019", "categoria": "site_app", "prioridade": "alta", "status": "respondido"},
    {"chamado": "Tenho um gift card, posso usar junto com o cartão de crédito?", "doc": "DOC-020", "categoria": "vale_presente", "prioridade": "baixa", "status": "respondido"},
    {"chamado": "Qual é o salário inicial de um vendedor?", "doc": None, "categoria": "fora_da_base", "prioridade": "baixa", "status": "sem_informacao"},
    {"chamado": "Vocês têm canal no YouTube?", "doc": None, "categoria": "fora_da_base", "prioridade": "baixa", "status": "sem_informacao"},
    {"chamado": "Qual é o horário de funcionamento do escritório central?", "doc": None, "categoria": "fora_da_base", "prioridade": "baixa", "status": "sem_informacao"},
    {"chamado": "Quem é o dono da empresa?", "doc": None, "categoria": "fora_da_base", "prioridade": "baixa", "status": "sem_informacao"},
    {"chamado": "Vocês fazem doações para ONGs?", "doc": None, "categoria": "fora_da_base", "prioridade": "baixa", "status": "sem_informacao"},
]

casos_demonstracao = [
    {"nome": "Entrega atrasada", "chamado": "Meu pedido deveria ter chegado semana passada e até agora nada."},
    {"nome": "Compra suspeita", "chamado": "Alguém fez uma compra com meu cartão na minha conta sem eu saber."},
    {"nome": "Informação ausente", "chamado": "Vocês têm loja física no Rio de Janeiro?"},
]
