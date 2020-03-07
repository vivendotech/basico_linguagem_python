from foguete_biblioteca import *
from turtle import *
import time

lis_fogueute_tempo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #segundos


velocidade_tempo = 5
massa_tempo = 50

# inicializar a tartaruga
color('red', 'yellow')
begin_fill()

for tempo_foguete in lis_fogueute_tempo:

    # calculo de velcidade e massa
    velocidade_tempo = calculo_velocidade(velocidade_tempo)
    massa_tempo = calculo_massa(massa_tempo)


    # desenhando na tela
    # empurrando a tartaruga
    forward(velocidade_tempo)

    # mudando o tamanho da tartaruga
    resizemode("user") 
    shapesize(massa_tempo, massa_tempo, 12)
    

    # esperando um certo tempo 
    time.sleep(0.2)
    
    # Imprimindo na tela.
    print(velocidade_tempo)
    print(massa_tempo)

# terminado o desenho
end_fill()
done()