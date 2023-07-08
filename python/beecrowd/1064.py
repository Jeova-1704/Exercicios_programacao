qtd_positivos = soma__positivos = 0
for _ in range(6):
    x = float(input())
    if x > 0:
        qtd_positivos += 1
        soma__positivos += x

media = soma__positivos / qtd_positivos
print(f'{qtd_positivos} valores positivos')
print(f'{media:.1f}')

