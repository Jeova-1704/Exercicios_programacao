x = int(input())
y = int(input())
soma = 0

if x > y:
    maior = x
    menor = y   
else: 
    menor = x
    maior = y

for num in range(menor + 1, maior):
    if num % 2 != 0:
        soma += num

print(soma)