asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

notas = []

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    notas.append(nota)

for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
