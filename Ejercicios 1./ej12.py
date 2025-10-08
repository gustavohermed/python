barras_no_día= int(input("Cuántas barras que no son del día has vendido?"))

barra= 3.49
descuento= 0.06

precio_descuento= barra * (1 - descuento)
precio_total= barras_no_día * precio_descuento

print (f"El precio habitual de una barra de pan es: {barra}")
print (f"La barra al no ser fresca se le hace un descuento de: {descuento * 100}%")
print (f"El precio final de la barra que no es del dia es: {round(precio_total, 2)} €")
        