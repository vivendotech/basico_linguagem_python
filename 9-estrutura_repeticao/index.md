---
title: "Laco for de repeticao"
date: 2020-01-31T00:14:11-03:00
draft: false

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Laços for de repetição" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "Como usar o for do python" # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.
---


Outra forma de construir escopos no python é usando a palavra reservada for. A palavra reservada for constroi um escopo de tal forma que o que esta dentro do escopo é repetido uma série de vezes. O jeito obvio de usar o for do python é junto a uma variavel do tipo lista de dados. Veja os tutotiaris passados para entender melhor esses conceitos. A quantidade de vezes que será repetido o escopo que o for construiu é determinado pela quantidade de elementos que tem a lista usada para construir o for.

# Como construir um laco de repetição for

Para construir o laço for é necessario escrever a palavra reservada *for* seguida de uma variavel que vai assumir, o valor de cada elemento na lista, a palavra reservada *in*, a lista que você gostaria de caminhar, iterar, atravessar e por fim os dois pontos (:) que marcam o inicio do novo escopo. Construindo nosso primeiro laço de repetição, veja o codigo 1. 


```python
# codigo 1
lista_dados = ["josue","joao","miguel","mariquinha","luluzinha"]
for elemento in lista_dados:
    print(elemento)

# josue
# joao
# miguel
# mariquinha
# luluzinha
```
Quando usamo o operador *in* do python estamos dizendo que queremos um elemento dentro dessa lista.

Para quem vem de outras linguagens a funcionalidade do for se asemelha muito ao for each (para cada). Mas no python, esse é o jeito obvio de usar esse laco de repetição. E para o python sempre o jeito obvio é o que envolve menos quantidade de código. Outra forma muito popular de usar o for é tendo junto a cada elemento da lista o valor da posição do elemento.

## Usando o enumerate do Python

O enumerate ele também é um callable como a função, mas ele tem um diferencial que ele é do tipo gerador. O que significa que além dele poder ser invocado ele retorna um valor diferente cada vez que é invocado. Iremos entrar mais a fundo a respeito de geradores no tutorial no nivel intermediario. Outra coisa que devemos saber a respeito dele é que ele permite a entrada de quaquer iterable, estrutura de dados que permite ser iterado, caminhada, rodada. O enumerate retorna um elemento do tipo iterator também. Veremos mais sobre isso quando chegarmos no proximo modulo. Por enquanto, pense que  ele retorna uma tupla (dados correlacionados como vimos no tópico passado) aonde o primeiro elemento é o index, posição do elemento na lista, e o segundo valor da tupla é a respeito do valor do elemento. Vemos um elemento.

```python
lista_dados = ["josue","joao","miguel","mariquinha","luluzinha"]
for index, elemento in enumerate(lista_dados):
    print(index, elemento)


# 0 josue
# 1 joao
# 2 miguel
# 3 mariquinha
# 4 luluzinha
```

Nesse post vimos a respeito do for. Mesclando o que aprendemos até agora que faz o mundo começar a ficar muito interessante. Antes de mergulahrmos em uma série de projetos, exercicios desse modulo. Vamos para os ultimos módulo teóricos. Os proximos modulos dissem respeito de como interar para adquirir as baterias inclusas do python os módulos e bibliotecas.