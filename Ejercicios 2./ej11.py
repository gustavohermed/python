nombre = input("Nombre del producto: ")
precio = float(input("Precio unitario (en euros): "))
unidades = int(input("Número de unidades: "))

coste_total = precio * unidades

print(f"{nombre} {precio:06.2f} {unidades:03d} {coste_total:08.2f}")
