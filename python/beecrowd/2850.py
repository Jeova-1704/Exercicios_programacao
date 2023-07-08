pernas= {
    'esquerda': 'ingles',
    'direita': 'frances',
    'nenhuma':  'portugues',
    'as duas': 'caiu'
}

while True:
    try:
        x = input()
        fala = pernas.get(x)
        print(fala)
    
    except EOFError:
        break
    