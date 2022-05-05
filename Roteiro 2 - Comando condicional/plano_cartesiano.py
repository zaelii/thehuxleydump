x = int(input())
y = int(input())

if x == 0 and y == 0:
    print ("Sobre a origem")
elif x == 0 and y > 0:
    print ('Sobre o eixo y')
elif x == 0 and y < 0:
    print ('Sobre o eixo y')
elif x > 0 and y == 0:
    print ('Sobre o eixo x')
elif x < 0 and y == 0:
    print ('Sobre o eixo x')
if x > 0: #POSITIVO
    if y > 0: #POSITIVO
        print("Primeiro Quadrante")
if x < 0: #NEGATIVO
    if y > 0: #POSITIVO
        print("Segundo Quadrante")
if x > 0: #POSITIVO
    if y < 0: #NEGATIVO
        print("Quarto Quadrante")
if x < 0: #NEGATIVO
    if y <0: #NEGATIVO
        print("Terceiro Quadrante")
