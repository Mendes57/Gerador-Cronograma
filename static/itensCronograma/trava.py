from static.funcoes.coletaDados import dadosCliente
def trava():
    return [["*Trava de geladeira:*"],
            [f"Adquirir trava magnética - *{dadosCliente[0]}* -",
            f"Adquirir placa controladora para a trava (Link abaixo do cronograma) - *{dadosCliente[0]}* -",
            f"Adquirir Fonte 12v para placa (Link abaixo do cronograma) - *{dadosCliente[0]}* -",
            f"Adquirir caixa hermética p/ placa e fonte (Favor escolher a que mais se adeque ao seu caso) - *{dadosCliente[0]}* -",
            f"Envio de esquema elétrico para placa (Envio após o cronograma) - ACCESYS - ",
            f"Configuração do app para controle da trava - ACCESYS e {dadosCliente[0]} - ",]
            ]