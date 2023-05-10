# def resultados(jogada1, jogada2):
#     if jogada1 == jogada2:
#         return 'empate'
    
#     if jogada1 ==  'tesoura' and jogada2 == 'papel' or jogada1 ==  'papel' and jogada2 == 'pedra' or jogada1 ==  'pedra' and jogada2 == 'lagarto' or jogada1 ==  'lagarto' and jogada2 == 'Spock' or jogada1 ==  'Spock' and jogada2 == 'tesoura' or jogada1 ==  'tesoura' and jogada2 == 'lagarto' or jogada1 ==  'lagarto' and jogada2 == 'papel' or jogada1 ==  'papel' and jogada2 == 'Spock' or jogada1 ==  'Spock ' and jogada2 == 'pedra' or jogada1 ==  'pedra' and jogada2 == 'tesoura':
#         return 'sheldon'
#     else:
#         return 'raj'
    

# n = int(input())
# c = 0
# while c != n:
#     jogada1 , jogada2 = input().lower().split()
#     vencedor = resultados(jogada1, jogada2)
#     if vencedor == 'empate':
#         print('De novo!')
#     if vencedor == 'sheldon':
#         print('Bazinga!')
#     if vencedor == 'raj':
#         print('Raj trapaceou!')
#     c += 1






def jogada():
    s, r = map(str,input().split())
    return s,r


def contagem(cont):
    cont += 1
    return cont


def winner(a,b,cont,play):
    w = 1
    if a == 'tesoura' and b == 'papel':
        w = a
    if a == 'papel' and b == 'pedra':
        w = a
    if a == 'pedra' and b == 'lagarto':
        w = a
    if a == 'lagarto' and b =='Spock':
        w = a
    if a == 'Spock' and b == 'tesoura':
        w = a
    if a == 'tesoura' and b == 'lagarto':
        w = a
    if a == 'lagarto' and b == 'papel':
        w = a
    if a == 'papel' and b == 'Spock':
        w = a
    if a == 'Spock' and b == 'pedra':
        w = a
    if a == 'pedra' and b == 'tesoura':
        w = a
    if w == a:
        if play == 'she':
            print('Caso #{}: Bazinga!'.format(cont))
        if play == 'raj':
            print('Caso #{}: Raj trapaceou!'.format(cont))
    return w


def main():
    n = int(input())
    cont = 1
    for i in range(n):
        s, r = jogada()
        w = winner(s,r,cont,'she')
        if w != 1:
            cont = contagem(cont)
            continue
       
        w = winner(r,s,cont,'raj')
        if w != 1:
            cont = contagem(cont)
            continue
       
        if w == 1:
            print('Caso #{}: De novo!'.format(cont))
        cont = contagem(cont)
       
main()