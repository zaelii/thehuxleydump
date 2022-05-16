#feito

contadorB = 0
contadorC = 0
for i in range(7):
     passeio = input().upper()
     if passeio == "BOLICHE":
         contadorB += 1 
     elif passeio == "CINEMA":
         contadorC += 1
if contadorC > contadorB:
     print("CINEMA")
else:
     print("BOLICHE")
         
