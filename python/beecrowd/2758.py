# # Leitura dos valores de entrada
# A, B = map(float, input().split())
# C, D = map(float, input().split())

# # Impressão dos valores originais
# print(f"A = {A:.6f}, B = {B:.6f}")
# print(f"C = {C:.6f}, D = {D:.6f}")

# # Impressão dos valores com uma casa decimal
# print(f"A = {A:.1f}, B = {B:.1f}")
# print(f"C = {C:.1f}, D = {D:.1f}")

# # Impressão dos valores com duas casas decimais
# print(f"A = {A:.2f}, B = {B:.2f}")
# print(f"C = {C:.2f}, D = {D:.2f}")

# # Impressão dos valores com três casas decimais
# print(f"A = {A:.3f}, B = {B:.3f}")
# print(f"C = {C:.3f}, D = {D:.3f}")

# # Impressão dos valores em notação científica
# print(f"A = {A:.3E}, B = {B:.3E}")
# print(f"C = {C:.3E}, D = {D:.3E}")

# # Impressão somente da parte inteira
# print(f"A = {int(A)}, B = {int(B)}")
# print(f"C = {int(C)}, D = {int(D)}")



from struct import pack, unpack

e = str(input()).split()
a = float(unpack("f", pack("f", float(e[0])))[0])
b = float(unpack("f", pack("f", float(e[1])))[0])

e = str(input()).split()
c = float(e[0])
d = float(e[1])

print('A = {:.6f}, B = {:.6f}'.format(a, b))
print('C = {:.6f}, D = {:.6f}'.format(c, d))

print('A = {:.1f}, B = {:.1f}'.format(a, b))
print('C = {:.1f}, D = {:.1f}'.format(c, d))

print('A = {:.2f}, B = {:.2f}'.format(a, b))
print('C = {:.2f}, D = {:.2f}'.format(c, d))

print('A = {:.3f}, B = {:.3f}'.format(a, b))
print('C = {:.3f}, D = {:.3f}'.format(c, d))

print('A = {:.3E}, B = {:.3E}'.format(a, b))
print('C = {:.3E}, D = {:.3E}'.format(c, d))

print('A = {:.0f}, B = {:.0f}'.format(a, b))
print('C = {:.0f}, D = {:.0f}'.format(c, d))