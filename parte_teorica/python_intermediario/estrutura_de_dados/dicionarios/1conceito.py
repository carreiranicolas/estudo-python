'''
DICIONARIOS

Dicionários de dados são estruturas de dados em python  do tipo chave e valor. Essa chave podemos considerar como sendo a 
“mesma coisa” que o indice para listas e o valor é o valor em si. Inclusive, assim como as listas, dicionáros são mutáveis.
Usamos chaves {} para criar dicionários ou entao a classe dict pode ser usada também para criar dicionários. 

Além disso, nos dicionários em python, AS CHAVES podem ser criadas com qualquer tipo IMUTAVEL do python (str, int, float, bool e tuple).
O VALOR pode ser de QUALQUER TIPO como é na lista. Podemos, inclusive, ter outro dicionário dentro do próprio dicionário.

Dicionarios são interessantes para serem usados para jogar um valor dentro de determinado "indice", onde esse "indice" 
pode ser referenciado de maneira mais simples (coloquei indice entre aspas porque na verdade estamos falando de chaves, mas
estamos fazendo um paralelo com listas para poder explicar sobre dicionarios)

Em listas, por exemplo, se tivermos uma lista: lista = ['Luiz'], iriamos referenciar o nome luiz com o indice 0. Isso pode ser confuso 
e complicado para lembrar. Se, por exemplo, criarmos uma lista que além do nome tem os atributos da pessoa, como sobrenome, idade, altura, endereço 
(lista = ['Luiz', 'Carreira', 19, 1.80, 'Itaparica']), podemos utilizar os dicionários onde nós podemos ter uma string como chave ('nome') onde podemos 
encontrar o nome dessa pessoa referenciando pela string 'nome', o  que é muito mais simples que encontrar o nome da pessoa referenciando por indice, por exemplo.
Então nós estamos basicamente dando nome aos bois

Vamos ver agora como criamos dicionarios. Veja:
'''

pessoa1 = {
    'nome': 'Nicolas',
    'sobrenome': 'Carreira',
    'idade': 19,
    'altura': 1.72
}

print(pessoa1, type(pessoa1)) # Irá retornar: {'nome': 'Nicolas', 'sobrenome': 'Carreira', 'idade': 19, 'altura': 1.72} <class 'dict'>

#OUTRA FORMA DE CRIAR DICIONARIOS, COMO DISSÉSMOS ANTES É USANDO A CLASSE DICT

pessoa2 = dict(nome='Luiza', sobrenome='Carreira', idade=16, altura=1.60)

print(pessoa2, type(pessoa2)) # {'nome': 'Luiza', 'sobrenome': 'Carreira', 'idade': 16, 'altura': 1.6} <class 'dict'>

#CURIOSIDADE: Podemos criar dicionarios a partir de tuplas. Veja:

# 1- Criando dicionarios com tuplas: Precisamos ter uma lista com as tuplas, sendo que cada tupla
# precisa ter 2 valores (um será referente a chave e outro será referente ao valor)

lista_tuplas = [('nome', 'José'), ('idade', 25), ('cidade', 'São Paulo')]
dicionario = dict(lista_tuplas)
print(dicionario) # Retorna: {'nome': 'José', 'idade': 25, 'cidade': 'São Paulo'}

'''
Um detalhe que é importante de se falar é que se criarmos um dicionario com chaves repetidas, mas valores diferentes,
a chave que será usada será a última. Veja abaixo no exemplo:

pessoa = {'nome': 'Nicolas', 'nome': 'José'}

print(pessoa) # Retorna: {'nome': 'José'}

Para acessar os itens do dicionario é praticamente a mesma coisa que acessar um item de uma lista, mas de forma muito mais fácil.
Se quiséssemos acessar o nome da pessoa, por exemplo, nós faríamos: pessoa['nome']. Veja abaixo:
'''

print(pessoa1['nome']) #Irá retornar: Nicolas

'''
Outra coisa muito interessante é que: suponhamos que quiséssemos inserir dentro do dicionário 'endereços', sendo que nesses 
endereços nós teríamos rua e número, por exemplo. Veja como poderíamos fazer:
'''

pessoa1 = {
    'nome': 'Nicolas',
    'sobrenome': 'Carreira',
    'idade': 19,
    'altura': 1.72,
    'endereços': [
        {'rua': 'Humberto Pereira', 'número': 254},
        {'rua': 'Rangel Mauro', 'número': 6122}
    ]
}

'''
Perceba que  criamos endereços e dentro dessa chave colocamos uma lista e essa lista tem dentro dela outros dicionários.
Para acessar 'rua' que fica dentro da lista em 'endereços', fazemos:
'''

print(pessoa1['endereços'][0]['rua']) #Isso retorna: Humberto Pereira


print(pessoa1['endereços'][1]['rua'])  #Isso retorna: Rangel Mauro


'''
Um deatlhe é que o dicionário especificamente não é iteravel, mas se fizermos um for no dicionário, o python chama o método 
do dicionário que nos entrega as chaves, então poderíamos fazer:
'''

for chave in pessoa1:
    print(chave) #Irá retornar: nome
                               #sobrenome
                               #idade
                               #altura
                               #endereços


#A partir disso, poderíamos acessar os valores dentro das chaves de forma dinâmica da seguinte forma:

for chave in pessoa1:
    print(chave, pessoa1[chave]) #Irá retornar: nome Nicolas
                                                #sobrenome Carreira
                                                #idade 19
                                                #altura 1.72
                                                #endereços [{'rua': Humberto Pereira1, 'número': 254}, {'rua': Rangel Mauro, 'número': 6122}]

'''
Uma observação é que se quiséssemos acessar uma chave que não existe dentro do dicionário, nos retornaria um erro,
mas existe um detalhe sobre isso, que falaremos melhor sobre em metodos.py, mas podemos acessar chaves que não 
existem no dicionario sem dar erro utilizando o metodo .get() e o .setdefault()
'''


'''
Já vimos como criamos dicionários e como acessamos seus valores. Agora, veremos mais alguns detalhes. Veremos como
criar novas chaves em um dicionário já existente, como editar os valores das chaves já existentes e como exclui-las


- CRIANDO CHAVES

Suponhamos que tivéssemos o dicionário vazio abaixo em nosso código e quisséssemos criar uma chave com um valor, 
por exemplo. Poderiamos fazer o seguinte:
'''

pessoinha = {}

pessoinha['nome'] = 'Nicolas'

print(pessoinha) # Retorna {'nome': 'Nicolas'}

# Outra coisa que podemos fazer é utilizar chaves de formas dinâmicas. Veja:

chavinha = 'idade'

pessoinha[chavinha] = 20

print(pessoinha) # Retorna {'nome': 'Nicolas', 'idade': 20}

'''
- REATRIBUIÇÃO DE VALORES PARA CHAVES (EDITAR VALORES DAS CHAVES)

Como o dicionario é um tipo mutavel, podemos atribuir um valor a uma chave e depois mais afrente atribuir outro valor, 
assim o valor que foi atribuido por último seria adotado como valor final (é a mesma coisa que acontece nas listas.) 
Veja:
'''

pessoinha['nome'] = 'José'

print(pessoinha) #Agora retorna: {'nome': 'José', 'idade': 20}

'''
- EXCLUINDO CHAVES

Quando quisermos deletar uma chave juntamente com seu valor, nós fazemos: del dicionario[chave]. Veja:
'''

del pessoinha['nome']

print(pessoinha) # Agora retorna: {'idade': 20}