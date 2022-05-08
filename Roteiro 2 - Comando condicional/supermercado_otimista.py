dia_da_semana = str(input())
preco = float(input())
opcao = str(input())
nome = str(input())

if dia_da_semana == "seg" or dia_da_semana == "ter" or dia_da_semana == "qua":
    if opcao == "ouro":
        print ("O preco do produto "+(str(nome))+ " no dia "+(str(dia_da_semana))+" eh "+(str(preco/2)))
    else:
        print (("O preco do produto "+(str(nome))+ " no dia "+(str(dia_da_semana))+" eh "+(str(preco))))
if dia_da_semana == "qui" or dia_da_semana == "sex":
    if 10 <= preco <= 100 and opcao == "ouro" or opcao == "prata":
        print ((("O preco do produto "+(str(nome))+ " no dia "+(str(dia_da_semana))+" eh {:.2f}".format((preco*(1/3))))))
    else:
        print (("O preco do produto "+(str(nome))+ " no dia "+(str(dia_da_semana))+" eh "+(str(preco))))
if dia_da_semana == "sab":
    if opcao == "prata":
        print (("O preco do produto "+(str(nome))+ " no dia "+(str(dia_da_semana))+" eh "+(str(preco*3))))
