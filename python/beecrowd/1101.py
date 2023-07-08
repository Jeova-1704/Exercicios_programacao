while True:
    soma = 0
    x, y = sorted(map(int, input().split()))
    if x <= 0 or y <= 0:
        break
    for i in  range(x, y+1):
        print(i, end=' ')
        soma += i
    print(f'Sum={soma}')
