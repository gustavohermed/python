num = int(input("Dime un número entero positivo: "))

for inicio in range(1, num + 1,2):
    for x in range(inicio, 0, -2):
        print(x, end=" ")
    print()
