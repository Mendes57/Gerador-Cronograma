from static.funcoes.coletaDadosEChecaErros import dadosCliente

def app():
    return [["*APP:*"],
            [f"Coleta de tokens para homologação do app - ACCESYS e *{dadosCliente[0]}* - ",
            f"Homologação do Gateway de pagamento - ACCESYS - ",
            f"Aprovação do app nas lojas Android/IOS - ACCESYS - "]
            ]