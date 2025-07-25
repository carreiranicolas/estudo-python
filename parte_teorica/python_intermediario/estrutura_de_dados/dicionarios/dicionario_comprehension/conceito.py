'''
DICTONARY COMPREHENSION

Tudo que falamos sobre o list comprehension irá se aplicar ao dictionary

Suponhamos que queiramos fazer um dictionary comprehension, por exemplo, poderíamos fazer da seguinte 
forma:
'''

produto = {
    'nome': 'Caneta',
    'preco': 2.5,
    'categoria': 'Escritorio'
}

#Fazendo o dictionary comprehension:

dictionary = {
    chave:valor
    for chave, valor in produto.items()
}

print(dictionary) #Retorna: {'nome': 'Caneta', 'preco': 2.5, 'categoria': 'Escritorio'}


'''
Agora, nesse dictionary comprehension, suponhamos que quiséssemos deixar as strings em caixa alta, 
poderíamos fazer valor.upper() ali antes do loop for. No entanto, isso não daria certo, daria um erro,
pois um dos valores (o valor da chave preco) é um número float e não tem como utilizar esse método com 
números. Com isso, o que poderíamos fazer é utilizar um if ternário antes do loop for com a função 
“isinstance()” , que irá checar se o valor é de determinado tipo (nesse caso, queremos checar se é uma 
string) e se for, irá retornar True e consequentemente aplicar o método de string .upper(), caso não 
for, irá apenas repetir o valor, sem fazer nada. Para utilizar a função isinstance(), nós passamos o 
valor e o tipo que queremos checar, da seguinte forma: isinstance(valor, str). 
Veja abaixo:
'''

dictionary = {
    chave:valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}

print(dictionary) # Retorna: {'nome': 'CANETA', 'preco': 2.5, 'categoria': 'ESCRITORIO'}



'''
Legal. Agora, suponhamos que queiramos filtrar as chaves que irão entrar no dicionario. Nós queremos
apenas as chaves que forem diferentes de 'categoria'. Poderíamos aplicar um FILTRO fazendo:
'''

#Aplicando filtro:

dictionary = {
    chave:valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

print(dictionary) #Retorna: {'nome': 'CANETA', 'preco': 2.5}

'''
Uma curiosidade interessantissima é que se tivessemos uma lista com tuplas dentro e dentro dessas 
tuplas nós tivessemos elementos que se parecem com chave e valor, poderíamos utilizar o dictionary 
comprehension para transformar isso em um dicionário. Veja:
'''

listinha = [
    ('a', 'Amanda'),
    ('b', 'Beraldo'),
    ('c', 'Carlos')
]

dicionario = {
    chave:valor
    for chave, valor in listinha
}

print(dicionario) # Retorna: {'a': 'Amanda', 'b': 'Beraldo', 'c': 'Carlos'}

#Isso que fizemos acima também poderia ser feito usando a função dict(), como ja vimos em 1conceito.py

