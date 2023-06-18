valor = int(input())

print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = []

for nota in notas:
    quantidade = valor // nota
    quantidades.append(quantidade)
    valor = valor % nota

for i in range(len(notas)):
    print(f'{quantidades[i]} nota(s) de R$ {notas[i]:.2f}'.replace('.', ','))
