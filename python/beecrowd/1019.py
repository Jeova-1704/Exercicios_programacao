tempo = int(input())

horas = tempo // 3600
resto = tempo % 3600
minutos = resto // 60
segundos = resto % 60

print(f'{horas}:{minutos}:{segundos}')
