from foguete_biblioteca import *

lis_fogueute_tempo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #segundos
list_foguete_massa = []
list_foguete_velocidade = []



# adição de elementos no array
# 
velocidade_tempo = 100
massa_tempo = 200
for tempo_foguete in lis_fogueute_tempo:
    velocidade_tempo = calculo_velocidade(tempo_foguete, velocidade_tempo)
    massa_tempo = calculo_massa(tempo_foguete, massa_tempo)

    list_foguete_velocidade.append(velocidade_tempo)
    list_foguete_massa.append(massa_tempo)

print(list_foguete_velocidade)
print(list_foguete_massa)
