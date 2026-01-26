cesta = {}

while True:
    articulo = input("Introduce un artículo (o 'fin' para terminar): ")
    
    if articulo == "fin":
        break
    
    precio = float(input(f"Introduce el precio de {articulo}: "))
    cesta[articulo] = precio

print("\nLista de la compra")
total = 0

for articulo, precio in cesta.items():
    print(f"{articulo} {precio}")
    total += precio

print(f"Total {total}")
