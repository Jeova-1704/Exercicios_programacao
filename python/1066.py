par, impar, positivo, negativo = [0, 0, 0, 0]
for c in range(5):
    c = int(input())
    if c % 2 == 0:
        par += 1
    if c > 0 :
        positivo += 1
    if c % 2 != 0:
        impar += 1
    if c < 0:
        negativo += 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
