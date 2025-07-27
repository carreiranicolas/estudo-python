'''
FUNÇÃO LAMBDA

A função lambda é uma função como qualquer outra em Python, porém ela tem suas peculiaridades, que são: 
Ela ser anonima, ou seja, ela não tem nome, nós não daremos nome a ela e também é de uma linha, ou seja, 
você faz ela em uma linha só

Veja abaixo:
'''
soma = lambda x, y: x + y #Primeiro colocamos os parametros (x,y) e depois dos dois pontos, o retorno
print(soma(2, 3))  # Saída: 5


#A função acima é o que seria a função abaixo:

def somaa(x,y):
    return x + y


'''
O lambda é muito utilizado quando precisamos de funções simples que poderão ser usadas como
argumentos de outras funções.

Um bom exemplo para demonstrar isso é quando queremos utilizar o método .sort() ou a função sorted()
para realizar a ordenação de dicionarios de dentro de uma lista conforme a chave nome ou sobrenome de
dentros dos dicionários (caso você não saiba como funciona .sort() e sorted()) visite a
pasta de estrutura de dados da parte básica). Veja abaixo:
'''

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}
]

print(lista) #Antes: [{'nome': 'Luiz', 'sobrenome': 'Miranda'}, {'nome': 'Maria', 'sobrenome': 'Oliveira'}, {'nome': 'Daniel', 'sobrenome': 'Silva'}, {'nome': 'Eduardo', 'sobrenome': 'Moreira'}, {'nome': 'Aline', 'sobrenome': 'Souza'}] 

lista.sort(key=lambda item: item['nome'])

print(lista) #Depois: [{'nome': 'Aline', 'sobrenome': 'Souza'}, {'nome': 'Daniel', 'sobrenome': 'Silva'}, {'nome': 'Eduardo', 'sobrenome': 'Moreira'}, {'nome': 'Luiz', 'sobrenome': 'Miranda'}, {'nome': 'Maria', 'sobrenome': 'Oliveira'}]

'''
Perceba que os dicionarios da lista foram organizados em ordem alfabetica a partir da chave 'nome'.

Isso acontece porque o método .sort() vai iterando os elementos da lista para fazer a ordenação e ai
a função lambda entra pegando cada dicionario iterado pelo método e retorna a o valor da chave 'nome'
desse dicionário, permitindo que o método sort faça a ordenação em ordem alfabetica por meio dos valores
da chave 'nome' de cada dicionario

Agora, suponhamos que queremos ordenar em ordem alfabética a partir de sobrenome. Veja:
'''

lista.sort(key=lambda item: item['sobrenome'])

print(lista) # Retorna: [{'nome': 'Luiz', 'sobrenome': 'Miranda'}, {'nome': 'Eduardo', 'sobrenome': 'Moreira'}, {'nome': 'Maria', 'sobrenome': 'Oliveira'}, {'nome': 'Daniel', 'sobrenome': 'Silva'}, {'nome': 'Aline', 'sobrenome': 'Souza'}]


# Agora vamos utilizar a função sorted() para demonstrar (não muda praticamente nada)


lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}
]


lista_ordenada = sorted(lista, key=lambda item: item['nome'])

print(lista) #Sem ordenação: [{'nome': 'Luiz', 'sobrenome': 'Miranda'}, {'nome': 'Maria', 'sobrenome': 'Oliveira'}, {'nome': 'Daniel', 'sobrenome': 'Silva'}, {'nome': 'Eduardo', 'sobrenome': 'Moreira'}, {'nome': 'Aline', 'sobrenome': 'Souza'}]

print(lista_ordenada) #Com ordenação: [{'nome': 'Aline', 'sobrenome': 'Souza'}, {'nome': 'Daniel', 'sobrenome': 'Silva'}, {'nome': 'Eduardo', 'sobrenome': 'Moreira'}, {'nome': 'Luiz', 'sobrenome': 'Miranda'}, {'nome': 'Maria', 'sobrenome': 'Oliveira'}]

'''
Se as funções lambdas não existissem, nós teríamos precisado criar uma função para depois passar para
key= e assim conseguir fazer o que fizemos. Com a função lambda, fica bem mais simples
'''