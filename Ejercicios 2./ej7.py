correo = input("Dime tu correo electrónico: ")

usuario= correo.split("@")[0]

nuevo_correo = usuario + "@ceu.es"

print (f"Tu correo nuevo es: ", nuevo_correo)