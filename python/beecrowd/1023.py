# cidade = 1
# while True:
#     casos = int(input())
#     if casos == 0:
#         break

#     dados_pessoas = []
#     consumo_por_pessoa = []
#     consumo_maximo = 0
#     total_pessoas = 0
#     for _ in range(casos):
#         x, y = map(int, input().split())
#         consumo_maximo += y
#         total_pessoas += x
#         dados_pessoas.append([x, y])
    
#     for consumo_pessoal in dados_pessoas:
#         consumo = consumo_pessoal[1] // consumo_pessoal[0]
#         consumo_por_pessoa.append([consumo_pessoal[0], consumo])
    
#     consumo_medio = consumo_maximo / total_pessoas
#     consumo_por_pessoa = sorted(consumo_por_pessoa, key=lambda x: x[1])
    
#     print(f'Cidade# {cidade}:')
#     dados_formatados = [f'{dados[0]}-{dados[1]}' for dados in consumo_por_pessoa]
#     print(' '.join(dados_formatados))
#     print(f'Consumo medio: {consumo_medio:.2f} m3.\n')
#     cidade += 1






# for consumo_pessoal in dados_pessoas:
#     consumo = consumo_pessoal[1] // consumo_pessoal[0]
#     consumo_por_pessoa.append([consumo_pessoal[0], consumo])


# cidade = 1
# while True:
#     casos = int(input())
#     if casos == 0:
#         break

#     dados_pessoas = []
#     consumo_por_pessoa = []
#     consumo_maximo = 0
#     total_pessoas = 0
#     for _ in range(casos):
#         x, y = map(int, input().split())
#         consumo_maximo += y
#         total_pessoas += x
#         dados_pessoas.append([x, y])
    
#     consumo_por_pessoa = [[dados[0], dados[1] // dados[0]] for dados in dados_pessoas]

#     consumo_medio = consumo_maximo / total_pessoas
#     consumo_por_pessoa.sort(key=lambda x: x[1])

#     print(f'Cidade# {cidade}:')
#     for dados in consumo_por_pessoa:
#         print(f'{dados[0]}-{dados[1]}', end=' ')
#     print(f'\nConsumo medio: {consumo_medio:.2f} m3.\n')
#     cidade += 1





# from math import floor

# cidade = 1
# while True:
#     casos = int(input())
#     if casos == 0:
#         break

#     dados_pessoas = []
#     consumo_por_pessoa = []
#     consumo_maximo = 0
#     total_pessoas = 0
#     for _ in range(casos):
#         x, y = map(int, input().split())
#         consumo_maximo += y
#         total_pessoas += x
#         dados_pessoas.append([x, y])
    
#     for consumo_pessoal in dados_pessoas:
#         consumo = floor(consumo_pessoal[1] / consumo_pessoal[0])
#         consumo_por_pessoa.append([consumo_pessoal[0], consumo])
    
#     consumo_medio = consumo_maximo / total_pessoas

#     consumo_por_pessoa = sorted(consumo_por_pessoa, key=lambda x: x[1])  # Correção aqui
#     print(f'Cidade# {cidade}:')
#     for dados in consumo_por_pessoa:  # Correção aqui
#         print(f'{dados[0]}-{dados[1]}', end=' ')
#     print(f'\nConsumo medio: {consumo_medio:.2f} m3.\n')
#     cidade += 1


# cidade = 1
# while True:
#     casos = int(input())
#     if casos == 0:
#         break

#     consumo_por_pessoa = []
#     consumo_maximo = 0
#     total_pessoas = 0

#     for _ in range(casos):
#         x, y = map(int, input().split())
#         consumo_maximo += y
#         total_pessoas += x
#         consumo_por_pessoa.append([x, y // x])

#     consumo_medio = consumo_maximo / total_pessoas
#     consumo_por_pessoa.sort(key=lambda x: x[1])

#     print(f'Cidade# {cidade}:')
#     for x, consumo in consumo_por_pessoa:
#         print(f'{x}-{consumo}', end=' ')
#     print(f'\nConsumo medio: {consumo_medio:.2f} m3.\n')
#     cidade += 1


# cidade = 1

# while True:
#     casos = int(input())
    
#     if casos == 0:
#         break

#     consumo_por_pessoa = []
#     consumo_maximo = 0
#     total_pessoas = 0
    
#     for _ in range(casos):
#         x, y = map(int, input().split())
#         consumo_maximo += y
#         total_pessoas += x
#         consumo_por_pessoa.append([x, y // x])
    
#     consumo_medio = consumo_maximo / total_pessoas
#     consumo_por_pessoa.sort(key=lambda x: x[1])

