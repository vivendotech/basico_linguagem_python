---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Descricao que vai no card" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "a, b, c" # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.

---

<!-- ### Novo post -->
# Escopo

O escopo no Python é determinado pela identação que as declarações são feitas. O escopo global é quando os códigos não possuem nenhum espaço na linha, ou seja a identação é de 0 espaços. Por exemplo:

```python
def funcao_a_que_esta_no_escopo_global():
    pass # palavra reservada que não faz nada.
# fim da função do escopo global
```

## Escopos dentro de escopos (nested functions)

Dentro dos escopos podemos criar novos escopos. Por exmeplo:
```python

def funcao_a_que_esta_no_escopo_global():
    def funcao_1_no_escopo_da_funcao_a():
        pass
    # fim do escopo da função 1
    def funcao_2_no_escopo_da_funcao_a():
        pass
    #fim do escopo da função 2
# fim da função do escopo global
```

Quando os os escopos estão dentro de escopos esses escopos estão aninhados (a palavra fica no sentido dos escopos estarem entrelacados).Podemos construir uma quantidade infinitas de escopos dentro de escopos.

```python
def funcao_a_que_esta_no_escopo_global():
    def funcao_1_no_escopo_da_funcao_a():
        def funcao__no_escopo_da_funcao_1_no_escopo_da_funcao_a():
            pass
        # fim do escopo da funcao 1 que esta drendo da função a
    # fim do escopo da função 1

    def funcao_2_no_escopo_da_funcao_a():
        pass
    # fim do escopo da funcao 2 que esta dentro da função a
# fim do escopo da função global
```


# Hirarquia dos escopos.

Os escopos constroem uma hierarquia. Definições em escopos mais hierarquicos, mais próximos do global, podem ser usados, invocados, em escopos menos hierarquicos. Mas o inverso não pode ser feito. Ou seja, dentro de uma função que está em um escopo X, menos hierarquico que o global, pode acessar uma função definida no escopo global. Mas a definições feitas dentro desse escopo não podem ser usadas no escopo global. Vamos ver um exemplo. Vamos definir duas funções

```python
def taca_le_pau():
    print("Marco taca le pau no carrinho")
    print("Mas há marco véio")
```

A funçao taca le pau que quando ezecuta mostra 2 linhas de texto, como mostrada no codigo..

```python
taca_le_pau()
# Marco taca le pau no carrinho
# Mas há marco véio
```


Construindo uma função que define outra função dentro de seu escopo e que invoca a função *taca_le_pau* dentro dela.


```python
def taca_le_pau_marco_veio():

    def no_morro():
        print("La vem o marcus")
        print("Descendo o morro da ??dona oscelina??")
    
    no_morro()
    taca_le_pau()
```


Agora vamos invocar essas funções no escopo global.

```python
taca_le_pau()
#"Marco taca le pau no carrinho"
#"Mas há marco véio"

taca_le_pau_marco_veio()
#La vem o marcus
#Descendo o morro da ??dona oscelina??
#"Marco taca le pau no carrinho"
#"Mas há marco véio"


no_morro()
# Vai acusar um erro nessa linha, que ele nao encontrou a função.

```


O escopo global te ajuda a controlar o acesso de uso de certas funções e variaveis. Voltaremos a falar de funções depois de falarmos a respeito de variaveis.

