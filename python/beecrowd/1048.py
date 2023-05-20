salario = input()

salario = float(salario)

if 0 < salario <= 400.00:
    novoSalario = salario + (salario * (15/100))
    print(f'Novo salarario: {novoSalario:.2f}')
    print(f'Reajuste ganho {novoSalario - salario:.2f}')
    print('Em percentual: 15%')
    
elif 400.01 <= salario <= 800.00:
    novoSalario = salario + (salario * (12/100))    
    print(f'Novo salarario: {novoSalario:.2f}')
    print(f'Reajuste ganho {novoSalario - salario:.2f}')
    print('Em percentual: 12%')

elif 800.01 <= salario <= 1200.00:
    novoSalario = salario + (salario * (10/100))
    print(f'Novo salarario: {novoSalario:.2f}')
    print(f'Reajuste ganho {novoSalario - salario:.2f}')
    print('Em percentual: 10%')

elif 1200.01 <= salario <= 2000.00:
    novoSalario = salario + (salario * (7/100))    
    print(f'Novo salarario: {novoSalario:.2f}')
    print(f'Reajuste ganho {novoSalario - salario:.2f}')
    print('Em percentual: 7%')

else:
    novoSalario = salario + (salario * (4/100))    
    print(f'Novo salarario: {novoSalario:.2f}')
    print(f'Reajuste ganho {novoSalario - salario:.2f}')
    print('Em percentual: 4%')
