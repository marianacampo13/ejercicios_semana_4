numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
