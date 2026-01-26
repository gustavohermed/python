datos = """nif;nombre;email;teléfono;descuento
01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5
71476342J;Macarena Ramírez;macarena@mail.com;692839321;8
63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2
98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

lineas = datos.split("\n")

campos = lineas[0].split(";")

clientes = {}

for linea in lineas[1:]:
    valores = linea.split(";")
    nif = valores[0]

    clientes[nif] = {
        "nombre": valores[1],
        "email": valores[2],
        "teléfono": valores[3],
        "descuento": float(valores[4])
    }

print(clientes)
