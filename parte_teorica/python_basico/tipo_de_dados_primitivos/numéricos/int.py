'''
INT

Os números do tipo `int` em Python representam os números inteiros (positivos, negativos ou zero).

Diferente de muitas linguagens como C ou Java, o `int` em Python não tem um tamanho fixo (como 32 ou 64 bits).  
Ele cresce automaticamente conforme a necessidade, sendo limitado apenas pela memória disponível do sistema.

Com `int`, podemos utilizar todos os operadores aritméticos normalmente (+, -, *, /, //, %, **),  
e ainda podemos usar diversas funções da linguagem para operações matemáticas específicas, como fatorial, por exemplo.  
Para mais detalhes, veja o arquivo de funções para operações.

Veja na prática:

'''

print(type(1 + 1))

'''
Uma observação é que em operações com outros tipos numéricos (float), o resultado pode mudar de tipo 
(ex: virar float se houver divisão normal).

Veja:
'''

#EXEMPLO 1:

a = 5       # int
b = 2.0     # float

resultado = a + b
print(resultado)         # 7.0
print(type(resultado))   # <class 'float'>

#Nesse caso acima, teríamos que fazer a coerção

#EXEMPLO 2:

x = 10      # int
y = 4       # int

divisao = x / y
print(divisao)           # 2.5
print(type(divisao))     # <class 'float'>

#Para que a divisão acima resultasse em um int, deveráimos fazer:

divisao = x // y
print(divisao)           # 2 
print(type(divisao))     # <class 'int'>
