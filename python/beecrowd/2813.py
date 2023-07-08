# casos = int(input())
# casa = escritorio = quantidade = 0

# for i in range(casos):
#     chuva_ou_sol = input().split()

#     if chuva_ou_sol[0] == 'chuva':
#         quantidade -= 1

#         if casa > quantidade:
#             casa = quantidade

#     if chuva_ou_sol[1] == 'chuva':
#         quantidade += 1

#         if escritorio < quantidade:
#             escritorio = quantidade

# print(abs(casa), abs(escritorio))


casa = escritorio = qtd_casa = qtd_escritorio = 0

casos = int(input())

for g in range(casos):
    ida, volta = input().split()

    if ida == 'chuva':
        if casa > 0:
            casa -= 1
            escritorio += 1
        else:
            qtd_casa += 1
            escritorio += 1
            
    if volta == 'chuva':
        if escritorio > 0:
            escritorio -= 1
            casa += 1
        else:
            qtd_escritorio += 1
            casa += 1
print(qtd_casa, qtd_escritorio)


























