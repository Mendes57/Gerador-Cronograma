from static.funcoes.coletaDadosEChecaErros import dadosCliente
def sitef():
    return [["*SiTef:*"], 
            [f"Contratação da Operadora de Cartões (Abaixo do cronograma) - *{dadosCliente[0]}* - ",
            f"Coleta de informações para o TEF (Abaixo do cronograma) - ACCESYS e *{dadosCliente[0]}* - ",
            f"Coleta de informações para o PIX (Abaixo do cronograma) - ACCESYS e *{dadosCliente[0]}* - ",
            f"Contratação da licença TEF junto a Software Express - ACCESYS - ",]
            ]

