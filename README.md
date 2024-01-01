# Gerador-Cronograma

# Função geral e explicação da criação desse projeto:

Gera um cronograma que será utilizado como andamento das respectivas lojas
Criado como objeto de estudo em horas vagas e finais de semana

# Funcionalidade:

Coleta os dados, armazena e retorna a seguinte lista: nomeloja, totem, nomeOutroTotem, pagSeguroOuM10, temapp, temvendaapp, temimportacao, temtrava

Esses dados são passados para o gerador de cronograma onde ele formata as listas, zerando ou retirandos certos ítens para evitar ambiguidade, retornando e armazenando uma lista com todas as listas já modificadas para ficarem na ordem certa do cronograma, retorna mensagem de erro se possuir algum nos dados passados

A parte de coleta de dados e de gerar a lista armazenam as listas em variáveis que estão em seus respectivos arquivos, quase todos os ítens da lista utilizam esses dados para poderem mostrar o nome do cliente como responsável por seus ítens do cronograma

Após isso, a lista com a junção de todos os ítens do cronograma formatados é passada para a função de imprimir, que faz uma verificação se o gerador não retornou erros e imprime na tela todos os ítens recebidos
