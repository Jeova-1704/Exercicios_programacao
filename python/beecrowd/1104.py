"""Ana e Beatriz colecionam cartas de pokemon estão interesadas apenas nas cartas que cada uma possui um ‘id’ único.
Elas não querem trocar cartas identicas. E não querem receber cartas repetidas havera apenas uma única troca cada uma
da para outra um conjunto com n cartas distintas As meninas querem saber qual é o número máximo de cartas que podem
ser trocadas. Por exemplo, se Alice tem o conjunto de cartas Alice {1, 1, 2, 3, 5, 7, 8, 8, 9, 15} e Beatriz o
conjunto {2, 2, 2, 3, 4, 6, 10, 11, 11}, elas podem trocar entre si no máximo quatro cartas. Escreva um programa que,
dados os conjuntos de cartas que Alice e Beatriz possuem, determine o número máximo de cartas que podem ser trocada """


while True:
    try:
        A, B = [int(x) for x in input().strip().split()]

        if A == 0 and B == 0:
            break

        alice = set([int(x) for x in input().strip().split(' ')])
        beatriz = set([int(x) for x in input().strip().split(' ')])

        uniao = alice.union(beatriz)

        print(min(len(uniao) - len(beatriz), len(uniao) - len(alice))) 
    except EOFError:
        break


# while True:
#     try:
#         A, B = [int(x) for x in input().strip().split(' ')]

#         alice = set([int(x) for x in input().strip().split(' ')])
#         beatriz = set([int(x) for x in input().strip().split(' ')])

#         uniao = alice.union(beatriz)

#         print(min(len(uniao) - len(beatriz), len(uniao) - len(alice)))
#     except EOFError:
#         break