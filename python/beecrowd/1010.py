codigo, qtd, valor = map(str,input().split())
codigo2, qtd2, valor2 = map(str,input().split())

codigo = int(codigo)
codigo2 = int(codigo2)
qtd = int(qtd)
qtd2 = int(qtd2)
valor = float(valor)
valor2 = float(valor2)

total = (valor * qtd) + (valor2 * qtd2)
print(f"VALOR A PAGAR: R$ {total:.2f}")