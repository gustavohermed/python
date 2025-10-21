nombre = input("Dime tu nombre: ")
sexo = input("Dime tu sexo: ")

if (sexo == "mujer" and nombre[0].upper() < "M") or (sexo == "hombre" and nombre[0].upper() > "N"):
    print("Perteneces al grupo A.")
else:
    print("Perteneces al grupo B.")