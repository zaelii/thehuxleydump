ano = int(input())            # ano inicial
interv = int(input())         # intervalo ou periodo de tempo para a proxima vacina
cont = ano + interv           # fazer a soma do inicio com o periodo do proximo

for vacina in range(3):       #apenas 3 anos seguintes
    print (cont,end=" ")      # print final com o ano e os adiantes com o codigo debaixo
    cont+=interv              # contar 3 vezes em diante

