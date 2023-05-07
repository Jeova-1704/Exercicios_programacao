n = input()
n = int(n)


for c in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        maior, menor = x, y
    else:
        maior, menor = y, x
    somaImpares = 0
    for s in range(menor+1, maior):
        if s % 2 != 0:
            somaImpares += s
    print(somaImpares)