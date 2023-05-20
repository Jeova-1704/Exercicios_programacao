quantidadePares = 0
for c in range(5):
    c = float(input())
    if c % 2 == 0:
        quantidadePares += 1

print(f'{quantidadePares} valores pares')