inversion= int(input("Cantidad que quieres invertir: "))
interesanual= int(input("Interes anual: "))
naños= int(input("Número de años: "))
capital= inversion * (1+interesanual/100) ** naños

print(f"El capital obtenido es: {capital:.2f} €")