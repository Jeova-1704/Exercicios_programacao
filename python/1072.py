n = int(input())
dentro, fora = [0,0]
for qv in range(n):
    valor = int(input())
    if 10 <= valor <= 20:
        dentro += 1
        continue
    fora += 1

print(f'{dentro} in')
print(f'{fora} out')

