abecedario = list("abcdefghijklmnopqrstuvwxyz")

resultado = []

for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:
        resultado.append(abecedario[i])

print(resultado)
