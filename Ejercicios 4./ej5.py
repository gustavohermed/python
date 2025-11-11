cantidad = float(input("Indica la cantidad a invertir: "))
interes = float(input("Dime el interes anual: "))
años = int(input("Dime el numero de años: "))

años = años +1

for x in range(1, años):
    print(cantidad+(cantidad*(interes/100)*x))

