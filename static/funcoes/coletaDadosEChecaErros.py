from static.funcoes.delayEClear import clear
from static.funcoes.checaErros import checaErros

dadosCliente = []

def coletaDadosEChecaErros():
    clear()
    nomeLoja = checaErros(input("Digite o nome do cliente: "))
    clear()
    totem = checaErros(input("Que totem vai utilizar? \n1 - Totem M10 \n2 - Totem agSeguro \n3 - PagSeguro e M10 \n4 - Totem com raspberry pi \n5 - Totem com raspberry pi e PagSeguro ou M10 \n6 - Todas as opções \nResposta: "))
    
    pagSeguroOuM10 = checaErros(input("\nQual outro totem irá utilizar?\n1 - PagSeguro\n2 - M10\nResposta: ")) if totem == "3" else "0"
    clear()
    temApp = checaErros(input("O cliente tem app? \n1 - Sim \n2 - Não \nResposta: "))
    clear()
    temVendaApp = checaErros(input("O cliente vai vender pelo app? \n1 - Sim \n2 - Não \nResposta: ") if temApp == "1" else "2")
    clear()
    temImportacao = checaErros(input('Vai ter importação de produtos? \n1 - Base deles \n2 - Nossa base \n3 - não vai ter \nResposta: '))
    clear()
    temTrava = checaErros(input('Vai utilizar trava de geladeira? \n1 - Sim \n2 - Não \nResposta: '))
    clear() 

    dadosCliente.extend([nomeLoja, int(totem), int(pagSeguroOuM10), int(temApp), int(temVendaApp), int(temImportacao), int(temTrava)])
    return dadosCliente
