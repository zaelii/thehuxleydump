DIFERENCA_IDADE = 16
idade_adotante = int(input())
if idade_adotante < 18:
    print("Não pode adotar")
else:
    se_e_familia = input()
    adocao_conjunta = input()
    adotantes_casados = input()
    idade_adotando = input()
    paisdesconhecidos = input()
    consetimento_dos_pais = input()
    consetimento_do_adotando_12 = input()
    if se_e_familia == "S":
        print("Não pode adotar")
    elif idade_adotante < (int(idade_adotando) + 16):
        print("Não pode adotar")
    elif adocao_conjunta == "S" and adotantes_casados != "S":
        print("Não pode adotar")
    elif (int(idade_adotando) > 12 or idade_adotando == 10) and consetimento_do_adotando_12 == "N":
        print("Não pode adotar")
    elif paisdesconhecidos == "N" and consetimento_dos_pais == "N":
        print("Não pode adotar")
    elif idade_adotante > (int(idade_adotando) + 16):
        print("Pode adotar")
    elif idade_adotando >= 12 and consetimento_do_adotando_12 == "S":
        print("Pode adotar")
    elif paisdesconhecidos == "N" and consetimento_dos_pais == "S":
        print("Pode adotar")
    elif paisdesconhecidos == "S" and consetimento_dos_pais == "S":
        print("Pode adotar")
    elif paisdesconhecidos == "S" and consetimento_dos_pais == "N":
        print("Pode adotar")
    else:
        print("Não pode adotar")
