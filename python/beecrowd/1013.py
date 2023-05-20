A, B, C = input().split()
maior = 0 

A = int(A)
if A > maior:
    maior = A
B = int(B)
if B > maior:
    maior = B
C = int(C)
if C > maior:
    maior = C

print("{} eh o maior".format(maior))