pares = impares = positivos = negativos = 0
for _ in range(5):
    x = int(input())
    if x % 2 == 0:
        pares += 1
    elif x % 2 != 0:
        impares += 1
    if x > 0:
        positivos += 1
    elif x < 0:
        negativos += 1
print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')