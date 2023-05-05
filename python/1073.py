# n = max(5, min(2000, int(input()))) limita a entrada de dados com um intervalo definido

n = int(input())

for x in range(2, n+1):
    if x % 2 == 0:
        print(f'{x}^2 = {x**2}')