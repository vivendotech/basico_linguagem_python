---
title: "IF, ELSE, IF ELSE, estruturas de decisão"
date: 2020-01-31T00:14:11-03:00
draft: false

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Estruturas de decisão do python, if, else" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "If no python, if-else no python, estruturas de decisão no python" # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.
---


# Estruturas de decisão no python

As estruturas de decisão controlam quais escopos de códigos serão executados. Você define estruturas de decisão no python atravéz das palavras reservadas :*IF*, *ELSE*, *ELIF*. Cada vez que você usa uma dessas palavras reservadas, assim como funções, você delimita, constroi, novos escopos. Diferente das funções os escopos aqui não possuem um nome, ele são anonimos. Outra diferença é que o escopo construido pode ser executado ou não. Isso é definido controlado conforme o valor recebido por essa palavra. Por isso que essas palavras reservadas recebom o nome de controladores de fluxo

# A declaração IF
A palavra reservada *if* (traduzida para portugues como se) controla o fluxo de execução do código. Caso o if seja acompanhado da variavel boolena True ele executa o código que esta dentro de seu escopo, codigo 1. Caso o if seja acompanho da variavel boleanda False ele não executa o que esta dentro do escopo. Variaveis booleanas podem ser construidas com as palavras reservadas True ou False. Elas também podems er construida por operações lógicas, como veremos no proximo post. Isso porque uma coisa é como elas afetam a estrutura de execução e outra como elas podem ser calculadas. Aqui tenha em vista que caso algo seja verdadeiro ele executa o bloco de códigos caso seja falso ele pula todo esse escopo.


```python
# codigo 1
if True:
    print("bloco de códigos caso a condição seja verdadeira")
```

```python
# Codigo 2
if False:
    print("Essa linha de códigos não sera executada")
```


## A declaração IF ELSE

Outra forma bastante usual de usar a declação *if* é seguida da declaração *else* (outro). Nessa combinação de if else é para quando você quer executar um pedaço de código caso seja verdadeiro e outro caso for falso. Esses dois escopos estão intimamente relacionados. Por exemplo, você quer executar um pedaço de código caso um usuário seja encontrado em seu banco de dados e outro pedaço de código caso isso não seja. Como no if essa declaração funciona do if seguido de uma variavel booleana *True* ou *False*. No codígo 3 vemos o uso do if else.

```python
# bloco 3 a
# caso algo seja verdadeiro seguir um fluxo caso falso seguir outro fluxo
if True:
    print("bloco de códigos caso a condição seja verdadeira")
else:
    print("bloco de código caso a condição seja falsa")

# bloco de códigos caso a condição seja verdadeira

# bloco 3 b
if False:
    print("bloco de códigos caso a condição seja verdadeira")
else:
    print("bloco de código caso a condição seja falsa")

# bloco de código caso a condição seja falsa
```




# A declaração IF ELSIF
E a declaração if elsif é para quando você quer testar mais de uma condição. Como nos outros casos a execução dos blocos de códigos construidos dependem de o valor ser True ou False. Aqui nessa declaração a primeira hipotese testada sempre é a do IF. Se ela for verdadeira ela executa o primeiro bloco de códigos e pula o resto deles. Caso ela seja falsa ela testa a segunda hipotese, definida depois da palavra *elif*. Se essa expressão for verdadeira ele executa o bloco de códigos. Caso seja falso ele vai para a proxima declaração e se repete o processo. Geralmente a ultima opção construida é usando a palavra reservada else. Isso para que execute algo caso nada seja verdadeiro. Vamos aqui ver um exemplo usando o operador de igualdade do python (==). No proximo post veremos mais sobre operadores lógicos. No código 4, usamos a expressão if elsif. Nesse explo usando o operador de igualdade. Por enquanto, veja que o operador de igualdade testa se os valores são iguais e retorna uma variavel boleana.


```python
# codigo 4
nome = "João"
if nome == "joão": # nome é igual a joão ? Caso sim ele executa essa linha de código
    print("bloco de códigos caso o nome seja igual a joão")
elif nome == "zezinho": # o nome é igual ao zezinho ? Caso sim ele executa essa linha de código
    print("bloco de código caso o nome seja igual a zezinho")
elif nome == "luluzinha": # O nome é igual a luluzinha ? Caso sim ele executa essa linha de código
    print("bloco de código caso o nome seja igual a luluzinha")
else: # Caso nada seja verdadeiro executa essa linha de código.
    print("bloco caso nenhum nome seja verdadeiro")

# bloco de códigos caso o nome seja igual a joão
# mude o valor da string do nome para executar o bloco de código da luluzinha.

```


No próximo post veremos sobre operadores lógicos. Que permitem junto ao controle de execução de blocos construir logicas mais interessantes.
