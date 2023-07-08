nome, dia1 = map(str, input().split())
dia1 = int(dia1)
hora1, minuto1, segundo1 = map(int, input().split(':'))

nome, dia2 = map(str, input().split())
hora2, minuto2, segundo2 = map(int, input().split(':'))
dia2 = int(dia2)

segundos = segundo2 - segundo1
minutos = minuto2 - minuto1
horas = hora2 - hora1
dias = dia2 - dia1

if segundos < 0:
    segundos += 60
    minutos -= 1
if minutos < 0:
    minutos += 60
    horas -= 1
if horas < 0:
    horas += 24
    dias -= 1

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
