'''
TIPO TUPLES ()

As tuplas funcionam de forma bem semelhante das listas. A única diferença mesmo é que as tuplas é um tipo imutável, então
costumamos usar tuplas para quando nós queremos guardar dados e não queremos alterá-los mais, então na tupla nós não 
temos os métodos append, insert, pop.. e tudo relacionado a alteração. Veja como é feita a criação de tuplas:

tupla = ()

Acima, temos um exemplo de como é feita uma criação de uma tupla. Assim como nas listas, nas tuplas, nós podemos ter
quaisquer tipos de dados (string, int, float, listas, outras tuplas...). Além disso, algo que é importante de pontuar é
que a tupla em si é imutavel, porém os elementos mutáveis dentro dela (como listas e dicionários) podem ser alterados.

Outro detalhe é que uma tupla vazia, em python, é considerada False, então se tivermos

if ():
    print('ok')

a condição acima não será acionada, pois uma lista vazia é Falsa

Para acessarmos um elemento especifico da tupla, assim como nas listas basta fazer tupla[i], onde i é o indice desse 
elemento na tupla, então se quisermos acessar o primeiro elemento da tupla, por exemplo, usariamos o tupla[0]. 
Podemos utilizar indices negativos também (lembra bastante o acesso de caracteres de uma string) onde tupla[-1] seria o 
último elemento da tupla

Vamos ver na prática agora
'''

tupla = ('Nicolas', 'José', 'Lucas')

print(tupla[0]) #Aqui estamos acessando o primeiro elemento da tupla. Será exibido 'Nicolas'

tupla[0] = 'a' #Aqui estamos tentando alterar o primeiro elemento da tupla ('Nicolas') para 'a'

# Isso que tentamos fazer dará erro, uma vez que tuplas, diferentemente de listas, são imutáveis
