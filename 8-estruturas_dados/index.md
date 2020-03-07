---
title: "Estruturas de dados"
date: 2020-01-31T00:14:11-03:00
draft: false

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Estruturas de dados no python, finalmente começando a ficar interessante" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "Operadores lógicos no python" # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.
---

Até agora apenas mechiamos com variaveis primitivas, elas sózinhas não conseguem fazer muita coisa. Mas agora, quando combinadas com uma estrtura de dados elas começam a construir software mais interessantes.


# Tuplas
A primeira estrutura que iremos ver é a estrutura de tuplas. As tuplas relacionam uma série de variaveis que falam a respeito da mesma coisa. Por exemplo, queremos relacionar que uma pessoa chamada "joão" ganha um salario de 10 mil reais e possui a posição de engenheiro. 

## Construindo uma tupla

Para construir uma tupla basta escrever as variaveis que se relacionam entre paranteses. As variaveis devem estar divididas por uma virgula. Veja o código 1;
```python 
# codigo 1
#    nome   salarion posicao 
var_tupla_banco_dados = ("joao", 100000, "engenheiro") # construindo uma tupla
```

## Acessando elementos de uma tupla

Uma vez definindo uma variavel que guarda a estrtura de dados de uma tupla é possivel assesar os valores usando os colchetes ([]). Basta colocar a posição que a variavel se encontra na tupla e o valor é retornado. Vale resaltar que a contagem começa no 0.

```python

print(var_tupla_banco_dados[0]) # imprimi João
print(var_tupla_banco_dadosa[1]) # impimi 1000000
print(var_tupla_banco_dados[2]) # imprimi João
```

# Construindo uma lista de dados

Uma vez que possuimos mais de um valor que representa algo devemos listar. Por exemplo, vamos disser que tenhamos dois dados a respeito de nossos funcionarios. Esses dados devem ser postos numa lista, veja exemplo 2. Definir melhor o que é uma lista de dados. Uma lista é uma sequencia, alguma vezes ordenada, de dados que falam a respeito da mesma coisa. Por exemplo, uma lista de funcionarios, alimentos etc.


## Construindo uma lista
Para construir uma lista basta usar os colchetes. Para cada elemento na lista é dividido por uma virgula

```python
list_funcionarios = [("joao", 100000, "engenheiro"),
                    ("ricardo", 10000, "locutor radio"),
                    ("dona_mariquinha", 10000, "dona da empresa")]
```

## Acessando dados elementos de uma lista

Para acessar elementos de uma lista basta usar o colchetes([]) no final da variavel. E dentro dos colchetes passar a posição que você deseja acessar, veja codigo 4. Como nas tuplas o primeiro elemento da lista é o de numero 0.

```python
print(list_funcionarios[0]) # ("joao", 100000, "engenheiro")
print(list_funcionarios[1]) # ("ricardo", 10000, "locutor_radio")
print(list_funcionarios[2]) # ("dona_mariquinha", 10000, "dona da empresa")
```

# Dicionario

A estrutura de dados chamada de dicionario no Python também é extremamente popular. Ela como a tupla guarda elementos que devem ser processadas, manipuladas, enviadas juntos. A diferença é que ela te permite guardar o valor e o nome da variavel que esse valor pertence.


## Construindo um dicionario

Para construir um dicionario usa-se as chaves {}. Dentro das chaves é necessario informar um  nome seguido de dois pontos e o valor que essa variavel deve assumir. Os pares de chave-valores do dicionario, conjunto de nome da variavel e valor, devem ser separados por virgulas. Veja o exemplo

```python
dicionario_empregado = { "nome"    : "joao", 
                        "salario"  : 100000, 
                        "profissao":"engenheiro"}
```

## Acessando os elementos do dicionario

Para acessar os elementos do dicionario deve-se escrever entre parenteses o nome da chave do valor que gostaria de retorar. Veja o exemplo 2

```python
print(dicionario_empregado["nome"])
```


Existe outras formas de descompatar os dados das tuplas, listas e dicionarios que você construir. Mas iremos deixar esses outros metodos para o modulo intermediario.