'''
Uma coisa EXTREMAMENTE IMPORTANTE em qualquer linguagem de programação de um modo geral é a utilização da lógica. Para isso, nós temos nas linguens a inclusão de 
operadores lógicos. Dentre eles:

→ and :

'and' significa “e”, então quando utilizamos esse operador, precisamos de mais de uma coisa para ser verificada. Exemplo: uma condição E outra condição
Além disso, no 'and', TODAS as condições precisam ser verdadeiras para retornar True. Se uma condição for falsa, ele retorna a condição naquele valor (False)

→ or :

Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor (True)

→ not : 

É o operador que serve para inverter expressões. O que for false vira true e  o que for true vira false


→ in e not in :

In significa 'está entre' e not in significa 'não está entre'. são usados para verificar se um valor está contido (ou não) dentro de uma sequência ou coleção, 
como strings, listas, tuplas, dicionários, conjuntos, etc.

'''

#VEJA ALGUNS EXEMPLOS:


# and:

print(10 == 4 and 3==3) #False
print(10 == 10 and 3 ==3) #True

# or

print(10==2 or 10==10) #True
print(10 == 2 or 10 ==3) #False

# not

print(not 10 == 2) #True
print(not 10 == 10) #False

# in e not in:

print('n' in 'nicolas') # True
print('g' in 'nicolas') #False