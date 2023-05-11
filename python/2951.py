n, g = map(int, input().split())

runas = {}
for c in range(n):
    r, v = input().split()
    runas[r] = int(v)

x = int(input())
recitadas = input().split()

amizade = sum(runas[r] for r in recitadas)
if amizade>= g:
    print(amizade)
    print('You shall pass!')
else:
    print(amizade)
    print('My precioooous')
