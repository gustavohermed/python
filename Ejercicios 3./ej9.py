edad = float(input("Dime tu edad: "))

if edad < 4: 
    print ("Entrada gratis")
elif edad >=4 and edad <=18:
    print ("Tienes que pagar 5€ de entrada")
else:
    print ("Tienes que pagar 10€ de entrada")