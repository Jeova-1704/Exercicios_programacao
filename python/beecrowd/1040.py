n1, n2, n3, n4 = map(float, input().split())
p1, p2, p3, p4 = [2, 3, 4, 1]
media = ((n1 * p1)+(n2 * p2)+(n3 * p3)+(n4 * p4))/(p1+p2+p3+p4)

print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')

elif media < 5.0:
    print('Aluno reprovado.')

else:
    print('Aluno em exame.')
    nota = float(input())
    print(f'Nota do exame: {nota:.1f}')
    nova_media = (media + nota) / 2
    if nova_media >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {nova_media}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {nova_media}')

