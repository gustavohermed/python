creditos = {
    "Matemáticas": 6,
    "Física": 4,
    "Química": 5
}

total_creditos = 0

for asignatura, credito in creditos.items():
    print(f"{asignatura} tiene {credito} créditos")
    total_creditos += credito

print(f"El número total de créditos del curso es {total_creditos}")
