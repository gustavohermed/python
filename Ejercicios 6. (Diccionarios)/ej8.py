# Pedimos las traducciones al usuario
entrada = input("Introduce las traducciones (español:inglés, separadas por comas): ")

# Creamos el diccionario vacío
diccionario = {}

# Separamos cada par palabra:traducción
pares = entrada.split(",")

for par in pares:
    esp, eng = par.split(":")
    diccionario[esp] = eng

# Pedimos una frase en español
frase = input("Introduce una frase en español: ")

# Traducimos la frase
palabras = frase.split()
traduccion = []

for palabra in palabras:
    if palabra in diccionario:
        traduccion.append(diccionario[palabra])
    else:
        traduccion.append(palabra)

# Mostramos la frase traducida
print("Traducción:")
print(" ".join(traduccion))
