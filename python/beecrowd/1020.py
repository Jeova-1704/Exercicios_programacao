idade_dias = input()

idade_dias = int(idade_dias)
anos = idade_dias // 365
idade_dias = idade_dias % 365

meses = idade_dias // 30 
idade_dias = idade_dias % 30

dias = idade_dias

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
