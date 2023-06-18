from math import gcd #Para encontrar um maximo divisor comum 

def resultado(n1, d1, operacao, n2, d2):
    if operacao == '+':
        numerador = (n1*d2 + n2*d1) 
        denominador = (d1*d2)

    elif operacao == '-':
        numerador = (n1*d2 - n2*d1)
        denominador = (d1*d2)

    elif operacao == '*':
        numerador = n1*n2
        denominador = d1*d2
        
    elif operacao == '/':
        numerador = n1*d2
        denominador = n2*d1

    return numerador, denominador

def simplificacao(numerador, denominador):
    mdc = gcd(numerador, denominador)
    novo_numerador = int(numerador/mdc)
    novo_denominador = int(denominador/mdc)
    return novo_numerador, novo_denominador


entrada = int(input())

for _ in range(entrada):
    n1, caractere, d1, operacao, n2, caractere, d2 = map(str, input().split())
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)
    numerador, denominador = resultado(n1, d1, operacao, n2, d2)
    numerador_simplificador, denominador_simplificado = simplificacao(numerador, denominador)
    print(f'{numerador}/{denominador} = {numerador_simplificador}/{denominador_simplificado}')
