facturas = {}

cobrado = 0

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Añadir una factura")
    print("2. Pagar una factura")
    print("3. Terminar")

    opcion = input("Elige una opción (1/2/3): ")

    if opcion == "1":
        numero = input("Introduce el número de la factura: ")
        coste = float(input("Introduce el coste de la factura: "))
        facturas[numero] = coste

    elif opcion == "2":
        numero = input("Introduce el número de la factura a pagar: ")

        if numero in facturas:
            cobrado += facturas[numero]
            del facturas[numero]
        else:
            print("La factura no existe")

    elif opcion == "3":
        break

    else:
        print("Opción no válida")

    pendiente = sum(facturas.values())

    print(f"Cantidad cobrada hasta el momento: {cobrado}")
    print(f"Cantidad pendiente de cobro: {pendiente}")
