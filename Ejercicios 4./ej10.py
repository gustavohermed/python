num = int(input("Introduce un número entero: "))

if num < 2:
    print("No es primo.")
else:
    primo = True

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print("Es primo.")
    else:
        print("No es primo.")
