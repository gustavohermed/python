compra = input("Dime los productos de tu compra separados por comas: ")

lista_compra = compra.split(",") 

print ("Los producto de tu compra son: ")
for compra in lista_compra:
    print(compra.split())
