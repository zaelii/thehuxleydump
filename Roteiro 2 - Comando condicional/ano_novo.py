dia1 = int(input())
CO1, RE1, DE1 = map(float, input().split())
dia2 = int(input())
CO2, RE2, CE2, DE2 = map(float, input().split())

# NATAL
if 0 < dia1 <= 19:
    CO1 *= 1 - 0
    RE1 *= 1 - 0.10
    DE1 *= 1 - 0.15
elif dia1 == 20:           
    CO1 *= 1 - 0.12      
    RE1 *= 1 - 0.15   
    DE1 *= 1 - 0.20   
elif dia1 == 21:
    CO1 *= 1 - 0.17
    RE1 *= 1 - 0.22
    DE1 *= 1 - 0.27
elif dia1 == 22:
    CO1 *= 1 - 0.20
    RE1 *= 1 - 0.22
    DE1 *= 1 - 0.30
elif dia1 == 23:
    CO1 *= 1 - 0.25
    RE1 *= 1 - 0.29
    DE1 *= 1 - 0.35
elif dia1 == 24:
    CO1 *= 1 - 0.35
    RE1 *= 1 - 0.35
    DE1 *= 1 - 0.50
else:
    CO1 *= 1
    RE1 *= 1
    DE1 *= 1

# ANO NOVO
if 0 < dia2 < 20:
    CO2 *= 1 - 0
    RE2 *= 1 - 0.10
    CE2 *= 1 - 0
    DE2 *= 1 - 0.15
elif dia2 == 20:
    CO2 *= 1 - 0.12
    RE2 *= 1 - 0.15
    CE2 *= 1 - 0
    DE2 *= 1 - 0.2
elif dia2 == 21:
    CO2 *= 1 - 0.17
    RE2 *= 1 - 0.22
    CE2 *= 1 - 0
    DE2 *= 1 - 0.27
elif dia2 == 22:
    CO2 *= 1 - 0.20
    RE2 *= 1 - 0.22
    CE2 *= 1 - 0
    DE2 *= 1 - 0.30
elif dia2 == 23:
    CO2 *= 1 - 0.25
    RE2 *= 1 - 0.29
    CE2 *= 1 - 0
    DE2 *= 1 - 0.35
elif dia2 == 24:
    CO2 *= 1 - 0.35
    RE2 *= 1 - 0.35
    CE2 *= 1 - 0
    DE2 *= 1 - 0.5
elif dia2 == 25:
    CO2 *= 1 - 0.15
    RE2 *= 1 - 0.13
    CE2 *= 1 - 0
    DE2 *= 1 - 0.1
elif dia2 == 26:
    CO2 *= 1 - 0.19
    RE2 *= 1 - 0.25
    CE2 *= 1 - 0.05
    DE2 *= 1 - 0.23
elif dia2 == 27:
    CO2 *= 1 - 0.24
    RE2 *= 1 - 0.3
    CE2 *= 1 - 0.12
    DE2 *= 1 - 0.33
elif dia2 == 28:
    CO2 *= 1 - 0.3
    RE2 *= 1 - 0.32
    CE2 *= 1 - 0.2
    DE2 *= 1 - 0.35
elif dia2 == 29 or dia2 == 30:
    CO2 *= 1 - 0.35
    RE2 *= 1 - 0.4
    CE2 *= 1 - 0.33
    DE2 *= 1 - 0.42
elif dia2 == 31:
    CO2 *= 1 - 0.4
    RE2 *= 1 - 0.47
    CE2 *= 1 - 0.45
    DE2 *= 1 - 0.66
else:
    CO2 *= 1
    RE2 *= 1
    CE2 *= 1
    DE2 *= 1

print("Compras de natal: R$ {:.2f}.".format(CO1+RE1+DE1))
print("Compras de ano novo: R$ {:.2f}.".format(CO2+RE2+CE2+DE2))
print("Total das compras: R$ {:.2f}.".format(CO1+RE1+DE1+CO2+RE2+CE2+DE2))
