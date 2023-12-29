#Antigo estilo de cronograma, era feito baseado em cronogramas antigos

from static.funcoes.limpatela import clear
lugar = None
nome_totem = None




clear()

nome_loja = input('Qual o nome da nova loja? ')

clear()

localidade = input('De onde é essa loja? ')

clear()

usa_totem = int(input('Que totem vai utilizar? \n1 - Totem M10 \n2 - Totem PagSeguro \n3 - Ambos \n4 - Outros \nResposta: '))
if usa_totem == 1 or usa_totem == 3:
    usa_tef = 1
elif usa_totem == 2:
    usa_tef = 2
elif usa_totem == 4:
    clear()
    nome_totem = input('Qual o nome do totem? ')
    clear()
    usa_tef = int(input('Vai utilizar TEF? \n1 - Sim \n2 - Não \nResposta: '))
    clear()
    usa_Leitor = int(input('Vai utilizar leitor de código de barras? \n1 - Sim \n2 - Não \nResposta: '))
    clear()
    usa_PinPad = int(input('Vai utilizar PinPad? \n1 - Sim \n2 - Não \nResposta: '))

clear()

usa_app = int(input('Vai utilizar app? \n1 - Sim \n2 - Não \nResposta: '))

clear()

usa_trava = int(input('Vai utilizar trava de geladeira? \n1 - Sim \n2 - Não \nResposta: '))

clear()

usa_importacao_produtos = int(input('Vai ter importação de produtos? \n1 - Base deles \n2 - Nossa base \n3 - não vai ter \nResposta: '))

clear()






#Questões de contrato
obrigatorio = [
    f"Envio do contrato social do CNPJ -->  Responsável: {nome_loja} --> PRAZO:",
    f"Assinatura(via docusign) do contrato --> Responsável: {nome_loja} --> PRAZO:",
    f"Faturamento//pagamento dos valores do contrato --> Responsável: {nome_loja} --> PRAZO:\n"
]

#FEITO


#Listas de compra de totem

#Totem M10
compraM10 = [
    f"\nCompra de equipamentos, Totem Elgin Bematech M10, Leitor de código de barras USB e Pinpad --> Responsável: {nome_loja} --> PRAZO:\nElgin Bematech M10: https://produto.mercadolivre.com.br/MLB-2039561157-pdv-android-cimpressora-auto-atendimento-m10-elgin-bematech-_JM#position=3&search_layout=stack&type=item&tracking_id=e86f182b-70ac-41fc-92e3-808a87236cc8 \nLeitor de código de barras (pode ser qualquer modelo com conexão USB) Ex.: https://www.mercadolivre.com.br/leitor-de-codigo-de-barras-semi-fixo-jetway-jl-500-1d-2d-usb-cor-preto-tipo-de-conector-do-cabo-usb-voltagem-5v/p/MLB23444671?pdp_filters=category:MLB1648#searchVariation=MLB23444671&position=1&search_layout=grid&type=product&tracking_id=a8ae9128-0487-4377-947b-8375962b703e \nPinpad Gertec PPC930 (geralmente é disponibilizado pela adquirente ou banco) https://produto.mercadolivre.com.br/MLB-3191802432-pin-pad-criptografado-gertec-ppc-930-usb-contactless-_JM#is_advertising=true&position=2&search_layout=stack&type=pad&tracking_id=8d22acd2-6251-49c1-b8df-597e63791a0b&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=2&ad_click_id=YjU1ODFlNmYtYjYzNS00ZmQzLWEwNDktMmQ5ZmIxNmVjMzA2 \n"
]

configM10 = [
    f"Instalação, configuração e testes no totem elgin bematech m10, retirar tela de bloqueio do Android ao inicializar, solicitar ao cliente para conectar a bateria interna do m10 que vem desconectada. --> Responsável: Matheus Mendes --> PRAZO:\n"
]

#Totem PagSeguro
compraPagSeguro = [
    f"Compra de equipamentos para a loja (SmartPagseguro, Leitor código de barras e hub usb) --> Responsável: {nome_loja} --> PRAZO:\nSMART PAGSEGURO: https://pagseguro.uol.com.br/para-seu-negocio/maquininhas/moderninha-smart-2 \nHUB USB: https://produto.mercadolivre.com.br/MLB-3208310075-hub-adaptador-extensor-hdmi-4k-tipo-c-3-em-1-usb-30-pd-_JM#position=8&search_layout=stack&type=item&tracking_id=dc4fa7bc-c7c4-48f4-8fbb-256a6bcc181a \nOpção de Leitor de Código de Barras, pode ser qualquer um modelo USB, EX: https://www.mercadolivre.com.br/leitor-de-codigo-de-barras-semi-fixo-jetway-jl-500-1d-2d-usb-cor-preto-tipo-de-conector-do-cabo-usb-voltagem-5v/p/MLB23444671?pdp_filters=category:MLB1648#searchVariation=MLB23444671&position=1&search_layout=grid&type=product&tracking_id=6e2c97e9-3ccb-4538-94d7-f7d19eebea2f\n",
    f"Caso não tiver, criar conta pagseguro e fazer verificação de segurança da conta --> Responsável: {nome_loja} --> PRAZO:\n"
]

