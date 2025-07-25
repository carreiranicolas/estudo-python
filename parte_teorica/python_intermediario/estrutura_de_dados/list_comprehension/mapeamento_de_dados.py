'''
MAPEAMENTO DE DADOS

Na list comprehention, nós podemos fazer mapeamento de dados. Isso significa que estamos pegando dados 
de um lado do iterável (uma lista), transformando esses dados e colocando em outra lista, sendo que 
esses dois iteraveis tem que ter o mesmo tamanho. Veja um exemplo:
'''

lista = [numero * 2 for numero in range(10)]

print(list(range(10))) #Retorna: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista) #Retorna: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


'''
Note acima que temos listas do mesmo tamanho, além disso, os elementos da primeira lista tem o mesmo 
indice dos elementos da segunda lista. Na primeira lista, por exemplo, o elemento 0 tem o mesmo indice 
do elemento 0 da segunda lista. A única coisa que muda de uma lista para outra é a TRASNFORMAÇÃO dos 
elementos da primeira lista ao serem multiplicados por 2, porém o tamanho da lista é o mesmo e a 
equivalencia de index entre os elementos é a mesma

Agora, faremos um exemplo mais complexo que envolverá, inclusive, dicionarios, mas será importante
para que possamos entender de maneira plena o mapeamento e sua utilidade em list comprehension. Dessa 
forma, caso precise ver sobre dicionarios antes, basta acessar a pasta de dicionarios. 
Vamos ao exemplo:
'''

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 30},
    {'nome': 'p3', 'preco': 40},
]

'''
Poderíamos querer mapear essa lista acima para outra lista jogando os produtos com preços de valores 
diferentes dentro da outra lista. Veja:
'''

novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco'] * 2}
    for produto in produtos
]

print(produtos) # Retorna: [{'nome': 'p1', 'preco': 20}, {'nome': 'p2', 'preco': 30}, {'nome': 'p3', 'preco': 40}]
print(novos_produtos) #Retorna: [{'nome': 'p1', 'preco': 40}, {'nome': 'p2', 'preco': 60}, {'nome': 'p3', 'preco': 80}]

'''
Perceba na imagem acima que estamos mapeando a lista “produtos” para a lista “novos_produtos”. 
Estamos fazendo isso criando um dicionario antes do loop for para cada item da lista “produtos”. As 
chaves dessa lista “Novos_produtos” são as mesmas da lista “produtos”, sendo que na chave ‘preco’, nós 
teremos o preço do produto especifico na lista “produtos” multiplicado por 2.

Agora vai uma pergunta: Suponhamos que tivéssemos 500 chaves em cada dicionario dessa lista “produtos”, 
nós teríamos que criar um dicionario antes do loop for e escrever as 500 chaves uma a uma? Na verdade 
não, poderíamos fazer o desempacotamento do de cada dicionario (cada produto) no dicionario que fica 
antes do loop for. Veja:
'''

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 2}
    for produto in produtos
]

#OBS: lembre-se que não há chaves repetidas em dicionarios, então quando “criamos” a nova chave “preco” 
# depois do desempacotamento do dicionario produto, a chave “preco” que estava dentro do dicionario 
# produto irá assumir o valor da chave “preco” que foi “criada depois”

'''
Portanto, note que simplifica muito as coisas. Inclusive, é interessante que após fazer esse 
desempacotamento, poderíamos adicionar uma nova chave-valor caso quisséssemos. Veja:
'''

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 2, 'reajuste': 'x2'}
    for produto in produtos
]

print(novos_produtos) #Retorna: [{'nome': 'p1', 'preco': 40, 'reajuste': 'x2'}, {'nome': 'p2', 'preco': 60, 'reajuste': 'x2'}, {'nome': 'p3', 'preco': 80, 'reajuste': 'x2'}]

'''
Além disso, outra coisa muito interessante que poderíamos fazer é: Suponhamos que queiramos multiplicar 
por 2 apenas os preços que sejam maior que vinte, poderíamos fazer isso utilizando um if ternario. 
Veja:

'''

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 2} if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(novos_produtos) #Retorna: [{'nome': 'p1', 'preco': 20}, {'nome': 'p2', 'preco': 60}, {'nome': 'p3', 'preco': 80}]

'''
Portanto, o que acontece acima é que haverá o desempacotamento de produto e o preço do produto só será 
multiplicado por 2 caso o preço for maior que 20, caso contrário, só irá feito o desempacotamento, 
fazendo com que o preço permaneça a mesma coisa
'''