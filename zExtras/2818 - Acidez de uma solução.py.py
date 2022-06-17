print("Digite o pH da solucao:")
valor = float(input())

if 0 <= valor <= 14:
    if valor == 7:
        print("Solucao neutra")
    elif valor < 7:
        print("Solucao acida")
    else:
        print("Solucao basica")
else:
    print("Valor do pH deve estar entre 0 e 14")

