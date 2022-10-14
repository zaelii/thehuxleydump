

valor_alvo = float(input())
numero_de_contribuintes = int(input())
if numero_de_contribuintes <= 0:
    print("Nao ha conta ou funcionario suficiente para pagar a conta")
else:
    acumulador = 0
    pessoas = []
    valores = []
    for i in range(numero_de_contribuintes):
        nome = input()
        pessoas.append(nome)
        valor = float(input())
        valores.append(valor)
        acumulador += valor

    meta = valor_alvo - acumulador
    maior_valor_pago = max(valores)
    posicao_maior_valor = valores.index(max(valores))
    pos = pessoas[posicao_maior_valor]


    if meta <= 0:
        print(pos,"pagou R$",maior_valor_pago)
        print("Valor excedente: sobra R$",(meta*-1))
    else:
        print(pos,"pagou R$",maior_valor_pago)
        print("Valor insuficiente: falta R$",(meta))
