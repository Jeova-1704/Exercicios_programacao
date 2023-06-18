"""
Raju e Meena adoram jogar um jogo diferente com pequenas peças de mármores, chamados Marbles. Eles têm um monte destas peças com números escritos neles. No início, Raju colocaria estes pequenos mármores um após outro em ordem ascendente de números escritos neles. Então Meena gostaria de pedir a Raju para encontrar o primeiro mármore com um certo número. Ele deveria contar 1...2...3. Raju ganha um ponto por cada resposta correta e Meena ganha um ponto se Raju falha. Depois de um número fixo de tentativas, o jogo termina e o jogador com o máximo de pontos vence. Hoje é sua chance de jogar com Raju. Sendo um/a cara esperto/a, você tem em seu favor o computador. Mas não subestime Meena, ela escreveu um programa para monitorar quanto tempo você levará para dar todas as respostas. Portanto, agora escreva o programa, que ajudará você em seu desafio com Raju.

Entrada
A entrada contém vários casos de teste, mas o total de casos é menor do que 65. Cada caso de teste inicia com dois inteiros: N que é o número de mármores e Q que é o número de consultas que Meena deseja fazer. As próximas N linhas conterão os números escritos em cada um dos N mármores. Os números destes mármores não tem qualquer ordem em particular. As seguintes Q linhas irão conter Q consultas. Tenha certeza, nenhum dos números da entrada é maior do que 10000 e nenhum deles é negativo.
A entrada é terminada por um caso de teste onde N = 0 e Q = 0.

Saída
Para cada caso de teste de saída deve haver um número serial do caso de teste. Para cada consulta, escreva uma linha de saída. O formato desta linha dependerá se o número consultado estiver ou não escrito em um dos mármores. Os dois diferentes formatos são descritos abaixo:
'x found at y', se o primeiro marble x foi encontrado na posição y. Posições são numeradas de 1, 2,...  a N.
'x not found', se o marble com o número x não estiver presente.
"""
# contador = 1
# while contador <= 65:
#     numeros_marmore = []
#     numeros_acertado = []
#     numeros_errados = []
#     N, Q = [int(x) for x in input().split()]
#     if N == 0 and Q == 0:
#         break

#     for _ in range(N):
#         numero = int(input())
#         numeros_marmore.append(numero)

#     for _ in range(Q):
#         suposicao_marmore = int(input())
#         if suposicao_marmore in numeros_marmore:
#             numeros_acertado.append([suposicao_marmore, numeros_marmore.index(suposicao_marmore)])
#         else:
#             numeros_errados.append(suposicao_marmore)

#     print(f'CASE# {contador}')
#     if len(numeros_errados) > 0:
#         for erro in numeros_errados:
#             print(f'{erro} not found')
#     for acertado in numeros_acertado:
#         print(f'{acertado[0]} found at {acertado[1]+1}')

#     contador += 1



caso = 1
while caso <= 60:
    marmore = []
    N, Q = map(int, input().split())
    if N == Q == 0:
        break

    for _ in range(N):
        marmore.append(int(input()))

    marmore.sort()

    print(f'CASE# {caso}:')
    for _ in range(Q):
        x = int(input())
        if x in marmore:
            print(f'{x} found at {marmore.index(x)}')
        else:
            print(f'{x} not found')
            
    caso += 1
