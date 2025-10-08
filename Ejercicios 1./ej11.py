cuenta_ahorros= float(input("Dinero en la cuenta de ahorros:"))

interes= 0.04

año1 = cuenta_ahorros * (1 + interes)
año2 = año1 * (1 + interes)
año3 = año2 * (1 + interes)

print(f"Saldo tras el primer año: {round(año1, 2)} €")
print(f"Saldo tras el segundo año: {round(año2, 2)} €")
print(f"Saldo tras el tercer año: {round(año3, 2)} €")