def checaErros(variavel):
    if variavel == "":
        print(f"\nErro ao inserir dados, por favor, tente novamente\nErro: {variavel}\n\n")
        exit()
    else:
        return variavel