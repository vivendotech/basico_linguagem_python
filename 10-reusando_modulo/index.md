---
title: "Entendo o import do Python"
date: 2020-01-31T00:14:11-03:00
draft: false

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Importe toda sua lição de casa de outro documento" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "Importando modulos no Python, Import Python." # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.
---

Até agora estavamos falando de programas que eram compostos de apenas 1 documento. Até agora você tinha acesso apenas uma quantidade restrita de coisas prontas. Mas tudo muda agora. A partir desse momento você poderá importar códigos prontos feitos por outra pessoa. Essa outra pessoa pode ser você no passado. Olha só, derrepente você pode importar todo o seu trabalho de outra biblioteca #dev_sincero. Nada se constroi tudo se importa!

# Construindo um modulo.

Iremos construir o módulo que calcula se um foguete consegue voar ou não. Para isso escreveremos o módulo "foguete_biblioteca.py". Para isso copie o codigo a baixo dentro do arquivo foguete_biblitoeca.py

```python
# arquivo foguete_biblioteca.py
def ola_modulo_foguete():
    print("Foguete espacial construído")


def calculo_velocidade(velocidade_tempo):
    const_aceleracao = 3
    return velocidade_tempo + const_aceleracao

def calculo_massa(massa_tempo):
    const_perda_masa = -3
    return massa_tempo + const_perda_masa


```
# Importando sua biblitoca

Existe várias formas de importar bibliotecas no Python. Que iremos explorar nos tópicos seguintes. Por enquanto, que estamos entendendo, apenas os mecanimos vamos importar todos as funções construidas no módulo. Para exemplificar isso construa um novo documento, chamado aqui no tutorial de "calculo_velocidade_foguete.py". É super importante que esse documento criado esteja na mesma pasta que o módulo construido para funcionar. Existe outras formas de importar biblitoecas que veremos mais para frente. Dentro desse documento escreva a frase "from foguete_biblioteca import *" que significa dizer para o compilador que a partir do modulo chamada foguete_bilioteca você gostaria de importar TUDO! 

``` python
# arquivo foguete_calculo.py
from foguete_biblioteca import *
ola_modulo_foguete() # testa se importou corretamente o módulog
# Foguete espacial construído
```

# Usando o módulo do foguete

```python
from foguete_biblioteca import *

velocidade_tempo = 100
massa_tempo = 200
for tempo_foguete in lis_fogueute_tempo:
    velocidade_tempo = calculo_velocidade(tempo_foguete, velocidade_tempo)
    massa_tempo = calculo_massa(tempo_foguete, massa_tempo)
    
    print(velocidade_tempo)
    # 200
    # 300
    # 400
    print(massa_tempo)
    # 196
    # 192
    # 188
```

# Importanto as bibliotecas padrões do Python.
Para importar as bibliotecas padrões do Python é feito da mesma forma. Para exemplificar vamos importar a biblioteca Turtle, responsavel por desenhar nosso foguete e a biblioteca padrão time para adicionar um tempo ao looping for.



```python
from foguete_biblioteca import *
from turtle import *
import time

# construindo o tempo
lis_fogueute_tempo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #segundos

# inicializando a velocidade inicial e massa do foguete
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

```
