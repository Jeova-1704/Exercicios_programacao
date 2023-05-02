N = input()

N = int(N)
horas = N // 3600
resto = N % 3600
minutos = resto // 60
resto = resto % 60
segundos = resto

print(f'{horas}:{minutos}:{segundos}')