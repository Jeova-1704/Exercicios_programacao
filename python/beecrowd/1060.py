positivos = 0 
for _ in range(6):
    x = float(input())
    if x > 0:
        positivos += 1
print(f'{positivos} valores positivos')