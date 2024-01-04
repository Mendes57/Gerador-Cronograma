from static.itensCronograma.contrato import contrato
from static.itensCronograma.desenvolvimento import desenvolvimento
from static.itensCronograma.sitef import sitef
from static.itensCronograma.totemM10 import totemM10
from static.itensCronograma.totemPagSeguro import totemPagSeguro
from static.itensCronograma.trava import trava
from static.itensCronograma.erp import erp
from static.itensCronograma.app import app
from static.itensCronograma.finalizacao import finalizacao
from static.itensCronograma.linksM10 import linksm10
from static.itensCronograma.linksPagseguro import linkspagseguro
from static.itensCronograma.linksTrava import linkstrava
from static.itensCronograma.dadosSitef import dadossitef
from static.itensCronograma.outroTotem import outroTotem
from static.itensCronograma.linksOutroTotem import linksOutroTotem


def geraCrono(dadosCliente):
    contrato_mut = contrato()
    desenvolvimento_mut = desenvolvimento()
    sitef_mut = sitef()
    m10_mut = totemM10()
    pagseguro_mut = totemPagSeguro()
    trava_mut = trava()
    erp_mut = erp()
    app_mut = app()
    finalizacao_mut = finalizacao()
    linksm10_mut = linksm10()
    linkspagseguro_mut = linkspagseguro()
    linkstrava_mut = linkstrava()
    dadossitef_mut = dadossitef()
    outroTotem_mut = outroTotem()
    linksOutroTotem_mut = linksOutroTotem()

    if dadosCliente[1] == 1: pagseguro_mut.clear(); linkspagseguro_mut.clear(); outroTotem_mut.clear(); linksOutroTotem_mut.clear()
    elif dadosCliente[1] == 2: sitef_mut.clear(); dadossitef_mut.clear(); m10_mut.clear(); linksm10_mut.clear(); outroTotem_mut.clear(); linksOutroTotem_mut.clear()
    elif dadosCliente[1] == 3: del pagseguro_mut[1][0]; del linkspagseguro_mut[1][2]; pagseguro_mut[0][0] = pagseguro_mut[0][0].replace(" e Servidor", ""); del m10_mut[1][0]; del linksm10_mut[1][2]; m10_mut[0][0] = m10_mut[0][0].replace(" e Servidor", ""); outroTotem_mut.clear(); linksOutroTotem_mut.clear()
    elif dadosCliente[1] == 4: pagseguro_mut.clear(); linkspagseguro_mut.clear(); m10_mut.clear(); linksm10_mut.clear()
    elif dadosCliente[1] == 5: 
        if dadosCliente[2] == 1: m10_mut.clear(); linksm10_mut.clear(); del outroTotem_mut[1][0]; del linksOutroTotem_mut[1][0]; outroTotem_mut[0][0] = outroTotem_mut[0][0].replace(" e Servidor", "")
        elif dadosCliente[2] == 2: pagseguro_mut.clear(); linkspagseguro_mut.clear(); del outroTotem_mut[1][0]; del linksOutroTotem_mut[1][0]; outroTotem_mut[0][0] = outroTotem_mut[0][0].replace(" e Servidor", "")
    elif dadosCliente[1] == 6: del outroTotem_mut[1][0]; del linksOutroTotem_mut[1][0]; outroTotem_mut[0][0] = outroTotem_mut[0][0].replace(" e Servidor", ""); pagseguro_mut[0][0] = pagseguro_mut[0][0].replace(" e Servidor", "");del pagseguro_mut[1][0]; del linkspagseguro_mut[1][2]

    
    if dadosCliente[3] == 1: pass
    elif dadosCliente[3] == 2: app_mut.clear(); del finalizacao_mut[1][2]

    if dadosCliente[4] == 1: 
        if dadosCliente[4] == 2: del app_mut[1][0:2]
    elif dadosCliente[4] == 2: app_mut.clear(); del finalizacao_mut[1][2]
    
    if dadosCliente[5] == 1: pass
    elif dadosCliente[5] == 2: del desenvolvimento_mut[1][2:4]
    elif dadosCliente[5] == 3: del erp_mut[1][5]; del desenvolvimento_mut[1][2:4]
    
    if dadosCliente[6] == 1: pass
    elif dadosCliente[6] == 2: trava_mut.clear(); linkstrava_mut.clear()

    return [contrato_mut, desenvolvimento_mut, sitef_mut, m10_mut, pagseguro_mut, outroTotem_mut, trava_mut, erp_mut, app_mut, finalizacao_mut, linksm10_mut, linkspagseguro_mut, linksOutroTotem_mut, linkstrava_mut, dadossitef_mut]
