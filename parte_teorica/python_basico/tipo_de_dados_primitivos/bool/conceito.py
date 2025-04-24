'''
BOOLS

Valores booleanos são importantes em praticamente todas as lingugens de programação. Eles são extramamente fundamentais para o funcionamento da linguagem, uma
vez que a partir deles, entramos em condições, loops, podemos realizar a utilização de flags e diversas outras coisas. 
Eles representam dois estados: True ou False (verdadeiro ou falso) e podem ser retornados principalmente a partir de operadores relacionais, lógicos e etc.

'''


print(type(True)) #Retornará bool

print(type(False)) #Retornará bool

'''
Uma observação é que valores de string, int, listas, tuplas e etc retornam valores booleanos também.
Isso é um ponto de atenção muito importante, principalmente se o valor booleano retornado por esses tipos de 
dados forem False (apesar de serem poucos exemplos desses tipos de dados que retornarão False), uma vez que
se o booleano for False, nós não entramos em condições, loops etudo mais. Veja abaixo os valores de cada tipo de
dados que retornam valores False:

'' --> String vazia

0 --> Zero

0.0 --> Zero float

[] --> Lista vazia

() --> Tupla vazia

None --> Não valor

range(0,0) 

'''