#FEITO, EXPLICADO


caixaspequenas = 0                             #vamos iniciar a contagem de caixas pequenas;
caixasgrandes = 0                             #vamos iniciar a contagem de caixas grandes;

for cont in range(7):                            #vamos limitar o numero de professores que irão fazer a doação para 7 por isso o range 7;
    quantos = int(input())                        #quantas CAIXAS serao doadas por cada professor; APENAS NUMERO INTEIRO
    tamanho = str(input()).lower()                 #qual tamanho da CAIXA que esta sendo doada;
    if tamanho == 'p':                             #se for CAIXA PEQUENA, vamos colocar no contador de CAIXAS PEQUENAS;
        caixaspequenas+=quantos                   #contador de QUANTOS vai para as CAIXAS PEQUENAS;
    else:                                        #se for outra so temos a CAIXA GRANDE, vamos colocar no contador;
        caixasgrandes+=quantos                   #contador de QUANTOS vai para as CAIXAS GRANDES;
capsulas = (caixaspequenas*10)+(caixasgrandes*16)  #NUMERO DE CAPSULAS VEZES O CONTATOR QUE EU OBTI;
print('{}'.format(capsulas))                           #NUMERO DE CAPSULAS TOTAIS
print('{:.0f}'.format((capsulas*2)/7))                 #QUANTAS XICARAS PARA OS 7 PROFESSORES.
