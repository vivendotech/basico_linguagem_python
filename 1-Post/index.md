# Funções, agrupando uma série de instruções em um verbo.

O interpretador de python consegue entender uma série de palavras reservadas, que possuem um significado pré definidio (e.g. if, for, class, que iremos ver em outros tutorias) e regras que determinam a sintaxe da linguagem, ou seja, a forma de construir frazes que fação algum sentido para o interpretador.

Uma regra muito importante no Python é a que constroi verbos. Nessa construção de verbos, é necessário agrupar uma série de comandos comandos. 

# Construindo palavras que podem ser invocadas (functions)

Por exemplo, um comando, palavra que pode ser invocada, já criado pela biblioteca padrão do python e ó de escrever uma certa palavra, numero, estrutura, na tela, o vulgo: * print *. O print é um palavra que pode ser chamada (do ingles, Callable). E ela é invocada, chamada, quando adicionamos os paranetes (i.e., letras ()) no final dela. Por exemplo, queremos invocar ela digitamos:

```
print()
# nada parece ter executado
```
Parece que nada foi executado, por que nada foi impresso na tela. Isso aconteceu por causa que nenhum parametro foi passado para essa função, verbo. Para passar um argumento, que ja ja veremos o que isso significa, a essa invocação passamos dentro dos parenteses. Por exemplo:

```
print("taca le pau")
# taca le pau
```

Existem varios tipos de variaveis que podemos passar argumentos para uma ação, veremos sobre variaveis no proximo post.

# Como construir uma palavra reservada que pode ser invocada (function).

Para construir uma palavra reservada que pode ser invocada usamos a palavra reservada do python chmada de **def**. A palavra reservada que pode ser invocada vem em seguida e para finalizar a definição devemos colocar parenteses (o sinal ()) e dois pontos (o sinal :) Por exemplo, vamos criar a função chamada de  taca le pau.:

```python
# def nome_funcao():
def taca_le_pau():
# veja que nao se pode ter espacos entre as palavras no python, ele só aceita uma palavra. Geralemente se usa o underline para separar palavras
```

Informamos, então, que queriamos definir a palavra "taca_le_pau" (taca le pau) agora devemos informar o que ela deve significar. O que ela significa, ou em outras palavras faz, é definido dentro dela. PAra o python saber que definições estão dentro da definição ou fora dela ele usa a identação. A identação é feita quando você aperta a tecla tab. O ambiente de desenvolvimento converte o tab em 4 espaços em braco. O Python é extremamente dependente da identação do código por isso a importancia de possuir um editor de texto compativel.

 Por exemplo, vamos definir que taca_le_pau é a função que mostra na tela a frase:- "marco deve taca le pau no carrinho".

```python
def taca_le_pau():
    print("Marco taca le pau no carrinho")
```

Para invocar esa função digitamos o nome seguido de parentesis para invocar ela.

```
taca_le_pau()
# saida: "Marco taca le pau no carrinho"
```

Podemos passar uma série de ações dentro do escopo da função, parte que pertence a funcao. Uma vez que a indentação termina, volta a sua quantidade anteiror, o python determina o fim do escopo dessa função.

```python
def taca_le_pau():
    print("Marco taca le pau no carrinho")
    print("Mas há marco véio")


taca_le_pau() #invocando a palavra taca_le_pau
#saida: Marco taca le pau no carrinho
#saida: Mas há marco véio
```

O que a função significa ou faz está guardada dentro do escopo dela. Uma vez construida as funções, a forma com que elas fazem isso podem ser abstraidas. Por exemplo, não sabemos como a função **print** funciona, só sabemos que ela mostra na tela um texto. Quando usamo ela apenas precisamos saber isso. Programar, é você construir cada vez mais abstrações que vão encapsulando, juntando ações. E usando essas definições para atingir mais funcionalidades. Programar é o ato de ir construindo definições nas quais você as utiliza para construir mais definições. E no ato de compor essas definições cada vez construir um sistema que realiza ações mais complexas, mais emaranhadas. Como por exemplo, um sistema bancario.


<!-- ### Novo post -->
# Escopo

O escopo no Python é determinado pela identação que as declarações são feitas. O escopo global é quando os códigos não possuem nenhum espaço na linha, ou seja a identação 0 espaços. Por exemplo:

```python
def funcao_a_que_esta_no_escopo_global():
    pass # palavra reservada que não faz nada.

```

## Escopos dentro de escopos (nested functions)

Dentro dos escopos podemos criar novos escopos. Por exmeplo:
```python

def funcao_a_que_esta_no_escopo_global():
    def funcao_1_no_escopo_da_funcao_a():
        pass

    def funcao_2_no_escopo_da_funcao_a():
        pass
```

Quando os os escopos estão dentro de escopos esses escopos estão aninhados (a palavra fica no sentido dos escopos estarem entrelacados).Podemos construir uma quantidade infinitas de escopos dentro de escopos.

```python
def funcao_a_que_esta_no_escopo_global():
    def funcao_1_no_escopo_da_funcao_a():
        def funcao__no_escopo_da_funcao_1_no_escopo_da_funcao_a():
            pass

    def funcao_2_no_escopo_da_funcao_a():
        pass
```


# Hirarquia dos escopos.

Os escopos constroem uma hierarquia. Definições em escopos mais hierarquicos, mais próximos do global, podem ser usados, invocados, em escopos menos hierarquicos. Mas o inverso não pode ser feito. Ou seja, dentro de uma função que está em um escopo X, menos hierarquico que o global, pode acessar uma função definida no escopo global. Mas a definições feitas dentro desse escopo não podem ser usadas no escopo global. Vamos ver um exemplo. Vamos definir duas funções

```python
def taca_le_pau():
    print("Marco taca le pau no carrinho")
    print("Mas há marco véio")

def taca_le_pau_marco_veio():

    def no_morro():
        print("La vem o marcus")
        print("Descendo o morro da ??dona oscelina??")
    
    no_morro()
    taca_le_pau()

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

Isso te ajuda a controlar o acesso de uso de certas funções e variaveis. Voltaremos a falar de funções depois de falarmos a respeito de variaveis.



# Variaveis


# Mais sobre funções, funções com argumentos


# Estruturas de dados.

# Controladore fluxo

# Controladores de repetição

# Importando modulos da biblioteca padrão


# Importando modulos construido na comunidade.


# Construindo um software simples.



# Proximo mundo é explorar o python, no paradigma de programação orientada ao objeto.



Os escopos determinam o que está dentro e fora de um função. Assim com que espaço as definições estão construidas e aonde elas podem ser invocadas. Por exemplo, uma função definina no esco global pode ser invocada por qualquer função







