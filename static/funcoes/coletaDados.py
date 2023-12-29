#
# coleta dos dados do cliente e armazenamento na variavel dadosCliente
# Serão perguntados aqui
#
from static.funcoes.limpatela import clear

dadosCliente = []

def coletaDados():
    clear()
    nomeloja = input("Digite o nome do cliente: ")
    clear()
    totem = int(input("Que totem vai utilizar? \n1 - Totem M10 \n2 - Totem PagSeguro \n3 - Ambos \n4 - Outros \nResposta: "))
    clear()
    temapp = int(input("O cliente tem app? \n1 - Sim \n2 - Não \nResposta: "))
    clear()
    temvendaapp = int(input("O cliente vai vender pelo app? \n1 - Sim \n2 - Não \nResposta: "))
    clear()
    temimportacao = int(input('Vai ter importação de produtos? \n1 - Base deles \n2 - Nossa base \n3 - não vai ter \nResposta: '))
    clear()
    temtrava = int(input('Vai utilizar trava de geladeira? \n1 - Sim \n2 - Não \nResposta: '))
    clear() 


    dadosCliente.extend([nomeloja, totem, temapp, temvendaapp, temimportacao, temtrava])
    return dadosCliente