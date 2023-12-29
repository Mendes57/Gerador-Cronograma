from static.itensCronograma.contrato import contrato
from static.itensCronograma.desenvolvimento import desenvolvimento
from static.itensCronograma.sitef import sitef
from static.itensCronograma.m10 import m10
from static.itensCronograma.pagseguro import pagseguro
from static.itensCronograma.trava import trava
from static.itensCronograma.erp import erp
from static.itensCronograma.app import app
from static.itensCronograma.finalizacao import finalizacao
from static.itensCronograma.linksm10 import linksm10
from static.itensCronograma.linkspagseguro import linkspagseguro
from static.itensCronograma.linkstrava import linkstrava
from static.itensCronograma.dadossitef import dadossitef


ordem = []

def geraCrono(dadosCliente):
    contrato_mut = contrato()
    desenvolvimento_mut = desenvolvimento()
    sitef_mut = sitef()
    m10_mut = m10()
    pagseguro_mut = pagseguro()
    trava_mut = trava()
    erp_mut = erp()
    app_mut = app()
    finalizacao_mut = finalizacao()
    linksm10_mut = linksm10()
    linkspagseguro_mut = linkspagseguro()
    linkstrava_mut = linkstrava()
    dadossitef_mut = dadossitef()

    if dadosCliente[1] == 1: pagseguro_mut.clear(); linkspagseguro_mut.clear()
    elif dadosCliente[1] == 2: sitef_mut.clear(); dadossitef_mut.clear(); m10_mut.clear(); linksm10_mut.clear()
    elif dadosCliente[1] == 3: del pagseguro_mut[1][0]; del linkspagseguro_mut[1][2]; pagseguro_mut[0][0] = pagseguro_mut[0][0].replace(" e Servidor", "")
    else: return "Erro nos dados do totem"
    
    if dadosCliente[2] == 1: pass
    elif dadosCliente[2] == 2: app_mut.clear(); del finalizacao_mut[1][2]
    else: return "Erro nos dados do app"

    if dadosCliente[3] == 1: pass
    elif dadosCliente[3] == 2: del app_mut[1][0:2]
    else: return "Erro nos dados da venda pelo app"
    
    if dadosCliente[4] == 1: pass
    elif dadosCliente[4] == 2: del desenvolvimento_mut[1][2:4]
    elif dadosCliente[4] == 3: del erp_mut[1][5]; del desenvolvimento_mut[1][2:4]
    else: return "Erro nos dados da importação"
    
    if dadosCliente[5] == 1: pass
    elif dadosCliente[5] == 2: trava_mut.clear(); linkstrava_mut.clear()
    else: return "Erro nos dados da trava"

    ordem.extend([contrato_mut, desenvolvimento_mut, sitef_mut, m10_mut, pagseguro_mut, trava_mut, erp_mut, app_mut, finalizacao_mut, linksm10_mut, linkspagseguro_mut, linkstrava_mut, dadossitef_mut])
    return ordem