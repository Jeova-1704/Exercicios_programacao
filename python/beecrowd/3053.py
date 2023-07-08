def realizar_movimento(posicao_moeda, tipo_movimento):
    if tipo_movimento == 1:
        if posicao_moeda == 'A':
            return 'B'
        elif posicao_moeda == 'B':
            return 'A'
    elif tipo_movimento == 2:
        if posicao_moeda == 'B':
            return 'C'
        elif posicao_moeda == 'C':
            return 'B'
    elif tipo_movimento == 3:
        if posicao_moeda == 'A':
            return 'C'
        elif posicao_moeda == 'C':
            return 'A'
    
    return posicao_moeda


N = int(input())
posicao_moeda = input()

for _ in range(N):
    tipo_movimento = int(input())
    posicao_moeda = realizar_movimento(posicao_moeda, tipo_movimento)

print(posicao_moeda)
