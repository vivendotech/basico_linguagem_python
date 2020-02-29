---
title: "Operadores lógicos do python"
date: 2020-01-31T00:14:11-03:00
draft: false

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Operadores lógicos do python" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "Operadores lógicos no python" # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.
---


Os operadores lógicos servem para criar uma lógica no programa entre uma ou mais variaveis boleanas. No python as variaveis são fortemente tipadas o que significa que o tipo da variavel importa. E isso se demonstra quando começamos a operar variaveis no nosso programa. Iremos entrar mais a fundo nesse tópico em post seguintes mas tenha em mente que a operação que o sinal ira realizar é depentende do tipo das variaveis. Geralmente quando lidamos com operadores lógicos mostramos as possiblidades que esses operadores retornam em forma de uma tabela. Essa tabela é tão importante que tem um nome, é a famigerada tabela verdade. Em post, no nivel mediano iremos falar mais a fundo como manipular expressões lógicas, como reduzilas usando as leis de Morgan. Mas a introdução ao uso de variaveis boleanas veremos nesse post.

Os operadores lógicos retoram um valor boleano conforme uam tabela verdade.

# Operador de negação (Not)

O operador *Not* inverte o valor boleano. Então, se a entrada for verdadeira(True) o retorn sera falso (False). A tabela verdade desse operador pode ser visto a baixo:
 | x | y= not x |
 | --- |--- | 
 | False | True|
 | True | False|

 No codigo 1 iremos usar o operador not em uma variavel. 

 ```python
 x = True # atribuimos a variavel x o valor True
 y = not x # atribuimos a variavel y o valor not X
 print(y)
 # False
 ```


# Operador E (AND)
O operador AND retorna verdadeiro apenas quando os valores de entrada são verdadeiros. Note que o operador AND necessita duas entradas. A tabela verdade dele depende da combinação de duas variaveis.
Ambos os valores devem ser verdadeiros para essa função retorar verdadeiro (True);
| x | y | z = x and y |
| --- |--- | --- |
| False | False| False |
| True | False| False |
| False | True| False |
| True | True| True |

```python
x = True
y = True
z = x and y
print(z)
# True
```
# Operador (OR)

O operador OR retorna verdadeiro se pelo menos uma das opções da função ser verdadeiro. Veja a tabela verdade a baixo

 | x | y | x or y |
 | --- |--- | 
 | False | False| False |
 | True | False| True |
 | False | True| True |
 | True | True| True |


```python
x = False
y = True
z = x or y
print(z)
# True
```

# Operador de igualdade boleana

O operador de igualdade boleana retorna verdadeiro caso as duas opções sejam verdadeiras
 | x | y | x == y |
 | --- |--- | 
 | False | False| True |
 | True | False| False |
 | False | True| False |
 | True | True| True |


# Operador de desigualdade boleana

A operação de desiguldade boleana retorna verdadeiro quando as entradas da função são diferentes. Veja tabela verdade a baixo.

 | x | y | x != y |
 | --- |--- | 
 | False | False| False |
 | True | False| True |
 | False | True| True |
 | True | True| False |


# Igualdade entre duas variaveis do mesmo tipo

# Operador maior menor


Proximo topico é o operador no python
