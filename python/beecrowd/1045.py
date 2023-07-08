a, b, c = sorted(map(float, input().split()), reverse=True)

if (a) >= (b + c):
    print('NAO FORMA TRIANGULO')

elif (a*a) == ((b*b) + (c*c)):
    print('TRIANGULO RETANGULO')

elif (a*a) > ((b*b) + (c*c)):
    print('TRIANGULO OBTUSANGULO')

elif (a*a) < ((b*b) + (c*c)):
    print('TRIANGULO ACUTANGULO')

if (a == b) and (b == c):
    print('TRIANGULO EQUILATERO')

elif (a == b) or (a == c) or (b == c):
    print('TRIANGULO ISOSCELES')
