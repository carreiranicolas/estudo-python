'''
METODOS - DICIONARIOS

Vamos ver agora sobre alguns métodos úteis para se usar com dicionários:
'''

pessoa = {
    'nome': 'Nicolas',
    'sobrenome': 'Carreira',
    'idade': 20
}


#Método .__len__(): Retorna o número de chaves do dicionário

print(pessoa.__len__()) #Retorna 3

#OBS: Poderíamos ao invés de usar o método __len__, usar a função len() passando o dicionario para dentro dela

# Método .keys():  retorna as chaves que temos em nosso dicionário em um tipo dict_keys, que pode ser convertido em 
# tuplas ou lista depois, por exemplo.

print(pessoa.keys()) #Retorna: dict_keys(['nome', 'sobrenome', 'idade'])

print(tuple(pessoa.keys())) #Retorna: ('nome', 'sobrenome', 'idade')

for chaves in pessoa.keys():
    print(chaves) #Retorna: nome
                              #sobrenome
                              #idade

#Método .values(): Lembra o método .keys(). Nos retorna só os valores que temos

 
print(pessoa.values()) #Retorna: dict_values(['Nicolas', 'Carreira', 20])

print(tuple(pessoa.values())) #Retorna: ('Nicolas', 'Carreira', 20)

for valor in pessoa.values():
    print(valor) #Retorna: Nicolas
                              #Carreira
                              #20

#Método .items(): Lembra ambos os métodos anteriores (keys e values), mas retorna a chave e o valor

print(pessoa.items()) #Retorna: dict_items([('nome', 'Nicolas'), ('sobrenome', 'Carreira'), ('idade', 20)])

print(tuple(pessoa.items())) #Retorna: (('nome', 'Nicolas'), ('sobrenome', 'Carreira'), ('idade', 20))

for chave, valor in pessoa.items():
    print(chave)
    print(valor) #Retorna: nome
                           #Nicolas
                           #sobrenome
                           #Carreira
                           #idade
                            #20

#Método .setdefault(): Suponhamos que queiramos uma chave que não existe em nosso dicionário (‘altura’, por exemplo), 
# se tentamos pegar essa chave inexistente, irá nos retornar um erro como sabemos, mas podemos configurar o 
# dicionário para retornar um valor por padrão quando essa chave não existir e for requisitada e é apartir do 
# setdefault() que fazemos isso.

pessoa.setdefault('altura', 'Valor padrão' )

print(pessoa['altura']) #Retorna: Valor padrão



# Método .get(): Esse método nos retorna ou o valor da chave passada, ou retorna None (caso a chave não exista)

print(pessoa.get('nome')) # Retorna: Nicolas

print(pessoa.get('altura')) #Retorna: None

#Método .pop(): apaga a chave especificada do nosso dicionário e ainda nos retorna o valor que estava naquela chave.

nome = pessoa.pop('nome')

print(nome) # Retorna: Nicolas
print(pessoa) #Retorna: {'sobrenome': 'Carreira', 'idade': 20}

#Método .popitem():  elimina a última chave do dicionário e ainda retorna o que foi removido (tanto a chave quanto o valor)

ultima_chave = pessoa.popitem()

print(ultima_chave) #Retorna: ('idade', 20)
print(pessoa) #Retorna: {'sobrenome': 'Carreira'}


#Método .update(): podemos fazer várias coisas, como atualizar os valores de chaves existentes, adicionar novas 
# chaves e dentre outras coisas. O melhor é que o update permite que façamos tudo isso ao mesmo tempo.



#OBS: Podemos fazer o update utilizando argumentos nomeados também, veja:

#OBS2: Podemos também fazer o update utilizando tuplas e listas. Veja:


# MÉTODOS DE CÓPIA (.copy() e deepcopy())

