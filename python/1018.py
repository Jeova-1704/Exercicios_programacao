valor = input()

valor = int(valor)
print(valor)
cem = valor // 100
valor = valor % 100
print("{} nota(s) de R$ 100,00".format(cem))

cinquenta = valor // 50
valor = valor % 50
print("{} nota(s) de R$ 50,00".format(cinquenta))

vinte = valor // 20
valor = valor % 20
print("{} nota(s) de R$ 20,00".format(vinte))

dez = valor // 10
valor = valor % 10
print("{} nota(s) de R$ 10,00".format(dez))

cinco = valor // 5
valor = valor % 5
print("{} nota(s) de R$ 5,00".format(cinco))

dois = valor // 2
valor = valor % 2
print("{} nota(s) de R$ 2,00".format(dois))

um = valor // 1
valor = valor % 1
print("{} nota(s) de R$ 1,00".format(um))

