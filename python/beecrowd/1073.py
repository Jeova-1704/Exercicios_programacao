casos = int(input())
for v in range(1, casos+1):
    if v % 2 == 0:
        print(f'{v}^2 = {pow(v, 2)}')