tempo = input()
velocidade = input()

tempo = int(tempo)
velocidade = int(velocidade)
distancia = velocidade * tempo
litros = distancia / 12

print("{:.3f}".format(litros))