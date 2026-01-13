asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

suspensas = []

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    
    if nota < 5:
        suspensas.append(asignatura)

print("Tienes que repetir las siguientes asignaturas:")
for asignatura in suspensas:
    print(asignatura)
