from static.funcoes.coletaDadosEChecaErros import dadosCliente

def erp():
    return [["*ERP:*"],
            [f"Solicitação do IP Fixo (de preferencia na internet que o pc que iremos instalar o sistema mais utiliza), favor verificar com operadora de internet - *{dadosCliente[0]}* - ",
            f"Configuração de emissão de Notas, opção de: Não emitir, Somente vendas com CPF, Emitir todas - *{dadosCliente[0]}* - ",
            f"Possuir certificado Digital para NFCe, código CSC e IDCSC do certificado (Favor deixar certificado digital já na máquina que iremos instalar o sistema e envair senha e códigos no grupo) - *{dadosCliente[0]}* - ",
            f"Para configuração de portas na rede, enviar login e senha ou foto do adesivo normalmente encontrado na parte de trás do roteador - *{dadosCliente[0]}* - ",
            f"Acesso remoto (AnyDesk/TeamViewer) - ACCESYS e *{dadosCliente[0]}* - ",
            f"Configuração do SERVIDOR - ACCESYS e *{dadosCliente[0]}* - ",
            f"Importação da tabela de produtos - ACCESYS - ",
            f"Configuração e liberação de portas no roteador - ACCESYS - "]
            ]