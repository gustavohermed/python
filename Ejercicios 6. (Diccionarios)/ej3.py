precios = {
    "plátano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}

fruta = input("Introduce una fruta: ").lower()
kilos = float(input("Introduce el número de kilos: "))

if fruta in precios:
    precio_total = precios[fruta] * kilos
    print(f"El precio de {kilos} kg de {fruta} es {precio_total} €")
else:
    print("La fruta no está en el diccionario")
