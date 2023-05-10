N = []
for c in range(20):
    valor = int(input())
    N.append(valor)

for i in range(10):
    j = 19 - i
    N[i], N[j] = N[j], N[i]

for i in range(20):
    print(f'N[{i}] = {N[i]}')

