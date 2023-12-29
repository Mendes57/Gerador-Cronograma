from static.itensCronograma.inicioCrono import inicioCrono

def printaCrono(itens):
    print (inicioCrono())
    for i in itens:
        if i != []:
            print (f"\n\n{i[0][0]}\n")

            for j in i[1]:
                print (f"{j}")