'''
Assim como em listas, os dicionarios também tem o método .copy(). Já falamos sobre esse método 
em metodos.py de estrutura_de_dados da parte_basica, mas vamos relembrar. Suponhamos que tenhamos um 
dicionario1 (que é um tipo mutavel) abaixo:
'''

dicionario1 = {
    'n1': 1,
    'n2': 2
}

'''
Se criarmos a variavel dicionario2 e atribuirmos o dicionario1 a ela, nós não estaremos fazendo uma 
cópia do dicionario1 na variavel dicionario2. O que estará acontecendo é que a variavel dicionario2 
estará apontando para dicionario1 e então, quando fizermos alguma alteração em dicionario2, ela será 
feita em dicionario1 também. Veja na prática:
'''

print(dicionario1) #Retorna: {'n1': 1, 'n2': 2}

# dicionario2 = dicionario1 --> deixei comentado para dar seguimento a explicações futuras

# dicionario2['n1'] = 1000 --> deixei comentado para dar seguimento a explicações futuras

print(dicionario1) #Retorna: {'n1': 1000, 'n2': 2}, apesar da alteração ter sido feita em dicionario2

'''
Dessa forma, para fazermos a cópia, iremos precisar usar o método .copy() e ele nos irá retornar uma 
cópia rasa (shallow copy). Veja:
'''

dicionario2 = dicionario1.copy()

dicionario2['n1'] = 1000

print(dicionario1) #Agora retorna: {'n1': 1, 'n2': 2}
print(dicionario2) #Agora retorna: {'n1': 1000, 'n2': 2}

'''
Agora, note que ao fazermos uma alteração no dicionario2, ela não se reflete no dicionario1, pois a 
variavel dicionario2 não aponta mais para dicionario1, uma vez que fizemos a copia do dicionario1 em 
dicionario2, assim dicionario2 terá seu próprio dicionario.

Teoricamente estaria tudo bem, mas isso que fizémos é uma cópia rasa, ou seja, tudo que que for 
imutável e estava no dicionario1, será copiado para dicionario2, mas caso não for imutavel.. Aí teremos 
um problema. Se tivéssemos uma lista dentro de dicionario1 e tentássemos copiar o dicionario1 para 
dicionario2, o que aconteceria é que não teríamos uma lista diferente copiada para o dicionario2. Na 
verdade, a lista que seria copiada para o dicionario2 estaria linkada à lista do dicionario1 e isso é 
um problema, pois se quisséssemos alterar os valores dessa lista apenas no dicionario1, também seria 
alterado no dicionario2. Veja:

'''

dicionario1 = {
    'n1': 1,
    'n2': 2,
    'lista': [1,2,3]
}

print(dicionario1) #Retorna: {'n1': 1, 'n2': 2, 'lista': [1, 2, 3]}

dicionario2 = dicionario1.copy()

dicionario2['lista'][0] = 9999999

print(dicionario1) #Retorna: {'n1': 1, 'n2': 2, 'lista': [9999999, 2, 3]}

'''
Perceba que alteramos o valor de indice 0 da lista do dicionario2, mas também alterou no dicionario1, 
pois as listas estão linkadas. Esse é o problema do Shallow Copy, por isso temos que fazer um Deep Copy. 
Para fazer um Deep Copy, o python tem um módulo chamado copy (import copy) e aí usaríamos u método 
chamado deepcopy. VeJA:
'''

import copy

dicionario1 = {
    'n1': 1,
    'n2': 2,
    'lista': [1,2,3]
}

print(dicionario1) # Retorna: {'n1': 1, 'n2': 2, 'lista': [1, 2, 3]}

dicionario2 = copy.deepcopy(dicionario1)

dicionario2['lista'][0] = 999999

print(dicionario1) #Continua retornando {'n1': 1, 'n2': 2, 'lista': [1, 2, 3]}

print(dicionario2) #Retorna {'n1': 1, 'n2': 2, 'lista': [999999, 2, 3]}



#Método .clear(): Limpa tudo dentro do dicionário

pessoa.clear()
