'''
FATIAMENTO DE LISTAS e TUPLAS

Já vimos a forma como podemos acessar elementos de uma lista e de tuplas, mas você sabia que
temos fatiamento de listas e tuplas ? Lembrando que fatiamento (ou slicing) é uma forma de 
pegar uma fatia de algo, uma parte de algo. Nesse caso, pegaremos uma parte de listas ou
tuplas

Para fazer o fatiamento seguimos a seguinte estrutura: [i:f:p], onde no “i” colocamos o 
índice da lista ou tupla que vamos iniciar o fatiamento e “f” colocamos o índice da lista ou tupla que vamos finalizar 
o fatiamento (uma observação é que no f, temos que botar o indice + 1 para o elemento que queremos incluir. 
Exemplo: Quero incluir o elemento de indice 2 no fatiamento. Temos que colocar o 'f' como sendo 3) o ”p”, onde nós 
colocamos o passo que é de quantos em quantos elementos ele vai andar (1 em 1, 2 em 2..) (caso não coloquemos o “p” 
ele vai de um em um por padrão). Caso não coloquemos o índice que vamos finalizar o fatiamento, ele continua até o final 
da lista

Dessa forma, em resumo:

- início: o índice onde o fatiamento começa (inclusivo).
- fim: o índice onde o fatiamento termina (**exclusivo**, ou seja, o elemento nesse índice não é incluído).
- passo: de quantos em quantos elementos vamos andar. Se omitido, o padrão é 1.

Se omitirmos o início, ele começa do início da sequência.
Se omitirmos o fim, ele vai até o final da sequência.

Veja na prática
'''

lista = ['Nicolas', 'José', 'Maria', 'João', 'Pedro', 'Carlos', 'Neto']

print(lista[0:3:1])  #Irá retornar: ['Nicolas', 'José', 'Maria']

print(lista[0:5:2]) #Irá retornar ['Nicolas', 'Maria', 'Pedro'] 

print(lista[3:6]) # Irá retornar ['João', 'Pedro', 'Carlos'] --> não incluiu o elemento de indice 6. Para incluir: f = 7


tupla = ('Maria', 'Ana', 'Madalena', 'Cris')

print(tupla[0:3:1]) #Irá retornar ('Maria', 'Ana', 'Madalena')

print(tupla[0:5:2]) #Irá retornar ('Maria', 'Madalena')

'''
No arquivo de conceitos de lista, já chegamos a comentar que podemos acessar itens da lista utilizando indices negativos. 
Agora, no fatiamento, uma observação é que podemos ter fatiamentos de trás para frente, usando um passo negativo.

Quando usamos um passo negativo, a leitura é feita de trás para frente, ou seja, os índices precisam ser ajustados 
ao contrário. Sendo assim em uma lista que tem 6 elementos, o último item dela teria indice -1 e o primeiro teria indice
-6 

Veja na prática:
'''

print(lista[::-1]) # Inverte toda a lista: ['Neto', 'Carlos', 'Pedro', 'João', 'Maria', 'José', 'Nicolas']

print(lista[-2:-5:-1]) # ['Carlos', 'Pedro', 'João'] (começa do -2)

print(lista[-1:-6:-2])  # ['Neto', 'Pedro', 'Maria']


'''
Podemos ainda misturar: Colocar passo negativo e manter os indices possitivos.

Veja abaixo:
'''


print(lista[5:2:-1]) # ['Carlos', 'Pedro', 'João'] (começa do 5 e vai té o 2 (lembre que o elemento de indice f não é incluido))

print(lista[6:1:-2])  # ['Neto', 'Pedro', 'Maria'] (começa do 5 e vai té o 1 (lembre que o elemento de indice f não é incluido))