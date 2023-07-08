casos = int(input())
dentro = fora = 0

for v in range(casos):
    x = int(input())
    if 10 <= x <= 20:
        dentro += 1
        continue
    else:
        fora += 1
print(f'{dentro} in')
print(f'{fora} out')