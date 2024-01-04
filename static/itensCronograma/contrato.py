from static.funcoes.coletaDadosEChecaErros import dadosCliente

def contrato():
    return [["*Contrato Social:*"],
            [f"Envio de Contrato - *{dadosCliente[0]}* - ",
            f"Assinatura via Docusign - *{dadosCliente[0]}* - ",
            f"Pagamentos do Start - *{dadosCliente[0]}* - ",]
            ]