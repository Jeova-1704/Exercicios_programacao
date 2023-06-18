valor = float(input())
valor_centavos = int(valor * 100)

notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]

print('NOTAS:')
for nota in notas:
    quantidade = valor_centavos // (nota * 100)
    valor_centavos %= nota * 100
    print(f'{quantidade} nota(s) de R$ {nota:.2f}')

print('MOEDAS:')
for moeda in moedas:
    quantidade = valor_centavos // moeda
    valor_centavos %= moeda
    valor_moeda = moeda / 100
    print(f'{quantidade} moeda(s) de R$ {valor_moeda:.2f}')
