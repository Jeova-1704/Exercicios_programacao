salario = float(input())

if salario <= 400:
    novo_salario = salario + (salario * (15/100))
    rajuste = novo_salario - salario
    percentual = 15

elif 400 < salario <= 800:
    novo_salario = salario + (salario * (12/100))
    rajuste = novo_salario - salario
    percentual = 12

elif 800 < salario <= 1200:
    novo_salario = salario + (salario * (10/100))
    rajuste = novo_salario - salario
    percentual = 10

elif 1200 < salario <= 2000:
    novo_salario = salario + (salario * (7/100))
    rajuste = novo_salario - salario
    percentual = 7

elif salario > 2000:
    novo_salario = salario + (salario * (4/100))
    rajuste = novo_salario - salario
    percentual = 4

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {rajuste:.2f}')
print(f'Em percentual: {percentual} %')
