print("Digite o pH da solucao:")
n = int(input())


if n < 0 or n > 14:
    print("Valor deve estar entre 0 e 14.")
elif n == 7:
    print("Essa solucao e neutra.")
elif n > 7:
    print("Essa solucao e basica.")
else:
    print("Essa solucao e acida.")