configPagSeguro = [
    f"Smart PagSeguro --> Vinculo do número de série da smart com o sistema, instalação do app e testes de vendas(Crédito, Débito, PIX) --> Responsável: @Matheus Mendes --> PRAZO:\n"
]


#Outro tipo de totem
compra_Outro_Totem = [
    f"Compra de equipamentos, Totem {nome_totem} --> Responsável: {nome_loja} --> PRAZO:\n"
]

compraLeitor = [
    f"Compra de leitor de código de barras (pode ser qualquer modelo com conexão USB) Ex.: https://www.mercadolivre.com.br/leitor-de-codigo-de-barras-semi-fixo-jetway-jl-500-1d-2d-usb-cor-preto-tipo-de-conector-do-cabo-usb-voltagem-5v/p/MLB23444671?pdp_filters=category:MLB1648#searchVariation=MLB23444671&position=1&search_layout=grid&type=product&tracking_id=a8ae9128-0487-4377-947b-8375962b703e --> Responsável: {nome_loja} --> PRAZO:\n"
    ]

compraPinPad = [
    f"Compra de pinpad Gertec PPC930 (geralmente é disponibilizado pela adquirente ou banco) https://produto.mercadolivre.com.br/MLB-3191802432-pin-pad-criptografado-gertec-ppc-930-usb-contactless-_JM#is_advertising=true&position=2&search_layout=stack&type=pad&tracking_id=8d22acd2-6251-49c1-b8df-597e63791a0b&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=2&ad_click_id=YjU1ODFlNmYtYjYzNS00ZmQzLWEwNDktMmQ5ZmIxNmVjMzA2 --> Responsável: {nome_loja} --> PRAZO:\n"
    ]

config_Outro_Totem = [
    f"Instalação, configuração e testes no totem, retirar tela de bloqueio do Android ao inicializar. --> Responsável: Matheus Mendes --> PRAZO:\n"
]




#Listas caso tenha app da PagSeguro
desenvApp = [
    f"Envio das informações necessárias para desenvolvimento do app --> Responsável: {nome_loja} --> PRAZO:\nNome do aplicativo, Dados de identidade visual como: Logotipo, Ícone, Cores primária e secundária em hexadecimal(ou podemos obter as cores pelo logotipo).\n"
]

validaPagSeguro = [
    f"Contratação de gateway de pagamento Paseguro para o aplicativo e fazer validação de segurança da conta --> Responsável: {nome_loja} PRAZO:\n",
    ]

gatewaysApp = [
    f"Coleta das informações necessárias do gateway de pagamento e configuração do app na plataforma --> Responsável: MATHEUS e {nome_loja} - PRAZO:\n",
    f"Homologação do gateway de pagamento da PagSeguro --> Responsável: ACCESYS --> PRAZO:\n",
    f"Desenvolvimento, publicação e aprovação do app noas lojas Android e iOS --> Responsável: NAIARA - PRAZO:\n"
]


qrCApp = [
    f"Envio do QRCODE da loja para compra pelo aplicativo --> Responsável: DENIS --> PRAZO:\n"
    ]


#Listas caso tenha importação de produtos
importacaoDeles = [
    f"Envio de base de dados em excel do planograma da loja(Código de barras, ncm, cest, descricao, qtd ideal, minima e maxima, custo, venda, categoria, tributações) --> Responsável: {nome_loja} --> PRAZO:\n",
    f"Desenvolvimento de importação de dados da base em excel que foi enviada --> Responsável: ACCESYS --> PRAZO:\n",
]

executImportacaoDeles = [
    f"Executar importação de produtos, testes de envio a plataforma --> Responsável: Matheus Mendes --> PRAZO:\n"
]

importacaoNossaBase = [
    f"Envio de base de produtos micromarket, testes de envio para a plataforma --> Responsável: Matheus Mendes --> PRAZO:\n"
]


#Listas para o servidor
acessoServidor = [
    f"Disponibilização de Anydesk ou team viewer do servidor local para instalações --> Responsável: {nome_loja} PRAZO:\nConfiguração mínima: Intel core i5 8ª geração, 8GB RAM(Recomendável 16GB), 256 hd ssd \n",
    f"Verificação de internet local e roteador para configuração de serviços --> Responsável: ACCESYS --> PRAZO:\n"
]

installServidor = [
    f"Instalação de ERP AccMarket, configurações de serviços e internet --> Responsável: Matheus Mendes - PRAZO:\n"
]


