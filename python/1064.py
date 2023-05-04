quantidadePositivos = 0
somaPares = 0
for c in range(6):
    c = float(input())
    if c >= 0:
        somaPares += c
        quantidadePositivos += 1

media = somaPares / quantidadePositivos
print(f'{quantidadePositivos} valores positivos')
print(f'{media:.1f}')
