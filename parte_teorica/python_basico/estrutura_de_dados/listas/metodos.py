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

'''


'''
Concatenação de listas (método extend e operador '+')

Podemos fazer a conctenação de listas utilizando o método extend e o operador '+'

'''
