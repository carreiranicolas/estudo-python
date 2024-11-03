'''
Dentro do Python, os tipos de dados inicias (pois veremos outros posteriormente) são:

------------------------------------------------------------------------------------------------------

string (str) --> texto

Para escrever uma string, basta escrever nosso texto entre aspas duplas ("") ou aspas simples ('')

"Olá, mundo!" OU 'Olá, mundo!
-------------------------------------------------------------------------------------------------------

inteiros (int) --> números inteiros

Para escrever um número em Python, basta escrever o número normalmente, sem necessidade de aspas

123

------------------------------------------------------------------------------------------------------

ponto flutuante (float) --> números de ponto flutuante (com vírgula)

Para escrever um número com ponto flutuante, ou seja, um número com vírgula em Python, basta escrever
o número e substituir a vírugula por ponto (.)

3.14159265359
------------------------------------------------------------------------------------------------------

booleano (bool) --> só tem dois valores: True ou False

Para escrever um tipo booleano, podemos simplesmente escrever True ou False, sem a necessidade de aspas
ou também podemos escrever expressões cujo o valor possa retornar True ou False

True         False

1 +1 = 2     1 + 1 = 3

------------------------------------------------------------------------------------------------------

Um detalhe é que se quisermos verificar qual tipo de dados estamos trabalhando, basta utilizar

print(type(DADO)) e ele irá nos retornar: <class 'tipo de dado'>

'''

"Olá, mundo!"  'Olá, mundo!'

print(type("Olá, mundo!")) #Nos retorna <class 'str'>

123

print(type(123)) #Nos retorna <class 'int'>

3.14159265359

print(type(3.14159265359)) #Nos retorna <class 'float'>

True or False

print(type(True)) #Nos retorna <class 'bool'>

print(type(False)) #Nos retorna <class 'bool'>

1 + 1 == 2 or 1 + 1 == 3

print(type(1 + 1 == 2)) #Nos retorna <class 'bool'>

print(type(1 + 1 == 3)) #Nos retorna <class 'bool'>

