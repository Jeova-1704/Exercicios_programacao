n = int(input())
meninos, meninas = [0,0]

for c in range(n):
    nome, sexo = map(str, input().lower().split())
    if sexo == 'm':
        meninos += 1
    else:
        meninas += 1
print(f'{meninos} carrinhos')
print(f'{meninas} bonecas')
