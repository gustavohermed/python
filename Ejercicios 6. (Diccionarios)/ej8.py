entrada = input("Introduce las traducciones (español:inglés, separadas por comas): ")

diccionario = {}

pares = entrada.split(",")

for par in pares:
    esp, eng = par.split(":")
    diccionario[esp] = eng

frase = input("Introduce una frase en español: ")

palabras = frase.split()
traduccion = []

for palabra in palabras:
    if palabra in diccionario:
        traduccion.append(diccionario[palabra])
    else:
        traduccion.append(palabra)

print("Traducción:")
print(" ".join(traduccion))
