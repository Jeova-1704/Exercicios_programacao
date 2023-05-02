hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split())

duracao_minutos = (hora_fim * 60 + minuto_fim) - (hora_inicio * 60 + minuto_inicio)
if duracao_minutos <= 0:
    duracao_minutos += 24 * 60
duracao_horas = duracao_minutos // 60
duracao_minutos = duracao_minutos % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_horas, duracao_minutos))