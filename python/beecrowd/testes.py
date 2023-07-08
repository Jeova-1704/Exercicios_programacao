n, g = map(int, input().split())
runas = {}
for _ in range(n):
    ri, vi = input().split()
    runas[ri] = int(vi)

x = int(input())
recitadas = input().split()

amizade = sum(runas[ri] for ri in recitadas)
if amizade <= g:
    print(amizade)
    print('You shall pass!')
else:
    print(amizade)
    print('My precioooous')