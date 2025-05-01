'''
MODULOS

Modulos são basicamente arquivos que possuem código Python (funções, variáveis..), onde podemos importar esse arquivo 
(com todas as suas funções, variaveis..) e utilizar em outro código, facilitando muito nosso trabalho. O python tem 
muitos módulos por padrão (conhecidos também como modulos internos ou builtin), onde não precisamos instala-los para 
usá-los. Inclusive, quando um módulo começa a fazer muito sucesso, eles incluem ele na linguagem. Dessa forma, a 
linguagem tem muita coisa por padrão (builtin)

Aqui, falaremos somente sobre a importação dos modulos e seus detalhes

--> Para importar um modulo, nós fazemos: import nome_modulo

Fazendo isso acima, nós importamos o modulo INTEIRO. Se quisermos, podemos importar apenas partes do modulo.
Mas como assim partes do modulo?

Como dissémos, um modulo é basicamente um arquivo que possui código python, como funções e variaveis, por exemplo, 
então, se quisermos, podemos importar apenas funções ou variaveis especificas de um modulo especifico. 

--> Para importar partes de um modulo, nós fazemos: from nome_modulo import elemento1, elemento2..

Uma observação importante é que :importar módulos, seja eles inteiros ou uma parte deles não muda em nada o 
desempenho do teu programa

Vamos a um exemplo:
'''

# import sys --> Aqui estamos importando o modulo sys


# from sys import exit, plataform --> Aqui estamos importando a função exit e a variavel plataform do modulo sys


'''
Uma observação é que se importamos o modulo para o nosso código da primeira forma (import sys), ou seja, o modulo 
todo, na hora que formos  utilizar a função exit, por exemplo, nós teríamos que fazer sys.exit(). Agora, se fizermos 
a importação de partes do modulo como fizemos na segunda forma (from sys import exit, plataform), quando formos 
utilizar a função exit, bastaria utilizar a função normalmente: exit(), sem colocar sys.

Uma outra observação é que a partir do que fizemos acima, no segundo modo, nós importamos o nome plataform para o 
nosso módulo, por exemplo, então, caso tentarmos criar uma variavel chamada plataform em nosso código, iremos perder 
a função plataform que foi importada. 


Algo que podemos fazer também é importar um modulo e dar um alias para ele. O alias serve para facilitar na hora de
usar os recursos do modulo. Você viu que quando importamos o modulo todo na primeira forma (import sys), quando vamos
utilizar a função exit(), temos que fazer sys.exit(), então, se o nome do modulo for muito grande, fica muito 
tabalhoso, aí compensa mais renomear o modulo

Veja um exemplo:
'''
#import sys as s --> Renomeamos o modulo sys para s

# s.exit() --> Agora, quando usamos a função exit(), não fazemos sys.exit(), mas sim s.exit(), ou seja, facilita 

# OBS: Poderíamos também  dar um alias a algo que estamos importando do modulo. Veja abaixo:

#from sys import exit as ex --> Renomeando a função exit() importada do modulo para ex

# ex() Agora, na hora de usar exit(), vamos usar ex()

'''
UMA BOA PRÁTICA

Algo que pode ser feito, mas é má prática é importar tudo do módulo fazendo: from sys import *

Isso é má prática porque: lembra que quando importamos o modulo dessa forma acima, nós não precisamos botar
o sys. antes de uma função, por exemplo. Isso pode gerar conflitos com o seu código, porque se você tiver em
seu código uma função exit definida, por exemplo, isso geraria conflito com a função exit() do modulo sys. Portanto,
quando você quiser importar todos os recursos do modulo, use import sys. Assim, não gerará conflitos, porque se 
você tiver a função exit definida no seu código e quiser utilizar a função exit() do módulo sys, bastaria fazer
sys.exit() 

'''
