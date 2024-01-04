#
# coleta dos dados do cliente e armazenamento na variavel dadosCliente
# Serão perguntados aqui
#
from static.funcoes.delayEClear import clear
from static.funcoes.checaErros import checaErros


def coletaDadosEChecaErros():
    clear()
    nomeLoja = input("Digite o nome do cliente: ")
    checaErros(nomeLoja)
    clear()
    totem = input("Que totem vai utilizar? \n1 - Totem M10 \n2 - Totem agSeguro \n3 - PagSeguro e M10 \n4 - Totem com raspberry pi \n5 - Totem com raspberry pi e PagSeguro ou M10 \n6 - Todas as opções \nResposta: ")
    checaErros(totem)
    
    pagSeguroOuM10 = input("\nQual outro totem irá utilizar? \n1 - PagSeguro \n2 - M10 \nResposta: "); checaErros(pagSeguroOuM10) if totem == 5 else 0
    clear()
    temApp = input("O cliente tem app? \n1 - Sim \n2 - Não \nResposta: ")
    checaErros(temApp)
    clear()
    temVendaApp = input("O cliente vai vender pelo app? \n1 - Sim \n2 - Não \nResposta: ") if temApp == 1 else 2
    checaErros(temVendaApp)
    clear()
    temImportacao = input('Vai ter importação de produtos? \n1 - Base deles \n2 - Nossa base \n3 - não vai ter \nResposta: ')
    checaErros(temImportacao)
    clear()
    temTrava = input('Vai utilizar trava de geladeira? \n1 - Sim \n2 - Não \nResposta: ')
    checaErros(temTrava)
    clear() 


    return [nomeLoja, int(totem), int(pagSeguroOuM10), int(temApp), int(temVendaApp), int(temImportacao), int(temTrava)]
