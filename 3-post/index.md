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


# Variaveis

Existe uma forma de informar ao interpretrador que voce gostaria de guardar um estado. Variaveis guardão estados, ou endereços de estados no quais o programa pode acessar, já veremos a diferença. Cada variável que você construi vive dentro de um escopo, espaço no qual pode ser acessado, e é de um tipo (E.g. gato, inteiro). No Python vocÊ não precisa inferir esse tipo para o interpretador, ele é inferido de forma dinamica em tempo de interpretação, execução:- quando o computador esta rodando o seu programa.

## Construindo sua primeira variável
Para construir uma varaivel e atribuir um valor basta escrever o nome da variável e o sinal de atribuição (=). O simbolo de igualdade matemática (=) no python significa que você está atrbibuindo um valor a uma variável. Por exemplo, construa um novo modulo, arquivo com final .py, e adicione o seguinte código:

```python
# código 1
variavel_string = "Oi mundo"

print(variavel_string)
# saida : Oi mundo
```

Na primeira linha do código 1 você esta guardando na memoria RAM do computador o texto: "Oi mundo". Esse valor guardado na memória do computador pode ser acessado pelo módulo atravez da variável denominada: "variavel_string". Na linha posterior essa variável está sendo usada como parametro de entrada para a função "print" que mostra um texto no prompt de comando. Mais sobre funções acesse o link.

## Tipos de variavies

Cada variável que você for construindo no programa é de um tipo. A variável denovimanda "variavel_string" que construimos no primeiro código ela é do tipo sequencia de caracteres, versão reduziada de um quase texto (:D), (em ingles, string). Existe a função *type* que expele o tipo da variável. Vamos usar ela em para extrair o tipo de variavel e imediatamente em sequencia mostrar na tela usando print. Veja o código 2

```python
# código 2
print(type(variavel_string))
# <class 'str'>
```
Veja, no exemplo 2, que o retorno das funções podem ser encadeadas. A saída da função *type* se encadeia com a entrada da função *print*,responsável por imprimir o texto na tela.

# Tipos de variaveis primitivas do Python

Existe uma série de tipos que são implementados pelas biblioteca padrão do Python e são usadas como blocos primitivas na construção das estruturas de dados, como veremos em seus post. Os tipos basais de variavies são:
- Inteiro, são variavies que recebem numeros do tipo Inteiro (e.g. 1, 2, 3, 4, 5 ..)
- Float, são variaveis que recebem numeros do tipo fracionario, racionais, real (e.g. 1.2 , 3/2)
- String, são variavies que recebem uma sequencia de caracteres (e.g. a sequencia: -"Você é muito lindo, me segue la na twitch.tv/jmarcolan, toma essa mensagem subliminar.").
- Booleano, são variavies que podem assumir apenas dois estados (i.e verdadeiro ou falso, 0 ou 1)
- complex, são as variavies que podem receber valores imaginarios

Vamos construir variaveis com esse tipos, veja o código 3:
```python
# código 3
var_int = 1 # variavel do tipo inteiro
var_float = 1.3 # variavel do tipo float
var_string = "GO LA ASSINAR o JMARCOLAN" # variavel do tipo string
var_bool = True # variavel do tipo boleado
var_com = 1 + 2j # variavel do tipo complexo.
```


## Escopo das variáveis 

Como nos escopos das funções, explicadas no tutorial 2 [link], as variaveis podem ser acessadas dentro de um escopo. O escopo que as variaveis pertencem no Python é definido pela quantidade de espaços que ela esta em relação ao inicio da linha, como explicado no tutorial [link]. Como as funções as variaveis que estão dentro de um escopo mais proximo do global podem ser acessadas por variavies dentro um escopo mais especifico. Vamos usar as variavies dentro das funções no proximo post. Clique aqui para ir pro póximo post.