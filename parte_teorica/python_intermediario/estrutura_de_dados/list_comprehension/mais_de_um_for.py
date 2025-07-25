'''
LIST COMPREHENSION COM MAIS DE UM FOR

SUponhamos que quiséssemos fazer um for dentro do for e ir adicionando esses valores em uma lista. 
Na forma convencional, poderíamos fazer isso da seguinte forma:
'''

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x,y))

print(lista) #Retorna: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Mas como poderíamos fazer isso em list comprehension? Veja como poderíamos fazer:

lista_comprehension = [
    (x,y)
    for x in range(3)
    for y in range(3)
]

print(lista_comprehension) #Retorna: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

'''
Bastaria fazer isso que fizemos acima. Perceba que é só fazer um for debaixo do outro.

Outra coisa que podemos fazer de interessante é o seguinte:
'''

list_comprehension = [
    [x for n in range(3)]
    for x in range(3)
]

print(list_comprehension) # Retorna: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

'''
O que acontece acima é que ele irá rodar o último loop for, sendo que o primeiro número desse loop é 0. 
Depois disso, o que acontece é que ele vai lá pra cima, cria uma lista e dentro dessa lista nós temos 
“x for n in range(3)”. Isso significa que será adicionado nessa lista de cima o valor de x para cada 
iteração n daquela lista. Como estamos na primeira iteração do último loop, o valor de x é 0, então será 
adicionado o valor 0 à lista para cada iteração que tivermos ali. Como são 3 iterações, o valor 0 foi 
adicionado 3 vezes. O mesmo acontece para os próximos.

'''