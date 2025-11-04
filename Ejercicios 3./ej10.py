tipo = input("¿Pizza vegetariana? (sí/no): ").lower()

if tipo == "sí":
    print("Ingredientes: pimiento, tofu")
    ingrediente = input("Elige uno: ")
    pizza = "vegetariana"
elif tipo == "no":
    print("Ingredientes: peperoni, jamón, salmón")
    ingrediente = input("Elige uno: ")
    pizza = "no vegetariana"
else:
    print("Opción no válida.")
    exit()

print(f"\nTu pizza es {pizza} y lleva mozzarella, tomate y {ingrediente}.")

