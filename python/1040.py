notas = input().split()
n1, n2, n3, n4 = float(notas[0]), float(notas[1]), float(notas[2]), float(notas[3])

media = (n1*2 + n2*3 + n3*4 + n4*1) / 10

print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    nova_media = (media + exame) / 2
    if nova_media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(nova_media))
