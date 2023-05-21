n = int(input())
for _ in range(n):
    flag = False
    h, d, g = map(int, input().split())
    if 200 <= h <= 300 :
        if d >= 50:
            if g >= 150:
                flag = True
    if flag == True:
        print('Sim')
    else:
        print('Nao')
