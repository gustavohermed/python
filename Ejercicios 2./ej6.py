frase= input("Dime una frase: ")
vocal= input("Dime una vocal: ")

vocal_modificada= vocal.upper()
frase_modificada= frase.replace(vocal, vocal_modificada)

print ("Esta es la frase con la vocal en mayuscula: ", frase_modificada)