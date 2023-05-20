n = int(input())
for i in range(n):
    x = int(input())
    x_bin = bin(x)[2:]
    maximo_um_consecutivos = 0
    maximo_um = 0
    for bit in x_bin:
        if bit == '1':
            maximo_um += 1
            maximo_um_consecutivos = max(maximo_um_consecutivos, maximo_um)
        else:
            maximo_um = 0
    print(maximo_um_consecutivos)