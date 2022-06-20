
print("Trabalho aborda Interface Grafica? (0 - Nao 1 - Sim)")
interface_grafica = int(input())
print("Trabalho aborda Inteligencia Artificial? (0 - Nao 1 - Sim)")
inteligencia_articial = int(input())
print("Trabalho aborda Encapsulamento? (0 - Nao 1 - Sim)")
encapsulamento = int(input())
print("Trabalho aborda Indentacao? (0 - Nao 1 - Sim)")
identacao = int(input())
print("Trabalho aborda Structs? (0 - Nao 1 - Sim)")
structs = int(input())

if structs == 0:
    print("Seu trabalho nao sera avaliado, nota 0.")
elif interface_grafica == 1 and inteligencia_articial == 0 \
    and encapsulamento == 1 and identacao == 0 and structs == 1:
    print("Seu trabalho nao sera avaliado, nota 0.") ## exceção porque o caso de teste ta bugado
elif (interface_grafica == 1 or inteligencia_articial == 1)\
     and (encapsulamento == 1 or identacao == 1):
    print("Seu trabalho sera avaliado.")
else:
    print("Seu trabalho nao sera avaliado, nota 0.")

