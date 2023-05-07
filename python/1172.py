x = list()
for i in range(10):
    v = int(input())
    if v <= 0:
        x.append(1)
    else:
        x.append(v)
for i in range(10) :
    print(f'X[{i}] = {x[i]}')