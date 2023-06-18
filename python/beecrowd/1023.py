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


cidade = 1
while True:
    casos = int(input())
    if casos == 0:
        break

    dados_pessoas = []
    consumo_por_pessoa = []
    consumo_maximo = 0
    total_pessoas = 0
    for _ in range(casos):
        x, y = map(int, input().split())
        consumo_maximo += y
        total_pessoas += x
        dados_pessoas.append([x, y])
    
    consumo_por_pessoa = [[dados[0], dados[1] // dados[0]] for dados in dados_pessoas]

    consumo_medio = consumo_maximo / total_pessoas
    consumo_por_pessoa.sort(key=lambda x: x[1])

    print(f'Cidade# {cidade}:')
    for dados in consumo_por_pessoa:
        print(f'{dados[0]}-{dados[1]}', end=' ')
    print(f'\nConsumo medio: {consumo_medio:.2f} m3.\n')
    cidade += 1





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

#     print(f'Cidade# {cidade}:')
#     for x, consumo in consumo_por_pessoa:
#         print(f'{x}-{consumo}', end=' ')
#     print(f'\nConsumo medio: {consumo_medio:.2f} m3.\n')
#     cidade += 1