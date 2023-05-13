# # cada funcionario beb um café por dia
# # cada funcionario leva um minuto para subir ou descer um andar

predio = [int(input()) for andar in range(3)]
tempo_deslocamento = []
tempo_deslocamento.append(predio[0]*4 + predio[1]*2)
tempo_deslocamento.append(predio[0]*2 + predio[2]*2)
tempo_deslocamento.append(predio[1]*2 + predio[2]*4)
tempo_deslocamento.sort()
print(tempo_deslocamento[0])
