from static.funcoes.coletaDados import dadosCliente

def desenvolvimento():
    return [["*Desenvolvimento:*"],

            [f"Geração de Tokens - ACCESYS - ",
            f"Envio de dados para desenvolvimento do app: Nome do aplicativo, Dados de identidade visual como: Logotipo, Ícone, Cores primária e secundária em hexadecimal(ou podemos obter as cores pelo logotipo) - *{dadosCliente[0]}* - ",
            f"Envio de base de dados em excel do planograma da loja (Código de barras, ncm, cest, descricao, qtd ideal, minima e maxima, custo, venda, categoria, tributações) - *{dadosCliente[0]}* - ",
            f"Análise da tabela de produtos - ACCESYS - "]
            ]