n = int(input())

fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

for i in range(n):
    if i == n-1:
        print(fib[i])
    else:
        print(fib[i], end=' ')