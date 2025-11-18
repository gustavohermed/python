contraseña = "contraseña"

for intentos in range(5):
    pregunta = input("Dime una contraseña: ")

    if pregunta == contraseña:
        print ("Has acertado la contraseña")
        exit()
    else:
        print ("Contraseña incorrecta, inténtalo de nuevo")


