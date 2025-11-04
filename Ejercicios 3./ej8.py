puntuacion = float(input("Introduce tu puntuación (0.0, 0.4, 0.6 o más): "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = None

if nivel:
    dinero = 2400 * puntuacion
    print(f"Tu nivel de rendimiento es: {nivel}")
    print(f"Has obtenido {dinero:.2f}€ de beneficio.")
else:
    print("Puntuación no válida. Debe ser 0.0, 0.4 o 0.6 o más.")
