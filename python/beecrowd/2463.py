N = int(input())
vidas = list(map(int, input().split()))

max_vidas = 0

total_vidas = 0

for sala in vidas:

    total_vidas += sala

    if total_vidas > max_vidas:
        max_vidas = total_vidas

    if total_vidas < 0:
        total_vidas = 0

print(max_vidas)
