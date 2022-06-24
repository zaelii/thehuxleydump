aprovados = 0

while True:
    p = int(input())  #50questoes
    if p < 0:
        break
    m = int(input())  #35questoes
    if m < 0:
        break
    r = float(input())  #nota da redação
    if r < 0:
        break
    else:
        if p >= 40 and m >= 21 and r >= 7.0:
            aprovados += 1
print(aprovados)