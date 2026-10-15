"""Base de conhecimento da loja virtual fictícia: 20 políticas criadas para o trabalho.

Cada documento tem:
- id, titulo, conteudo: o que o RAG busca e entrega ao modelo;
- categoria, prioridade, equipe, procedimento: o gabarito que o modelo aprende a devolver no JSON;
- resposta_automatica: a mensagem enviada ao cliente quando o modelo indica este documento como fonte.
"""

base_conhecimento = [
    {
        "id": "DOC-001",
        "titulo": "Atraso na entrega",
        "conteudo": (
            "Pedidos que ultrapassarem o prazo de entrega informado na compra devem ser "
            "verificados pelo código de rastreamento em Meus Pedidos. Se o atraso passar "
            "de 5 dias úteis, o cliente pode solicitar reenvio ou reembolso."
        ),
        "categoria": "entrega",
        "prioridade": "media",
        "equipe": "logistica",
        "procedimento": "Verificar o rastreamento em Meus Pedidos; após 5 dias úteis de atraso, solicitar reenvio ou reembolso.",
        "resposta_automatica": (
            "Olá! Sentimos muito pelo atraso. Você pode acompanhar a entrega pelo código de "
            "rastreamento em Meus Pedidos. Se o atraso passar de 5 dias úteis, é só solicitar "
            "o reenvio do produto ou o reembolso por lá. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-002",
        "titulo": "Produto com defeito ou danificado",
        "conteudo": (
            "Produtos com defeito ou que chegaram danificados podem ser devolvidos em até "
            "30 dias após o recebimento. O cliente deve enviar fotos do problema em Meus "
            "Pedidos e a coleta do produto é gratuita."
        ),
        "categoria": "defeito",
        "prioridade": "alta",
        "equipe": "trocas_devolucoes",
        "procedimento": "Enviar fotos do defeito em Meus Pedidos em até 30 dias e aguardar a coleta gratuita.",
        "resposta_automatica": (
            "Olá! Para produtos com defeito ou danificados, você pode solicitar a devolução em "
            "até 30 dias após o recebimento. Por favor, envie fotos do problema em Meus Pedidos. "
            "A coleta do produto é gratuita. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-003",
        "titulo": "Troca por arrependimento, tamanho ou cor",
        "conteudo": (
            "A troca por arrependimento, tamanho ou cor pode ser solicitada em até 7 dias "
            "após o recebimento. O produto deve estar sem uso e com a etiqueta."
        ),
        "categoria": "troca",
        "prioridade": "baixa",
        "equipe": "trocas_devolucoes",
        "procedimento": "Solicitar a troca em até 7 dias após o recebimento, com o produto sem uso e com etiqueta.",
        "resposta_automatica": (
            "Olá! Você pode solicitar a troca por arrependimento, tamanho ou cor em até 7 dias "
            "após o recebimento, direto em Meus Pedidos. O produto precisa estar sem uso e com "
            "a etiqueta. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-004",
        "titulo": "Prazo de reembolso",
        "conteudo": (
            "O reembolso é feito depois que o produto devolvido chega ao centro de "
            "distribuição. No cartão de crédito o estorno aparece em até 2 faturas; no Pix "
            "ou boleto o valor é devolvido em até 5 dias úteis."
        ),
        "categoria": "reembolso",
        "prioridade": "media",
        "equipe": "financeiro",
        "procedimento": "Aguardar o estorno em até 2 faturas no cartão ou até 5 dias úteis no Pix ou boleto.",
        "resposta_automatica": (
            "Olá! O reembolso é liberado assim que o produto devolvido chega ao nosso centro de "
            "distribuição. Se a compra foi no cartão de crédito, o estorno aparece em até 2 faturas; "
            "no Pix ou boleto, o valor é devolvido em até 5 dias úteis. Se precisar de mais ajuda, "
            "estamos à disposição!"
        ),
    },
    {
        "id": "DOC-005",
        "titulo": "Cancelamento de pedido",
        "conteudo": (
            "Pedidos que ainda não foram enviados podem ser cancelados em Meus Pedidos sem "
            "custo. Se o pedido já foi enviado, o cliente deve recusar a entrega e o valor "
            "é reembolsado após o retorno do produto."
        ),
        "categoria": "cancelamento",
        "prioridade": "media",
        "equipe": "atendimento",
        "procedimento": "Cancelar em Meus Pedidos se não foi enviado; se já foi enviado, recusar a entrega.",
        "resposta_automatica": (
            "Olá! Se o pedido ainda não foi enviado, você pode cancelá-lo sem custo em Meus Pedidos. "
            "Se ele já foi enviado, basta recusar a entrega: o valor será reembolsado assim que o "
            "produto retornar para nós. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-006",
        "titulo": "Pagamento recusado",
        "conteudo": (
            "Pagamentos recusados normalmente ocorrem por dados incorretos ou limite "
            "insuficiente no cartão. O cliente deve conferir os dados ou usar outra forma "
            "de pagamento. Boletos são compensados em até 3 dias úteis."
        ),
        "categoria": "pagamento",
        "prioridade": "alta",
        "equipe": "financeiro",
        "procedimento": "Conferir os dados e o limite do cartão ou usar outra forma de pagamento; boleto compensa em até 3 dias úteis.",
        "resposta_automatica": (
            "Olá! Pagamentos recusados geralmente acontecem por algum dado incorreto ou limite "
            "insuficiente no cartão. Confira os dados informados ou tente outra forma de pagamento. "
            "Se você pagou por boleto, a compensação pode levar até 3 dias úteis. Se precisar de "
            "mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-007",
        "titulo": "Cupom de desconto inválido",
        "conteudo": (
            "Cupons de desconto não são cumulativos, possuem data de validade e podem exigir "
            "valor mínimo de compra. O código deve ser digitado no carrinho antes de "
            "finalizar o pedido."
        ),
        "categoria": "cupom",
        "prioridade": "baixa",
        "equipe": "marketing",
        "procedimento": "Verificar validade e valor mínimo do cupom e aplicar um único código no carrinho antes de finalizar.",
        "resposta_automatica": (
            "Olá! Verifique se o cupom ainda está dentro da validade e se a compra atinge o valor "
            "mínimo exigido. Lembre-se de que os cupons não são cumulativos: apenas um código pode "
            "ser aplicado no carrinho, antes de finalizar o pedido. Se precisar de mais ajuda, "
            "estamos à disposição!"
        ),
    },
    {
        "id": "DOC-008",
        "titulo": "Compra não reconhecida ou suspeita de fraude",
        "conteudo": (
            "Compras não reconhecidas ou suspeita de acesso indevido à conta são prioridade "
            "crítica. O cliente deve trocar a senha imediatamente e o caso é encaminhado à "
            "equipe de Segurança, que bloqueia os pedidos suspeitos. A loja nunca pede "
            "senha por mensagem."
        ),
        "categoria": "fraude",
        "prioridade": "critica",
        "equipe": "seguranca",
        "procedimento": "Trocar a senha imediatamente e encaminhar à Segurança para bloquear os pedidos suspeitos.",
        "resposta_automatica": (
            "Olá! Por segurança, troque a senha da sua conta imediatamente. Seu caso foi encaminhado "
            "com prioridade à nossa equipe de Segurança, que vai bloquear os pedidos suspeitos. "
            "Importante: a loja nunca pede sua senha por mensagem. Se precisar de mais ajuda, "
            "estamos à disposição!"
        ),
    },
    {
        "id": "DOC-009",
        "titulo": "Alteração do endereço de entrega",
        "conteudo": (
            "O endereço de entrega só pode ser alterado enquanto o pedido não foi enviado, "
            "pela opção Alterar endereço em Meus Pedidos. Depois do envio, a alteração não é "
            "possível e o cliente pode recusar a entrega para receber o reembolso."
        ),
        "categoria": "endereco",
        "prioridade": "media",
        "equipe": "logistica",
        "procedimento": "Alterar o endereço em Meus Pedidos antes do envio; após o envio, recusar a entrega para receber o reembolso.",
        "resposta_automatica": (
            "Olá! Enquanto o pedido não for enviado, você pode alterar o endereço de entrega pela "
            "opção Alterar endereço em Meus Pedidos. Se ele já foi enviado, não é mais possível "
            "mudar o endereço, mas você pode recusar a entrega e receber o reembolso. Se precisar "
            "de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-010",
        "titulo": "Valor do frete e frete grátis",
        "conteudo": (
            "O valor do frete é calculado no carrinho a partir do CEP de entrega. Compras acima "
            "de R$ 199 têm frete grátis para todo o Brasil, exceto produtos de grande porte."
        ),
        "categoria": "frete",
        "prioridade": "baixa",
        "equipe": "atendimento",
        "procedimento": "Informar o CEP no carrinho para calcular o frete; compras acima de R$ 199 têm frete grátis, exceto produtos de grande porte.",
        "resposta_automatica": (
            "Olá! O valor do frete aparece no carrinho assim que você informa o CEP de entrega. "
            "Compras acima de R$ 199 têm frete grátis para todo o Brasil, exceto produtos de grande "
            "porte. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-011",
        "titulo": "Produto errado ou faltando no pedido",
        "conteudo": (
            "Se o cliente recebeu um produto diferente do comprado ou se faltou algum item no "
            "pedido, deve informar o problema em Meus Pedidos em até 7 dias após a entrega. A loja "
            "envia o item correto sem custo e agenda a coleta do produto errado."
        ),
        "categoria": "pedido_incorreto",
        "prioridade": "alta",
        "equipe": "logistica",
        "procedimento": "Informar em Meus Pedidos em até 7 dias após a entrega; a loja envia o item correto sem custo e coleta o produto errado.",
        "resposta_automatica": (
            "Olá! Sentimos muito pelo engano no seu pedido. Informe o problema em Meus Pedidos em "
            "até 7 dias após a entrega: vamos enviar o item correto sem custo e agendar a coleta do "
            "produto errado. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-012",
        "titulo": "Nota fiscal",
        "conteudo": (
            "A nota fiscal é enviada por e-mail e fica disponível para download em Meus Pedidos "
            "em até 24 horas após o envio do pedido. Dados da nota não podem ser alterados depois "
            "de emitida."
        ),
        "categoria": "nota_fiscal",
        "prioridade": "baixa",
        "equipe": "financeiro",
        "procedimento": "Baixar a nota fiscal em Meus Pedidos ou no e-mail em até 24 horas após o envio do pedido.",
        "resposta_automatica": (
            "Olá! A nota fiscal é enviada para o seu e-mail e também fica disponível para download "
            "em Meus Pedidos em até 24 horas após o envio do pedido. Os dados da nota não podem ser "
            "alterados depois de emitida. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-013",
        "titulo": "Garantia do fabricante",
        "conteudo": (
            "Depois de 30 dias do recebimento, defeitos são tratados pela garantia do fabricante. "
            "O cliente deve procurar a assistência técnica autorizada da marca, levando a nota "
            "fiscal da compra."
        ),
        "categoria": "garantia",
        "prioridade": "media",
        "equipe": "trocas_devolucoes",
        "procedimento": "Após 30 dias do recebimento, procurar a assistência técnica autorizada da marca com a nota fiscal.",
        "resposta_automatica": (
            "Olá! Depois de 30 dias do recebimento, o defeito passa a ser atendido pela garantia do "
            "fabricante. Procure a assistência técnica autorizada da marca e leve a nota fiscal da "
            "compra. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-014",
        "titulo": "Parcelamento e formas de pagamento",
        "conteudo": (
            "A loja aceita cartão de crédito, Pix e boleto. No cartão, compras acima de R$ 100 "
            "podem ser parceladas em até 10 vezes sem juros, com parcela mínima de R$ 30. "
            "Pagamentos no Pix têm 5% de desconto."
        ),
        "categoria": "parcelamento",
        "prioridade": "baixa",
        "equipe": "financeiro",
        "procedimento": "Parcelar em até 10x sem juros no cartão acima de R$ 100 (parcela mínima R$ 30) ou pagar no Pix com 5% de desconto.",
        "resposta_automatica": (
            "Olá! Aceitamos cartão de crédito, Pix e boleto. No cartão, compras acima de R$ 100 podem "
            "ser parceladas em até 10 vezes sem juros, com parcela mínima de R$ 30. No Pix você ganha "
            "5% de desconto. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-015",
        "titulo": "Acesso à conta e senha esquecida",
        "conteudo": (
            "Para recuperar o acesso, o cliente deve usar a opção Esqueci minha senha na tela de "
            "login. O link de redefinição é enviado para o e-mail cadastrado e expira em 30 minutos."
        ),
        "categoria": "conta",
        "prioridade": "media",
        "equipe": "suporte_tecnico",
        "procedimento": "Usar Esqueci minha senha na tela de login e abrir o link enviado ao e-mail em até 30 minutos.",
        "resposta_automatica": (
            "Olá! Para recuperar o acesso, clique em Esqueci minha senha na tela de login. Vamos "
            "enviar um link de redefinição para o seu e-mail cadastrado, que vale por 30 minutos. "
            "Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-016",
        "titulo": "Exclusão de conta e dados pessoais",
        "conteudo": (
            "O cliente pode pedir a exclusão da conta e dos dados pessoais em Minha Conta, na opção "
            "Privacidade, conforme a LGPD. O pedido é concluído em até 15 dias, e pedidos em "
            "andamento precisam ser finalizados antes."
        ),
        "categoria": "privacidade",
        "prioridade": "media",
        "equipe": "privacidade",
        "procedimento": "Solicitar a exclusão em Minha Conta > Privacidade; prazo de até 15 dias, após finalizar pedidos em andamento.",
        "resposta_automatica": (
            "Olá! Você pode solicitar a exclusão da sua conta e dos seus dados pessoais em Minha "
            "Conta, na opção Privacidade, conforme a LGPD. O pedido é concluído em até 15 dias, e "
            "os pedidos em andamento precisam ser finalizados antes. Se precisar de mais ajuda, "
            "estamos à disposição!"
        ),
    },
    {
        "id": "DOC-017",
        "titulo": "Programa de pontos",
        "conteudo": (
            "Cada real gasto vale 1 ponto no programa de fidelidade. Os pontos são creditados "
            "30 dias após a entrega do pedido, podem ser trocados por descontos e expiram em 12 meses."
        ),
        "categoria": "fidelidade",
        "prioridade": "baixa",
        "equipe": "marketing",
        "procedimento": "Aguardar o crédito dos pontos 30 dias após a entrega; os pontos valem descontos e expiram em 12 meses.",
        "resposta_automatica": (
            "Olá! No nosso programa de fidelidade, cada real gasto vale 1 ponto. Os pontos são "
            "creditados 30 dias após a entrega do pedido, podem ser trocados por descontos e expiram "
            "em 12 meses. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-018",
        "titulo": "Produto esgotado e aviso de disponibilidade",
        "conteudo": (
            "Quando um produto está esgotado, o cliente pode clicar em Avise-me na página do "
            "produto para receber um e-mail quando ele voltar ao estoque. A loja não reserva "
            "produtos esgotados nem informa data de reposição."
        ),
        "categoria": "estoque",
        "prioridade": "baixa",
        "equipe": "comercial",
        "procedimento": "Clicar em Avise-me na página do produto para ser avisado por e-mail quando houver estoque.",
        "resposta_automatica": (
            "Olá! Quando um produto está esgotado, clique em Avise-me na página dele: você recebe um "
            "e-mail assim que ele voltar ao estoque. Não conseguimos reservar produtos esgotados nem "
            "informar a data de reposição. Se precisar de mais ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-019",
        "titulo": "Problema no site ou no aplicativo",
        "conteudo": (
            "Erros no site ou no aplicativo costumam ser resolvidos limpando o cache do navegador "
            "ou atualizando o aplicativo para a versão mais recente. Se o problema continuar, o "
            "cliente deve enviar um print da tela de erro pelo chat de suporte."
        ),
        "categoria": "site_app",
        "prioridade": "alta",
        "equipe": "suporte_tecnico",
        "procedimento": "Limpar o cache do navegador ou atualizar o aplicativo; se continuar, enviar print do erro pelo chat de suporte.",
        "resposta_automatica": (
            "Olá! Na maioria dos casos, o problema se resolve limpando o cache do navegador ou "
            "atualizando o aplicativo para a versão mais recente. Se o erro continuar, envie um print "
            "da tela pelo chat de suporte para nossa equipe técnica analisar. Se precisar de mais "
            "ajuda, estamos à disposição!"
        ),
    },
    {
        "id": "DOC-020",
        "titulo": "Vale-presente",
        "conteudo": (
            "O vale-presente vale por 12 meses a partir da compra e pode ser usado como forma de "
            "pagamento, inclusive junto com outras. O saldo não usado fica disponível para compras "
            "futuras, mas não pode ser trocado por dinheiro."
        ),
        "categoria": "vale_presente",
        "prioridade": "baixa",
        "equipe": "financeiro",
        "procedimento": "Usar o vale-presente como pagamento em até 12 meses; o saldo fica para próximas compras e não vira dinheiro.",
        "resposta_automatica": (
            "Olá! O vale-presente vale por 12 meses a partir da compra e pode ser usado como forma de "
            "pagamento, inclusive junto com outras. O saldo que sobrar fica disponível para as "
            "próximas compras, mas não pode ser trocado por dinheiro. Se precisar de mais ajuda, "
            "estamos à disposição!"
        ),
    },
]

# Mensagem quando o modelo indica que a base não cobre o chamado (status "sem_informacao").
RESPOSTA_FORA_DA_BASE = (
    "Olá! Não encontramos uma resposta automática para a sua solicitação. "
    "Seu chamado foi encaminhado para um de nossos atendentes, que vai responder em breve. "
    "Obrigado pela paciência!"
)

# Mensagem quando a resposta do modelo não pode ser usada (JSON inválido ou fonte inexistente).
RESPOSTA_ENCAMINHAMENTO = (
    "Olá! Recebemos a sua mensagem e ela foi encaminhada para um de nossos atendentes, "
    "que vai responder em breve. Obrigado pela paciência!"
)
