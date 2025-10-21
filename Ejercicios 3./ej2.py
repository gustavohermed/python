contraseña= "admin"
contraseñauser= input("Introduce una contraseña: ")

if contraseñauser.lower() == contraseña.lower():
    print ("Tu contraseña es correcta")
else:
    print ("Contraseña incorrecta")