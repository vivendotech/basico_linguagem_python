---
title: "Importando bibliotecas usando PIP"
date: 2020-01-31T00:14:11-03:00
draft: false

article: true
section: "teoria" # teoria, desafio, datasheet
descricao: "Importe todas as bibliotecas construidas pela comunidade python" # vai no seo tbm
repo: "/basico_linguagem_python"
categories: ["categoria"]
tags: ["a","b","c"] # gera uma lista de paginas para cada categoria
tags_seo: "Como usar o pip para importar bibliotecas no package manager" # tags que vai no seo
img_post: "/stes.jpg"  # img do post para as redes sociais.
---

No post passado vimos como importar bibliotecas criadas por você e as padrões no Python. Nesse veremos como importar bibliotecas indexadas pelo Python, ou seja bibliotecas construidas pela comunidade. O site que essas bibliotecas estão alocadas é na [pyPi](https://pypi.org/). A facilidade de importar biblitoecas no Pyton está no gerenciador de pacotes implementado pelo python, famoso PIP. 

# Instalando uma biblioteca do pyPi

Para instalar a biblioteca do pypi basta ir no site do [pypi](https://pypi.org/) para encontrar a biblioteca desejada. Nesse tutorial iremos instalar a biblioteca que nos auxilia a construir programas com interface de texto. O nome dessa biblioteca é dobopt. Escreva o nome dela em "search projects" (em portugues, procure projetos). Depois clique em [docopt 0.6.2 (caso queira acelerar o procesos)](https://pypi.org/project/docopt/). Bem em cima da pagina em baixo do titulo do pacote tem escrito "pip install docopt". Essa é a linha de comando para instalar essa biblioteca. Então, abra o powershell para instalar a biblioteca. Para isso clique com o botão esquerdo na tela, em qualquer pasta, e selecione "open powersheel". No powershell digite:

```powershell
pip install docopt
```
O comando padrão para instalar pacotes é "pip install algum-nome-de-pacote".

# Desinstalando bibliotecas
Para desinstalar os pacotes digite:

```
pip uninstall algum-nome-de-pacote
``` 


No ultimo tutorial dessa série iremos construir um programa usando o pacote docopt.
