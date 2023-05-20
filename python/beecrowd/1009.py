nome = str(input())
salarioFixo = float(input())
vendas = float(input())

salarioLiquido = salarioFixo + (vendas * 0.15)

print("TOTAL = R$ {:.2f}".format(salarioLiquido))
