'''
CRIAÇÃO DE ARQUIVOS EM PYTHON

Em python, podemos fazer várias coisas e, com certeza, uma das mais interessantes delas
é a abertura manipulação de arquivos. Por enquanto, vamos ver a parte de abertura. A parte de 
manipulação nós veremos em detalhes mais afrente. 

Para realizar a abertura do arquivo, temos que especificar primeiro onde queremos que esse arquivo
seja aberto. Existem 2 duas formas

# 1: Caso queiramos abrir o arquivo na mesma pasta que estamos:

caminho_arquivo = 'arquivo.txt'


# 2: Caso queiramos ser especificos (o que é o ideal) ou caso queiramos abrir o arquivo em outra pasta

caminho_arquivo = 'C:\\Users\\nicol\\OneDrive


OBS: Uma observação é que esse caminho que eu criei está no formato do windows, por isso as barras estão
invertidas ('\') e não normais ('/'). Além disso, esse caminho vai variar de computador para comutador o
obviamente

A partir disso, nós faremos:

arquivo = open(caminho_arquivo, 'modo') --> Explico sobre o que é esse 'modo' em #1

arquivo.close() --> Esse .close() é MUITO importante. Explico em #2


Certo, agora temos vários pontos para abordar:

#1 'Modos':

No lugar de de 'modo', nós basicamente botaríamos "o que queremos fazer com o arquivo". Os principais
modos e suas funções são:

--> 'w': Serve para escrita em arquivos

--> 'r': Serve para leitura de arquivos

--> 


#2 .close():

Algo muito importante de se falar é que SEMPRE que abrirmos um arquivo, nós temos que fechá-lo, pois
caso não seja feito, isso poderá nos gerar problemas. Portanto, sempre que você utilizar o open(),
utilize o .close() no final. Mais para frente, ainda neste arquivo, veremos sobre algo chamado 
with open(), que abre o arquivo e fecha ele automaticamente

Certo, agora, sabendo de tudo isso abriremos o nosso arquivo da seguinte forma:


OBS: Como estamos abrindo o arquivo pela primeira vez, nós meio que vamos "criar" o arquivo, portanto
os modos que podemos utilizar são: ... É importante pontuar que nós NÃO PODEMOS utilizar o modo 'r' 
de primeira, porque o arquvio nem foi criado, então se utilizarmos o 'r' de primeira, dará um erro de
FileNotFoundError
'''



'''
USANDO CONTEXT MANAGER WITH

Agora, falaremos sobre algo chamado Context Manager, que é baciamente uma estrutura que gerencia o uso de 
recursos que precisam ser abertos e fechados corretamente, como arquivos, por exemplo.

Dessa forma, lembra quando eu falei que quando abrimos um arquivo com o open, nós precisamos fechar ele
usando o .close() em algum momento? Então, com o context manager, ele abrirá o arquivo, fará o que deve ser
feito e depois fechará automaticamente, sem que precisemos utilizar o .close(). Para usá-lo, faremos:

with open(caminho_arquivo, modo) as arquivo:
    Alguma coisa
    

'''


