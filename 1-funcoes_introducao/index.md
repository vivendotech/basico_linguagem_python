---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: false

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Como construir funções, e como construir funções em Python" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "Funções em python, Introdução a funções em python" # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.

---

# Funções, agrupando uma série de instruções em um verbo.

O interpretador de python consegue entender uma série de palavras reservadas, que possuem um significado pré definidio (e.g. if, for, class, que iremos ver em outros tutorias) e regras que determinam a sintaxe da linguagem, ou seja, a forma de construir frases que façam algum sentido para o interpretador.

Uma regra muito importante no Python é de construção de verbos. Nessa construção de verbos, é necessário agrupar uma série de comandos. 

# Construindo palavras que podem ser invocadas (functions)

Por exemplo, um comando, palavra que pode ser invocado, já criado pela biblioteca padrão do python e ó de escrever uma certa palavra, numero, estrutura, na tela, o vulgo: * print *. O print é um palavra que pode ser chamada (do ingles, Callable). E ela é invocada, chamada, quando adicionamos os paranetes (i.e., letras ()) no final dela. Por exemplo, queremos invocar ela digitamos:

```python
print()
# nada parece ter executado
```
Parece que nada foi executado, por que nada foi impresso na tela. Isso aconteceu por causa que nenhum parametro foi passado para essa função, verbo. Para passar um argumento, que ja ja veremos o que isso significa, a essa invocação passamos dentro dos parenteses. Por exemplo:

```python
print("taca le pau")
# taca le pau
```

Existem varios tipos de variaveis que podemos passar como argumentos para uma ação, veremos sobre variaveis no proximo post.

# Como construir uma palavra reservada que pode ser invocada (function).

Para construir uma palavra reservada que pode ser invocada usamos a palavra reservada do python chmada de **def**. Para finalizar a definição devemos colocar parenteses (o sinal ()) e dois pontos (o sinal :) no fim da palavra construída. Por exemplo, vamos criar a função chamada de: taca_le_pau.:

```python
# def nome_funcao():
def taca_le_pau():
# veja que nao se pode ter espacos entre as palavras no python, ele só aceita uma palavra. Geralemente se usa o underline para separar palavras
```

Informamos, então, que queriamos definir a palavra "taca_le_pau" (taca le pau) agora devemos informar o que ela deve significar. O que ela significa, ou em outras palavras faz, é definido dentro dela. Para o Python saber que definições estão dentro da palavra construída ou fora dela ele usa a identação. A identação é feita quando você aperta a tecla tab do teclado. O ambiente de desenvolvimento converte o tab em 4 espaços em braco. O Python é extremamente dependente da identação do código por isso a importancia de possuir um editor de texto compatível.

 Por exemplo, vamos definir que taca_le_pau é a função que mostra na tela a frase:- "marco deve taca le pau no carrinho".

```python
def taca_le_pau():
    print("Marco taca le pau no carrinho")
```

Após construir a definição para invocar essa função digitamos o nome seguido de parentesis para invocar ela.

```python
taca_le_pau()
# saida: "Marco taca le pau no carrinho"
```

Podemos passar uma série de ações dentro do escopo da função, parte que pertence a função. Uma vez que a indentação termina, volta a sua quantidade anteiror, o Python determina o fim do escopo dessa função.

```python
def taca_le_pau():
    print("Marco taca le pau no carrinho")
    print("Mas há marco véio")
# fim da função taca_le_pau

taca_le_pau() #invocando a palavra taca_le_pau
#saida: Marco taca le pau no carrinho
#saida: Mas há marco véio
```

O que a função significa ou faz está guardada dentro do escopo dela. Uma vez construida as funções, a forma com que elas fazem isso podem ser abstraidas. Por exemplo, não sabemos como a função **print** funciona, só sabemos que ela mostra na tela um texto. Quando usamos ela apenas precisamos saber isso. Programar, é você construir cada vez mais abstrações que vão encapsulando, juntando ações. E usando essas definições para atingir mais funcionalidades. Programar é o ato de ir construindo definições nas quais você as utiliza para construir mais definições. E no ato de compor essas definições cada vez construir um sistema que realiza ações mais complexas, mais emaranhadas. Como por exemplo, um sistema bancário.





# Estruturas de dados.

# Controladore fluxo

# Controladores de repetição

# Importando modulos da biblioteca padrão


# Importando modulos construido na comunidade.


# Construindo um software simples.



# Proximo mundo é explorar o python, no paradigma de programação orientada ao objeto.



Os escopos determinam o que está dentro e fora de um função. Assim com que espaço as definições estão construidas e aonde elas podem ser invocadas. Por exemplo, uma função definina no esco global pode ser invocada por qualquer função







