'''
FATIAMENTO DE LISTAS e TUPLAS

Já vimos a forma como podemos acessar elementos de uma lista e de tuplas, mas você sabia que
temos fatiamento de listas e tuplas ? Lembrando que fatiamento (ou slicing) é uma forma de 
pegar uma fatia de algo, uma parte de algo. Nesse caso, pegaremos uma parte de listas ou
tuplas

Para fazer o fatiamento seguimos a seguinte estrutura: [i:f:p], onde no “i” colocamos o 
índice da lista ou tupla que vamos iniciar o fatiamento e “f” colocamos o índice da lista ou tupla que vamos finalizar 
o fatiamento e o ”p”, onde nós colocamos o passo que é de quantos em quantos elementos ele vai andar (1 em 1, 2 em 2..) 
(caso não coloquemos o “p” ele vai de um em um por padrão). Caso não coloquemos o índice que vamos 
finalizar o fatiamento, ele continua até o final da lista

Veja na prática
'''

lista = ['Nicolas', 'José', 'Maria', 'João', 'Pedro']

print(lista[0:3:1])  #Irá retornar: ['Nicolas', 'José', 'Maria']

print(lista[0:5:2]) # Irá retornar ['Nicolas', 'Maria', 'Pedro']


tupla = ('Maria', 'Ana', 'Madalena', 'Cris')

print(tupla[0:3:1]) #Irá retornar ('Maria', 'Ana', 'Madalena')

print(tupla[0:5:2]) #Irá retornar ('Maria', 'Madalena')