A, B, C = map(str,input().split())
pi = 3.14159

A = float(A)
B = float(B)
C = float(C)

print(f'TRIANGULO: {(A * C) / 2:.3f}')
print(f'CIRCULO: {pi * (C**2 ):.3f}')
print(f'TRAPEZIO: {((A + B) * C ) / 2:.3f}')
print(f'QUADRADO: {B * B:.3f}')
print(f'RETANGULO: { A * B :.3f}')
