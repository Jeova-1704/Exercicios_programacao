def pontuacao(list):
    score = 0
    for pontos, distancia in list:
        score += pontos * distancia
    return score

def vitorioso(listas_J, listas2):
    scoreJoao = pontuacao(listas_J)
    scoreMaria = pontuacao(listas2)
    if scoreJoao > scoreMaria:
        return 'JOAO'
    else:
        return 'MARIA'

n = int(input())
for _ in range(n):
    jogadas_joao = []
    jogadas_maria = []

    for _ in range(3):
        pontos, distancia = map(int, input().split())
        jogadas_joao.append([pontos, distancia])

    for _ in range(3):
        pontos, distancia = map(int, input().split())
        jogadas_maria.append([pontos, distancia])

    vencedor = vitorioso(jogadas_joao, jogadas_maria)
    print(f'{vencedor}')    
