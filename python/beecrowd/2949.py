# racas = {}
# anoes, elfos, humanos, magos, hobbits  = [0, 0, 0, 0, 0]
# n = int(input())

# for v in range(n):
#     n, r = input().lower().split()
#     racas[n] = r

# for r in racas:
#     if racas[r] == 'a':
#         anoes += 1
#     if racas[r] == 'e':
#         elfos += 1
#     if racas[r] == 'h':
#         humanos += 1
#     if racas[r] == 'm':
#         magos += 1
#     if racas[r] == 'x':
#         hobbits += 1

# print(f'{hobbits} Hobbit (s)')
# print(f'{humanos} Humano (s)')
# print(f'{elfos} Elfo (s)')
# print(f'{anoes} Anao (oes)')
# print(f'{magos} Mago (s)')


from collections import defaultdict

N = int(input())

i = 1
# comitiva = {
#     'anoes': 0,
#     'elfos': 0,
#     'humanos': 0,
#     'magos': 0,
#     'hobbits': 0
# }

comitiva = {}

comitiva = defaultdict(lambda : 0, comitiva) # Ele fornece um valor padrão para a chave que não existe.

while i <= N:
    nome_raca, tipo = map(str, input().split())
    if tipo == 'A':
        comitiva['anoes'] += 1
    if tipo == 'E':
        comitiva['elfos'] += 1
    if tipo == 'H':
        comitiva['humanos'] += 1
    if tipo == 'M':
        comitiva['magos'] += 1
    if tipo == 'X':
        comitiva['hobbits'] += 1

    i += 1

print("{} Hobbit(s)\n{} Humano(s)\n{} Elfo(s)\n{} Anao(s)\n{} Mago(s)".format(comitiva['hobbits'],comitiva['humanos'],comitiva['elfos'], comitiva['anoes'], comitiva['magos']))