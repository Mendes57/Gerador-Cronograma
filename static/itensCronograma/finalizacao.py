from static.funcoes.coletaDadosEChecaErros import dadosCliente

def finalizacao():
    return [["*Finalzação:*"],
            [f"Criação e envio de credenciais de Acesso Web, Favor fornecer nome, e-mail e número de telefone com DDD para cada usuário que desejam criar - ACCESYS e *{dadosCliente[0]}* - ",
            f"Envio de código para cadastrar envio de mensagens no Telegram - ACCESYS - ",
            f"QR Code para acessar loja pelo app - ACCESYS - ",
            f"Agendar data para treinamento geral (Mais longo mas contem todos os módulos) ou somente de manutenção de produtos (Mostra somente como cadastrar e editar produtos, inauguração rápida da loja, requer treinamento geral pós inauguração) - ACCESYS e *{dadosCliente[0]}* - ",
            f"Preparação para Go Live (Teste de leitura dos produtos, verificar precificação e teste de vendas) - *{dadosCliente[0]}* - ",
            f"Inauguração da primeira loja - ACCESYS e *{dadosCliente[0]}* - "]
            ]