#Listas caso tenha TEF
infosTef = [
    f"Confirmar adquirente para TEF e enviar dados necessários para solicitação da licença. --> Responsável: {nome_loja} --> PRAZO:\nAdquirentes compatíveis: Adiq, Getnet, Safra, Acqio, Globalpayments, Stone, Bin, PagSeguro, Única, Cielo, Rede, Vero \nEnviar: CNPJ,Razão Social,Nome Fantasia,Contato(Responsável),Telefone(Responsável),Email(Responsável), Adquirente/Operadora,Número Lógico, Bandeiras utilizadas(débito,crédito,Voucher,PIX...).\n",
    f"Confirmar instituição bancária para configuração do PIX no TEF. --> Responsável: {nome_loja} --> PRAZO:\nBancos aceitos pelo Sitef: Banco do Brasil, Bradesco, Gerencianet, Itaú, Mercado Pago, Verdecard, Santander, Sicoob, Sicredi, Tribanco, Ailos, Realize CFI, Banco Original, Senff \n",
    f"Contratação da licença TEF junto a Software Express --> Responsável: MATHEUS --> PRAZO:\n",
]

certificadoDigital = [
    f"Verificar se possui certificado digital e opção de emissão de NFCe para todas as vendas --> Responsável: MATHEUS e {nome_loja} --> PRAZO:\n"
    ]


#loja é de SP?

#    NÃO PRECISA MAIS DE SAT

# sat = [
#     f" Verificar se irá emitir cupom fiscal. Compra do equipamento SAT Fiscal, Ativação junto a SEFAZ e instalação no Servidor (Opcional) --> Responsável: {nome_loja} --> PRAZO:\n"
#     ]
#Verificar se possui certificado digital ou equipamento SAT Fiscal e opção de emissão de NFCe para todas as vendas


#Vai ter trava de geladeira?
trava= [
    f"Configuração da trava de geladeira no start da loja e envio da trava ao cliente --> Responsável:  DENIS --> PRAZO: \n"
]


#Denis
denis = [
    f"Start da loja piloto na plataforma LojaExpress --> Responsável: DENIS --> PRAZO:\n",
    f"Criação das credenciais de acesso a gestão web --> Responsável: DENIS --> PRAZO:\n",
    f"Adicionar a configuração do Telegram para recebimento de monitoramento totem --> Responsável: DENIS --> PRAZO:\n",
]


#Ultimos itens da lista final
ultimo = [
    f"Treinamentos testes gerais da plataforma e ERP --> Responsável: Matheus Mendes --> PRAZO:\n",
    f"Preparação para Go live: escanear todos os produtos da loja no totem de atendimento, conferir cadastro e preços \nrealizar uma venda no Crédito, Débito e PIX e conferir na conta bancária o valor --> Responsável: Matheus Mendes --> PRAZO:\n",
    f"Go live da primeira loja e acompanhamento remoto --> Responsável: Matheus Mendes E {nome_loja} --> PREVISÃO:\n"
]


if usa_totem == 1:
    compraPagSeguro.clear()
    compra_Outro_Totem.clear()
    compraLeitor.clear()
    compraPinPad.clear()
    configPagSeguro.clear()
    config_Outro_Totem.clear()
if usa_totem ==2:
    compraM10.clear()
    compra_Outro_Totem.clear()
    compraLeitor.clear()
    compraPinPad.clear()
    configM10.clear()
    config_Outro_Totem.clear()
    validaPagSeguro.clear()
if usa_totem == 3:
    compra_Outro_Totem.clear()
    compraLeitor.clear()
    compraPinPad.clear()
    config_Outro_Totem.clear()
    validaPagSeguro.clear()
if usa_totem == 4:
    compraM10.clear()
    compraPagSeguro.clear()
    configM10.clear()
    configPagSeguro.clear()


if usa_app == 2:
    desenvApp.clear()
    validaPagSeguro.clear()
    gatewaysApp.clear()
    qrCApp.clear()


if usa_importacao_produtos == 1:
    importacaoNossaBase.clear()
elif usa_importacao_produtos == 2:
    importacaoDeles.clear()
    executImportacaoDeles.clear()
elif usa_importacao_produtos == 3:
    importacaoDeles.clear()
    executImportacaoDeles.clear()
    importacaoNossaBase.clear()
    if usa_PinPad == 2:
        compraPinPad.clear()
    if usa_Leitor == 2:
        compraLeitor.clear()

if usa_tef == 2:
    infosTef.clear()

if usa_trava == 2:
    trava.clear()












cronogramaFinal = [obrigatorio, compraM10, compraPagSeguro, compra_Outro_Totem, compraLeitor, compraPinPad, desenvApp, importacaoDeles, acessoServidor, infosTef, certificadoDigital, validaPagSeguro, installServidor, executImportacaoDeles, importacaoNossaBase, configPagSeguro, configM10, config_Outro_Totem, gatewaysApp, trava, denis, qrCApp, ultimo]

print(f"Passo a passo para implantação da loja {nome_loja} - {localidade}:\n")

step_count = 1
for step_list in cronogramaFinal:
    for step in step_list:
        print(f"{step_count}. {step}")
        step_count += 1
