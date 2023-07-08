def imprimir_numeros(s1, s2, d1, d2):

    print(f'A = {s1:.6f}, B = {s2:.6f}')
    print(f'C = {d1:.6f}, D = {d2:.6f}')

    print(f'A = {s1:.1f}, B = {s2:.1f}')
    print(f'C = {d1:.1f}, D = {d2:.1f}')

    print(f'A = {s1:.2f}, B = {s2:.2f}')
    print(f'C = {d1:.2f}, D = {d2:.2f}')

    print(f'A = {s1:.3f}, B = {s2:.3f}')
    print(f'C = {d1:.3f}, D = {d2:.3f}')

    print(f'A = {s1:.3e}, B = {s2:.3e}')
    print(f'C = {d1:.3e}, D = {d2:.3e}')

    print(f'A = {int(s1)}, B = {int(s2)}')
    print(f'C = {int(d1)}, D = {int(d2)}')



s1, s2 = map(float, input().split())
d1, d2 = map(float, input().split())
imprimir_numeros(s1, s2, d1, d2)
