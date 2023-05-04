y = float(input())
x = list()

for c in range(100):
    x.append(f'{y:.4f}')
    y /= 2

for i, v in enumerate(x):
    print(f'N[{i}] = {v}')