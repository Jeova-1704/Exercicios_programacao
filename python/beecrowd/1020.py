dias_idade = int(input())

anos = dias_idade // 365
resto = dias_idade % 365
meses = resto // 30
resto = resto % 30
dias = resto

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')