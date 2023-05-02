todos = []
ordenados = []

x, y, z = map(int, input().split())
todos.append(x)
todos.append(y)
todos.append(z)
ordenados.append(x)
ordenados.append(y)
ordenados.append(z)
ordenados.sort()


for i in ordenados:
    print(i)

print()

for i in todos:
    print(i)
