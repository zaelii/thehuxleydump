idade = int(input())
jogo = input()

## azar: mais de 21 anos
##mmorpg: mais de 14 anos
## moba: mais de 10 anos
## casual: livre
## "Pode entrar!"
## "Volte daqui há alguns anos."


if 0 <= idade < 10:
    if jogo == 'casual':
        print("Pode entrar!")
    elif jogo == 'moba' or jogo == 'mmorpg' or jogo == 'azar':
        print("Volte daqui há alguns anos.")
    else:
        print("Jogo invalido.")
if 10 <= idade < 14:
    if jogo == 'casual' or jogo == 'moba':
        print("Pode entrar!")
    elif jogo == 'mmorpg' or jogo == 'azar':
        print("Volte daqui há alguns anos.")
    else:
        print("Jogo invalido.")
if 14 <= idade < 21:
    if jogo == 'casual' or jogo == 'moba' or jogo == 'mmorpg':
        print("Pode entrar!")
    elif jogo == 'azar':
        print("Volte daqui há alguns anos.")
    else:
        print("Jogo invalido.")
if 21 <= idade <= 130:
    if jogo == 'azar' or jogo == 'casual' or jogo == 'moba' or jogo == 'mmorpg':
        print("Pode entrar!")
    else:
        print("Jogo invalido.")
if idade < 0:
    print('Idade invalida.')
if idade > 130:
    print('Idade invalida.')

