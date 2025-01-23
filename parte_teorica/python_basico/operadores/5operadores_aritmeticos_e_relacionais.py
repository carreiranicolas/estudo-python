'''
OPERADORES ARITMÉTICOS

Em python e em qualquer outra linguagem, uma coisa que bastante utilizada são os operadores artiméticos, no intuito de realizar contas e cálculos aritiméticos.

Os operadores aritméticos que nós temos são:

 + → Faz a adição entre os números

 - → faz a subtração entre os numeros

 * → Faz a múltiplicação entre os números

 ** → Faz a exponenciação dos números

 / → Faz a divisão dos números e sempre retorna um float

 // → Faz a divisão dos números e sempre retorna um int

 % → retorna o resto da divisão

 Uma observação importante a se fazer é que alguns operadores tem algumas peculiaridades. Exemplo: o operador de adição, além de somar números, faz concatenação de strings.
 Além disso, o operador de multiplicação, além de multiplicar números, pode fazer a repetição de strings .

 Uma outra observação muito importante é PRECEDENCIA DOS OPERADORES. Ela funciona da seguinte forma: A primeira coisa a ser executada são os parênteses 
 (vale lembrar que os parênteses são executados de dentro para fora), depois disso, vem a exponenciação (**) e depois temos a multiplicação (*), a divisão (/), 
 a divisão inteira (//) e o módulo (%), que são operadores de mesma precedencia e portanto são executados da esquerda para direita na ordem que vier 
 (se não tiver nenhum parenteses priorizando algum) e, por último, a soma e a subtração, que são de mesma precedencia.

'''

print(1+1) # Irá nos retornar: 2

print(2-1) # Irá nos retornar: 1 

print(2*2) # Irá nos retornar: 4

print(3**2) #Irá nos retornar 9

print(3/2) # Irá nos retornar: 1.5

print(3//2) # Irá nos retornar: 1

print (3%2) # Irá nos retornar: 1

print('o' + 'i') # Irá nos retornar 'oi'

print ('o' * 5) # Irá nos retornar 'ooooo'

'''
OPERADORES RELACIONAIS

Em python e na programação, na verdade, algo essencial são os operadores relacionais, também conhecidos como operadores de comparação.
Os operadores de comparação são usados para checar coisas (se é menor, maior e etc..), sendo que na maioria esmagadora dos casos, nós utilizamos eles
para fazer comparação entre varíaveis em condicionais ou loops. Além disso, apesar já termos visto isso em 'tipo de dados', é importante relembrar que comparadores 
nos retornam valores booleanos (True ou Falso)

Os operadores relacionais que temos são:

a > b → operador que significa maior, “a” maior que “b”

a >= b → operador que significa maior ou igual, “a” maior ou igual a “b”

a < b → operador que significa menor, “a” menor que “b”

a <= b → operador que significa menor ou igual, “a” menor ou igual a “b”

“a” == “b” → operador que significa igual, “a” igual a “b”

a != b → operador que significa diferente, “a” diferente de “b”

Uma observação rápida é que usamos dois iguais (==) no operador relacional de  “igual” porque em python, um igual (=) significa atribuição, enquanto
dois iguais significa CHECAR/COMPARAR se dois valores envolvidos são iguais

'''

print(1>2) # Irá nos retornar False

print(1>=2) # Irá nos retornar False

print(1<2) # Irá nos retornar True

print(1<=2) # Irá nos retornar True

print(1==2) # Irá nos retornar False

print(1!=2) # Irá nos retornar True