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


'''
Perceba acima então que quando queremos passar nome, sobrenome.., por exemplo, passaríamos como argumentos nomeados

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
Para acessar 'rua' que fica.. Fazemos

'''



'''
Um deatlhe é que o dicionário especificamente não é iteravel, mas se fizermos um for no dicionário, o python chama o método 
do dicionário que nos entrega as chaves, então poderíamos fazer:
'''


#A partir disso, poderíamos acessar os valores dentro das chaves de forma dinâmica da seguinte forma:
