clientes = {}

while True:
    print("\nMENÚ")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

    opcion = input("Elige una opción (1-6): ")

    if opcion == "1":
        nif = input("Introduce el NIF: ")
        nombre = input("Introduce el nombre: ")
        direccion = input("Introduce la dirección: ")
        telefono = input("Introduce el teléfono: ")
        correo = input("Introduce el correo electrónico: ")
        preferente = input("¿Es cliente preferente? (s/n): ").lower() == "s"

        clientes[nif] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": preferente
        }

    elif opcion == "2":
        nif = input("Introduce el NIF del cliente a eliminar: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("El cliente no existe")

    elif opcion == "3":
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            print(clientes[nif])
        else:
            print("El cliente no existe")

    elif opcion == "4":
        for nif, datos in clientes.items():
            print(nif, datos["nombre"])

    elif opcion == "5":
        for nif, datos in clientes.items():
            if datos["preferente"]:
                print(nif, datos["nombre"])

    elif opcion == "6":
        break

    else:
        print("Opción no válida")
