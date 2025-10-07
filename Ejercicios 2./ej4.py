telefono = input("Pon tu número de telefono con prefijo y extensión (ejemplo: +34-958976543-56): ")

partes = telefono.split("-")
numero_normal = partes[1]

print("Número sin prefijo ni extensión:", numero_normal)
