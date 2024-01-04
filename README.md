# Gerador-Cronograma

# Função geral e explicação da criação desse projeto:

Gera um cronograma que será utilizado como andamento das respectivas lojas.
Criado como objeto de estudo em horas vagas e finais de semana.

# Funcionalidade:

Coleta e armazena os dados, Ajusta as listas de acordo com os dados do cliente e imprime na tela o ítens ajustados e editados para cada tipo de cronograma.


# Funções:

## limpaTela:

utiliza as bibliotecas "os" e "time" para a função de limpar o cmd, possui um delay de 0,1 segundos, um clear e mais um delay de 0,1s.

## coletaDados:

Coleta os dados do cliente que vamos usar para gerar o cronograma, checa se os dados possuem algum erro com a função checaErros() e os dados são armazenados em uma lista com as variáveis:

nomeLoja, totem, pagSeguroOuM10, temApp, temVendaApp, temImportacao, temTrava

## checaErros:

Verifica se possui algum erro nos valores atribuidos as variaveis, printa mensagem de erro, indicando a variável errada e para a execução do programa, se não encontrar erros retorna o valor inserido

## geraCronograma:

Os dados do cliente já verificados são passados para o gerador de cronograma onde ele formata as listas, zerando ou retirandos certos ítens para evitar ambiguidade, retornando e armazenando uma lista com as variáveis:

contrato_mut, desenvolvimento_mut, sitef_mut, m10_mut, pagseguro_mut, outroTotem_mut, trava_mut, erp_mut, app_mut, finalizacao_mut, linksm10_mut, linkspagseguro_mut, linksOutroTotem_mut, linkstrava_mut, dadossitef_mut

## printaCrono:

Após isso, a lista com a junção de todos os ítens do cronograma formatados é passada para a função printaCrono, que imprime na tela todos os ítens recebidos.