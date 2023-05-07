n = int(input())
valores = [num for num in range(10000) if num % n == 2]
for v in valores:
    print(v)
