t = float(input())
secrecao = input()

if t >= 37 and secrecao == "S":
    print ("Exames Especiais")
    
elif t < 37 and secrecao == "S":
    print ("Exames Basicos")

elif t > 37 and secrecao == "N":
    print ("Exames Basicos")

elif t < 37 and secrecao == "N":
    print("Liberado")
else:
    print("Erro")





