'''
MÉTODOS DE LISTAS

A partir dos metodos de listas, podemos fazer diversas coisas como deletar, ler valores, adicionar valores e diversas 
outras coisas 

OBS: Já vimos que para alterar um valor da lista, nós não utilizamos métodos, mas sim pegamos o valor e reatribuimos
outro valor a ele. Para ver isso melhor, vá ao arquivo de conceitos

Veja abaixo:
'''

lista = ['Nicolas']

# Método append: Adiciona o item no final da lista

lista.append('José')

print(lista) #Irá exibir ['Nicolas', 'José']

# Método insert: Insere o item que você quer em uma posição(indice) especifica  da lista

lista.insert(0,'Ana')

print(lista) #Irá exibir ['Ana', 'Nicolas', 'José']

'''
OBS: Muito cuidado ao utilizar o método insert, pois se estivermos trabalhando com listas muito grandes e inserirmos um
novo elemento nessa lista (no meio da lista, por exemplo), o que acontecerá é que todos os indices da lista serão 
remanejados para 
'''

# Método index: Nos retorna o indice da primeira aparição do item x

print(lista.index('José')) #Irá retornar o indice 2

#Metodo pop: remove da lista o elemento que colocamos o indice no pop, além de retornar o valor removido 

lista.pop(0) #Irá remover o elemento de indice 0 da lista ('Ana'), além de retornar 'Ana'

#OBS: Se não colocarmos nada no pop, remove o último elemento da lista por padrão 

#Metodo remove: remove da lista o elemento x

lista.remove('José') #Irá remover 'José' da lista

#Metodo clear: remove todos os elementos da lista

# lista.clear() --> deixará a lista vazia

#Metodo count: Conta quantas vezes o valor x aparece na lista

print(lista.count('Nicolas')) #Irá exibir 1, pois Nicolas só aparece uma vez na lista


'''
MÉTODO COPY

Para entender esse método de lista, temos que entender que estamos trabalhando com um tipo mutável, então fazer algumas 
coisas é sempre muito complicado, pois alterações podem acontecer a qualquer momento e complicar nossa vida.

Visto isso, o método copy é usado em lista quando às vezes queremos criar uma cópia da lista original para poder fazer 
alterações sem modificar a lista original.

Se tentarmos fazer, por exemplo, da seguinte forma:

lista1 = [1, 2, 3]
lista2 = lista1

Isso não dará certo, não estamos criando uma cópia da lista 1 na variavel lista2, estamos apenas criando uma nova variável
(lista2) que aponta para o mesmo local da memória que lista1.

Ou seja: qualquer alteração feita em lista2 também afeta lista1. Veja:

lista1 = [1, 2, 3]
lista2 = lista1

lista2.append(4)

print(lista1)  # [1, 2, 3, 4]
print(lista2)  # [1, 2, 3, 4]

# Ou seja, acima podemos ver que a alteração na lista2 atingiu a lista original também

Portanto, para contornar isso, se quisermos criar uma cópia independente, usamos o método copy(). Veja:

lista1 = [1, 2, 3]
lista2 = lista1.copy()

lista2.append(4)

print(lista1)  # [1, 2, 3]
print(lista2)  # [1, 2, 3, 4]

Agora sim: lista1 permaneceu intacta e lista2 foi modificada sem afetar a original.

Dessa for, o que o método copy fez foi criar uma nova lista, copiar todos os elementos da lista original para essa nova 
lista e aí as duas listas passam a ser listas separadas 

OBS: existe ainda o conceito de cópia rasa, que falaremos no módulo intermediário, mas falando de forma rápida, é quando
a lista que queremos fazer a cópia tem dentro dela outras listas dentro dela (listas aninhadas), aí o copy() não copia 
profundamente os objetos internos. Eles ainda serão compartilhados entre a lista original e a lista copiada. Sendo assim,
se alterarmos algo na lista que está dentro da original, será alterado na lista copiada!



'''


'''
Concatenação de listas (método extend e operador '+')

Suponhamos que temos uma lista A e outra lista B e queremos juntar essas duas listas em uma lista C, podemos juntar 
(concatenar) essas duas listas usando o sinal de “+”. Veja um exemplo

lista_a = [1,2,3]
lista_b = [4,5,6]

lista_c = lista_a + lista_b

print(lista_c) --> Irá retornar [1,2,3,4,5,6]

Além disso, temos o método extend --> lista_a.extend(lista_b) 

Acima, estenderemos a lista A para a lista B.  É um método que ocorre diretamente na lista A, ela não retorna 
um valor, ou seja, não podemos criar a váriavel: x = lista_a.extend(lista_b), pois o extend retornará um None (não valor), 
uma vez que é uma função que AGE DIRETAMENTE NA LISTA_A.

Portanto, se fizermos lista_a.extend(lista_b) e depois demos print(lista_a), será retornado [1,2,3,4,5,6]

'''

'''
Algo que podemos utilziar com listas (e iteraveis no geral) é uma função chamada len().
Com ela podemos ver o tamanho do nosso iteravel. Então, se tivermos, por exemplo, a lista
['José', 'Luiz', 'Carlos'], e usarmos len(lista), essa função irá nos retornar 3, que o tamanho do nosso 
iteravel (nesse caso, o número de elementos dela)
'''
