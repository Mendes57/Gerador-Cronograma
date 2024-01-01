from static.itensCronograma.inicioCrono import inicioCrono

def printaCrono(itens):
    
    print (inicioCrono())

    if itens[0:4] == "Erro":
        print (itens)
        return
    
    for i in itens:
        if i != []:
            print (f"\n\n{i[0][0]}\n")

            for j in i[1]:
                print (f"{j}")