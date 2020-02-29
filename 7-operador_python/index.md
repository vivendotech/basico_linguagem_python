---
title: "Operadores dos diferentes tipos"
date: 2020-01-31T00:14:11-03:00
draft: false

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Operadores nos diferentes tipos de variaveis do python" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "Operadores lógicos no python" # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.
---


Os outros tipos de variavies também possuem operadores. Alguns desses operadores inclusive podem retornar um valor boleano, como veremos a seguir. Mas, nesse post focaremos nos operadores basicos que os tipos basicos possuem. Vale ressaltar que um operador muda sua operação conforte o tipo de variavel que é passado na entrada. Em modulos mais avançados falaremos como implementar novas classes e como implementar essas funções magicas.

# Operador +
O operador + realiza diferente operações conforme o tipo da variavel que é passada como parametro. 


## Operador + entr duas variveis inteiras
O Operador + quando esta entre duas variaveis inteiras ele realiza a operação de adição
```python
var_int = 53
var_int_2 = 32
var_resultado = var_int + var_int_2 # 85
```

## Operador + entre duas variaveis flutuantes (float)
O operador + realiza a operação de soma quando é utilizado entre duas variaveis float.

```python
var_float = 53.3
var_float_2 = 32.12
var_resultado = var_float + var_float_2 # 85.42
```

## Operador + entre duas variaveis Strings
O operador + quando coloado entre duas variaveis do tipo string realiza a operação de concatenação

```python
var_string = "oi "
var_string_2 = "Mundoo"
var_string_resultado = var_string + var_string_2 # "oi Mundoo"
```


Voce pegou o espirito ?

## O operador * entre duas variaveis inteiras
O operador * quando colocado entre duas variaveis do tipo inteiro multiplica os valores

```python
var_int = 10
var_int_2 = 20
var_string_resultado = var_int * var_int_2 # 2000
```

# O operaodr * entre uma variavel inteira e uma string

O operador * entre uma variavel inteira e uma string multiplica a quantidade da variavel string e retorna uma string


```python
var_int = 2
var_string = "Oi "
var_string_resultado = var_int + var_string # Oi Oi 
```


Para ver a ação dos outros operadores siga a tabela, que sera gerada pelo pull request em nosso github.

<!-- https://rszalski.github.io/magicmethods/ -->