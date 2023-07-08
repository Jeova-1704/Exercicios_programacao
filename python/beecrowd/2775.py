def soma_time(pacotes, tempo):
    N = len(pacotes)
    total_tempo = 0
    
    for i in range(N-1):
        if pacotes[i] != i+1:
            j = pacotes.index(i+1)
            total_tempo += abs(j - i) * tempo[i]
            
            pacotes[i:j+1] = pacotes[i:j+1][::-1]
    
    return total_tempo


while True:
    try:
        qtd_pacotes = int(input())
        pacotes_entrega = list(map(int, input().split()))
        tempo_por_pacote = list(map(int, input().split()))

        soma_maxima = soma_time(pacotes_entrega, tempo_por_pacote)
        print(soma_maxima)

    except EOFError:
        break
