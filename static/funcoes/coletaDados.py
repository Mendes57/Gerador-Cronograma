#
# coleta dos dados do cliente e armazenamento na variavel dadosCliente
# Serão perguntados aqui
#
from static.funcoes.limpatela import clear

dadosCliente = []

def coletaDados():
    clear()
    nomeLoja = input("Digite o nome do cliente: ")
    clear()
    totem = int(input("Que totem vai utilizar? \n1 - Totem M10 \n2 - Totem PagSeguro \n3 - PagSeguro e M10 \n4 - Outro Totem \n5 - Outro totem e PagSeguro ou M10 \n6 - Todas as opções \nResposta: "))
    
    nomeOutroTotem = input("\nDigite o nome do totem: ") if totem in {4, 5, 6} else ""
    
    pagSeguroOuM10 = int(input("\nQual outro totem irá utilizar? \n1 - PagSeguro \n2 - M10 \nResposta: ")) if totem == 5 else ""
    clear()
    temApp = int(input("O cliente tem app? \n1 - Sim \n2 - Não \nResposta: "))
    clear()
    temVendaApp = int(input("O cliente vai vender pelo app? \n1 - Sim \n2 - Não \nResposta: "))
    clear()
    temImportacao = int(input('Vai ter importação de produtos? \n1 - Base deles \n2 - Nossa base \n3 - não vai ter \nResposta: '))
    clear()
    temTrava = int(input('Vai utilizar trava de geladeira? \n1 - Sim \n2 - Não \nResposta: '))
    clear() 


    dadosCliente.extend([nomeLoja, totem, nomeOutroTotem, pagSeguroOuM10, temApp, temVendaApp, temImportacao, temTrava])
    return dadosCliente