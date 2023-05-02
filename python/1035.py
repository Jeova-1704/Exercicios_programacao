A, B, C, D =  input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)
somaCD = C + D
somaAB = A + B

if B > C and D > A and somaCD > somaAB and C > 0 and D > 0 and A % 2 == 0:
    print('Valores aceitos')

else:
    print('Valores nao aceitos')
