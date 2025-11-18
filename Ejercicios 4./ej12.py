frase = input("Dime una frase: ")
letra = input("Dime una letra: ")

contador = 0

for x in frase:
    if x == letra:
        contador += 1
print (f"La letra {letra} aparece {contador} veces en la frase")
