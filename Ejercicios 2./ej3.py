nombre = input("Introduce tu nombre: ")


nombre_sin_espacios = nombre.replace(" ", "")
print(f"{nombre.upper()} tiene {len(nombre_sin_espacios)} letras.")
