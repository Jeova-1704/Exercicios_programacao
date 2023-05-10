n = int(input())
lista = []
lista.append(n)
valor = n
for c in range(19):
    valor *= 2
    lista.append(valor)

for i, v in enumerate(lista):
    print(f'N[{i}] = {v}')