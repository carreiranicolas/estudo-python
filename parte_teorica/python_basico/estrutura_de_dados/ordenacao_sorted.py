'''
FUNÇÃO SORTED

A função sorted é uma função que pode ser utilizada com qualquer iteravel (listas, tuplas, dicionarios, 
sets..) e sempre retorna uma nova lista ordenada (ou seja, não modifica o original). Veja:
'''

lista_original = [8, 7, 6]

lista_ordenada = sorted(lista_original)

print(lista_original)
print(lista_ordenada)

#Um detalhe é que o sorted aceita qualquer iteravel, assim como dissemos, mas sempre retorna uma lista
# Veja:

conjunto = {9, 3, 7}
ordenado = sorted(conjunto)
print(ordenado)  # [3, 7, 9]  ← virou lista

texto = "gato"
ordenado = sorted(texto)
print(ordenado)  # ['a', 'g', 'o', 't']

d = {'c': 3, 'a': 1, 'b': 2}
ordenado = sorted(d)
print(ordenado)  # ['a', 'b', 'c'] ← lista com as chaves ordenadas


'''
Um outro detalhe é que a função sorted aceita os parametros key= e reverse=.

O reverse=, nós iremos passar False ou True para dizer se a ordenação será em ordem crecente ou
decrescente. Esse parametro vem com False por padrão. Veja:
'''

lista_original = [3, 1, 4, 2]
lista_ordenada = sorted(lista_original, reverse=True)

print(lista_original)
print(lista_ordenada) #[4, 3, 2, 1]

'''
O uso do key= é mais complexo, ele recebe uma função que será aplicada a cada elemento do iterável 
para determinar o valor a ser usado na ordenação. Em outras palavras, estamos dizendo ao python:
"Ei, ao invés de ordenar direto os elementos, ordene baseado em alguma transformação deles."
Veja um exemplo:
'''

palavras = ['python', 'é', 'muito', 'legal']
ordenado = sorted(palavras, key=len)
print(ordenado)  # ['é', 'legal', 'muito', 'python']

#Acima, o Python usa o comprimento das palavras como chave de ordenação.


'''
Portanto, o key= irá receber uma função que será aplicada a cada item, o que pode customizar o critério
de ordenação. A função recebida pelo key= pode ser até mesmo funções criadas por nós mesmo ou então
funções do próprio python, como vimos no exemplo acima ao utilizar o len(). 
'''



