'''
FUNÇÃO ENUMARATE

A função enumerate basicamente pode receber um iterável qualquer e irá adicionar a cada item desse iteravel o seu indice.
Então se temos uma lista (lembrando que lista é um iteravel) lista = ['Nicolas', 'José', 'Carlos'], ao fazer 
enumerate(lista), teremos como retorno: [(0,'Nicolas'), (1,'José'), (2, 'Carlos')]

Dessa forma, a função enumerate basicamente retorna uma lista com tuplas dentro delas contendo os elementos da lista que
foi enumerada e seus indices

Vamos ver na prática
'''

lista = ['Nicolas', 'José', 'Carlos']

lista_enumerada = enumerate(lista)

for elemento in lista_enumerada:
    print(elemento)#Retorno:  # (0, 'Nicolas')
                              # (1, 'José')
                              # (2, 'Carlos')

'''
Como o enumerate é um iterador, ele tem um comportamento estranho. Após o a lista ter sido enumerada em 
lista_enumerada = enumerate(lista), se tentarmos reutilizar lista_enumerada depois, não acontecerá nada, pois não 
haverá mais nada ali. O iterador já consumiu (já enumerou) os valores que ele precisava. 

Veja abaixo:
'''

for elemento in lista_enumerada:
    print(elemento) #Não retornará absolutamente nada

'''
Para contornar isso, geralmente utilizamos a função enumerate direto no  loop for ao invés de criar uma variável para ela 
(igual fizemos em lista_enumerada = enumerate(lista)), porque ai é como se tivéssemos toda vez criando um novo iterador 
e aí os valores não se esgotam, diferente do que acontecia anteriormente. 

Veja:
'''

for elemento in enumerate(lista):
    print(elemento)#Retorno:  # (0, 'Nicolas')
                              # (1, 'José')
                              # (2, 'Carlos')



'''
Um detalhe é que podemos utilizar o desempacotamento para obter o indice e o valor do elemento de forma separada.
Veja:
'''

for elemento in enumerate(lista):
    indice,valor = elemento
    print(indice)
    print(valor) #Retorno: # 0
                           # Nicolas
                           # 1
                           # José
                           # 2
                           # Carlos

#Podemos fazer isso de forma mais direta ainda. Veja abaixo:

for indice,valor in enumerate(lista):
    print(indice)
    print(valor) #Retorno: # 0
                           # Nicolas
                           # 1
                           # José
                           # 2
                           # Carlos


'''
Uma observação é que poderíamos dizer a partir de qual numero queremos que o enumerate numere nossos itens
passando um start=. Veja:
'''

for elemento in enumerate(lista, start=5):
    print(elemento)#Retorno:  # (5, 'Nicolas')
                              # (6, 'José')
                              # (7, 'Carlos')

'''
Vamos ver um exemplo rápido do uso do enumerate com um iteravel diferente de lista, vamos usar string
Veja:
'''
string = 'Nicolas'

for letra in enumerate(string):
    print(letra) # Retorno:   # (0, 'N')
                              # (1, 'i')
                              # (2, 'c')
                              # (3, 'o')
                              # (4, 'l')
                              # (5, 'a')
                              # (6, 's')

