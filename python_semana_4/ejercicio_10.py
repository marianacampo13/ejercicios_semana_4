frase = "Hola gente"
contador = 0

for letra in frase.lower():
    if letra in "aeiou":
        contador = contador + 1

print("Cantidad de vocales:", contador)
