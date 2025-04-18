'''
FATIAMENTO DE STRINGS

Sabemos que strings em python são iteraveis. Com isso, podemos utilizar o fatiamento

O fatiamento pega uma fatia da sua string (uma letra, por exemplo) para isso, usamos a 
seguinte estrutura: [i:f:p], onde no “i” colocamos o índice da string que vamos iniciar o 
fatiamento e “f” colocamos o índice da string que vamos finalizar o fatiamento e o ”p”, 
onde nós colocamos o passo que é de quantos em quantos caracteres ele vai andar (1 em 1, 2 em 2..) 
(caso não coloquemos o “p” ele vai de um em um por padrão). Caso não coloquemos o índice que vamos 
finalizar o fatiamento, ele continua até o final da string
'''

variavel = 'Nicolas'

print(variavel[0]) #Aqui estamos fatiando e pegando a primeira letra, a letra de indice 0 ('N')

print(variavel[3:7]) #Aqui estamos fatiando e pegando a letra de indice 3 ('o') até a a letra de indice 7 ('s')

print(variavel[2::]) #Aqui começamos o fatiamento na letra de indice 2 ('c') e fomos até o final

print(variavel[::2]) #Aqui fizemos fatiamento da primeira letra e fomos até o final usando 2 como 'p'


'''
Uma observação MUITO IMPORTANTE é que podemos utilizar indices negativos para fatiar a nossa string
também. O indice -1 em uma string, por exemplo, se refere a última letra da string e é muito útil
quando temos strings que não sabemos como são e queremos acessar sua última letra. Veja:
'''

print(variavel[-1]) #Aqui estamos acessando a última letra da string 

print(variavel[-7]) #Aqui estamos acessando a primeira letra da string

'''
Inclusive, se colocarmos o 'p' (passo) como sendo -1 e começarmos do começo da string, podemos 
inverter a nossa string. Veja:
'''

print(variavel[::-1]) #Começamos do começo da string e utilizamos -1 como passo, logo,
# a primeira letra será -1 (que sabemos que é 's') e irá diminuindo até chegar a -7 (letra 'N')