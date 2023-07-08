salario = float(input())
if salario <= 2000:
    print('Isento')

else:
    if 2000 < salario <= 3000:
        imposto = (salario - 2000) * 0.08

    elif 3000 < salario <= 4500:
        imposto = 1000 * 0.08 + (salario - 3000) * 0.18
        
    else:
        imposto = 1000 * 0.08 + 1500 * 0.18 + (salario - 4500) * 0.28

    print(f'R$ {imposto:.2f}')
