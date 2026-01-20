divisas = {
    "Euro": "€",
    "Dollar": "$",
    "Yen": "¥"
}

divisa = input("Introduce una divisa: ")

if divisa in divisas:
    print(f"El símbolo del {divisa} es {divisas[divisa]}")
else:
    print("La divisa no está en el diccionario")
