soma = 0
x = int(input())
y = int(input())

if x > y:
    x, y = y, x

for num in range(x+1, y):
    if num % 2 != 0:
        soma += num

print(soma)