---
title: "Passando parametros para uma funcao"
date: 2020-01-31T00:14:11-03:00
draft: false

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Passando parametros para uma função, variaveis + funções" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "Como passar argumentos numa função do Python" # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.

---


# Mais sobre funções, funções com argumentos

Nesse post iremos ver como passar argumentos para funções e dentro delas lidar com uma serie de estados. Esse post é uma combinação dos posts passados. Para melhor entender de uma olhada neles. Nos post passados vímos como definir uma função mais no sentido de agrupar uma série de comandos. Em outro vimos como construir, definir, variaveis no Python.  Nesse tutorial vamos ver como passar variaveis para dentro dos escopos das funções.

Existem duas formas de passar estados, variaveis, para uma função. Uma delas é acessando as variavies pelo escopo e a outra forma é passando como argumento de uma função. As duas formas são validas porem hoje em dia com o aumento da popularidade de testes unitarios e do paradigma de programação funcional tem se preferido usar o método de passar as variaveis para a função atravéz de seus argumentos. Iremos ver os dois métodos por que no post de controladores de fluxo usaremos mais o método de acessar as variaveis por escopo, fique firme ai!

## Passando valores a partir dos argumento em uma funcao
Como estamos nesse post falando de acessar variaveis de um função a forma mais segura, com menos chances de introduzir problemas, mais fácil de testar de forma unitária, veja o post sobre testes automáticos, é a partir de passar as variaveis por argumentos da função. Isso não é novo para você q esta acompanhando os tutoriais, já fizemos isso nos post passados quando nós passavamos uma variavel para a função print imprimir na tela um certo texto.

Para construir uma função que permite a passagem de argumentos no python basta espeficar os parametros entre virgula na definição da função. Por exemplo, vamos construir, no código 1, a função que soma dois numeros e retorna o valor dessa soma.

```python
def soma_dois_numeros(numero_1, numero_2):
    soma = numero_1 + numero_2
    return soma # retunr é a palavra privada do python que permite retornar um valor da função

soma = soma_dois_numeros(10, 20) # passando o valor 10 e 20 como parametros para a funcao soma_dois_numeros 
print(soma) # imprimir na tela o valor da soma
# 30
```
A diferença na sintaxe das funções que construimos no primeiro modulo é que agora escrevemos as variaveis entre paranteses. Outra coisa que ainda não tinhamos falado a respeito é a palavra reservada que retorna valores a: *return*. Existe formas de retornar mais de um parametro usando essa palavra. Porém, só iremos falar dela depois de estudarmos estruturas de dados.

# Acessando variavies em escopos pais.


## O escopo global
Acessando variaveis dentro da função a partir do seu escopo. Como falamos anteriormente é possivel acessar as variaveis do escopo pai dentro de um escopo filho. O escopo mais próximo do espaçamento 0, que é mais hierarquico, é chamado de escopo global. Modificar o valor das variaveis globais dentro de um função é algo extremamente desencorajado no Python. Tanto, que para isso funcionar, apenas nesse escopo, é necessário usar a palavra reservada: *global*. Como veremos no código 3. Isso acontee porque é possivel introduzir muito bugs escrevendo códigos dessa forma.


```python
soma = 0

def soma_dois_numeros(numero_1, numero_2):
    global soma
    soma = numero_1 + numero_2

print(soma)



```

## Outros escopos

É possivel acesar as variaveis dentro de um escopo mais expecifico. Basta chamar pela variavel nesse escopo mais interno:

```python
# codigo ditatico
def soma_dois_numero(numero_1, numero_2)
    soma = numero_1 + numero_2
    def duplica():
        return soma * soma

    numeros_somados = soma(numero_1, numero_2)
    return numeros_somados
```


Outra forma de construir escopos e que fara muito mais sentido acessar as variavies é os operadores de controladores de fluxo que veremos no proximo post.