#     print(f'Cidade# {cidade}:')
#     print(' '.join([f'{x}-{consumo}' for x, consumo in consumo_por_pessoa]))
#     print(f'Consumo medio: {consumo_medio:.2f} m3.\n')
#     cidade += 1



# cidade = 1
# while True:
#     casos = int(input())
    
#     if casos == 0:
#         break

#     consumo_maximo = 0
#     total_pessoas = 0
#     consumo_por_pessoa = []

#     for _ in range(casos):
#         x, y = map(int, input().split())
#         consumo_maximo += y
#         total_pessoas += x
#         consumo_por_pessoa.append([x, y // x])
    
#     consumo_medio = consumo_maximo / total_pessoas
#     consumo_por_pessoa.sort(key=lambda x: x[1])

#     print(f'Cidade# {cidade}:')
#     for x, consumo in consumo_por_pessoa:
#         print(f'{x}-{consumo}', end=' ')
#     print(f'\nConsumo medio: {consumo_medio:.2f} m3.\n')
#     cidade += 1



# cidade = 1

# while True:
#     casos = int(input())
#     if casos == 0:
#         break
    
#     consumo = {}
#     consumo_total = 0
#     total_residentes = 0
    
#     for _ in range(casos):
#         residentes, valor_consumo = map(int, input().split())
        
#         chave = valor_consumo // residentes
#         if chave in consumo:
#             consumo[chave] += residentes
#         else:
#             consumo[chave] = residentes
#         consumo_total += valor_consumo
#         total_residentes += residentes
    
#     print(f"Cidade# {cidade}:")
    
#     for consumo_pessoa, residentes in sorted(consumo.items()):
#         print(f"{residentes}-{consumo_pessoa}", end=" ")
    
#     media = consumo_total / total_residentes
#     print("\nConsumo medio: {:.2f} m3.".format(media))
#     print()
#     cidade += 1















# # erro de 100%

# cidade = 1

# while True:
#     casos = int(input())
#     if casos == 0:
#         break
    
#     consumo = {}
#     consumo_total = 0
#     total_residentes = 0
    
#     for _ in range(casos):
#         residentes, valor_consumo = map(int, input().split())
        
#         chave = valor_consumo // residentes
#         if chave in consumo:
#             consumo[chave] += residentes
#         else:
#             consumo[chave] = residentes
#         consumo_total += valor_consumo
#         total_residentes += residentes
    
#     print(f"Cidade# {cidade}:")
    
#     for consumo_pessoa, residentes in sorted(consumo.items()):
#         print(f"{residentes}-{consumo_pessoa}", end=" ")
    
#     media = consumo_total / total_residentes
#     print(f"\nConsumo medio: {media:.2f} m3.")
#     print()
#     cidade += 1






# def main():
#     from sys import stdin, stdout
#     from collections import defaultdict
#     from operator import itemgetter
#     from math import floor

#     def truncate(f):
#         return floor(f * 100) / 100

#     cidade = 1
#     casos = int(stdin.readline())
#     while True:
#         consumptions = defaultdict(int)
#         total_consumption = total_residents = 0
#         for _ in range(casos):
#             x, y = map(int, stdin.readline().split())
#             consumptions[y // x] += x
#             total_consumption += y
#             total_residents += x

#         stdout.write(f'Cidade# {cidade}:\n')
#         stdout.write(' '.join(f'{c[1]}-{c[0]}' for c in sorted(consumptions.items(), key=itemgetter(0))))
#         stdout.write(f'\nConsumo medio: {truncate(total_consumption / total_residents):.2f} m3.\n')

#         casos = int(stdin.readline())
#         if casos == 0:
#             break
#         stdout.write('\n')
#         cidade += 1

# main()



import math

T = 0
while True:
    try:
        N = int(input())

        if(N == 0):
            break

        if(T):
            print('')

        totalX, totalY = 0, 0
        consumos = {}
        for _ in range(N):
            X, Y = map(int, input().split(' '))

            totalX += X
            totalY += Y

            if (Y//X in consumos):
                consumos[Y//X] += X
            else:
                consumos[Y//X] = X

        consumo_total = ((100 * totalY)/totalX)/100

        T += 1
        print(f'Cidade# {T}:')

        output = []
        keys = sorted(list(consumos.keys()))
        for key in keys:
            output.append(f'{consumos[key]}-{key}')

        print(f'{" ".join(output)}')

        consumo_medio = math.floor((100 * totalY)/totalX)/100

        print(f'Consumo medio: {consumo_medio:.2f} m3.')
    except EOFError:
        break