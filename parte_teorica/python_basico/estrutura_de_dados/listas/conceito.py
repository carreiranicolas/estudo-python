'''
TIPO LIST []

Listas é uma estrutra de dados em python que é mutavel, então além de conseguir fazer o que uma estrutura de dados comum
faz (armazenar dados), com ela, podemos editar esses dados, remover, adicionar e manipularmos da forma que quisermos.
Veja como é feita a criação de uma lista

lista = []

Acima temos o exemplo de como é feita a criação de uma lista. Dentro dela, podemos adicionar o tipo de dado que quisermos
(int, float, string, bool, listas, tuplas, dicionarios...), sendo que, uma lista pode ser classificada em HOMOGENEA e 
HETEROGENEA

--> Lista homogenea: Contém apenas tipos de dados do mesmo tipo dentro dela

--> Lista heterogenea: Contém apenas tipos de dados do mesmo tipo dentro dela

Um detalhe é que uma lista vazia é considerada False, então se tivermos:

if []:
    print('ok')

a condição acima não será acionada, pois uma lista vazia é Falsa

Para acessarmos um elemento especifico da lista, basta fazer lista[i], onde i é o indice desse elemento na lista,
então se quisermos acessar o primeiro elemento da lista, por exemplo, usariamos o lista[0]. Podemos utilizar indices
negativos também (lembra bastante o acesso de caracteres de uma string) onde lista[-1] seria o último elemento da lista

Vamos ver na prática agora

'''

lista = ['Nicolas', 'José', 'Lucas']

print(lista[1]) #Aqui estamos acessando o segundo elemento da lista. Será exibido 'José'

lista[1] = 'Maria' #Aqui estamos alterando o valor do segundo elemento da lista de 'José' para 'Maria'

print(lista[1]) #Acessamos o segundo elemento da lista e veremos que agora seu valor é 'Maria' e não mais 'José'

'''
Perceba com o exemplo acima então que estamos alterando os valores da lista de forma bem tranquila. Se estivéssemos 
tentando alterar a letra de uma string, por exemplo, como já vimos no nosso estudo sobre strings, daria um erro. Isso
porque strings é um tipo imutável, enquanto listas é um tipo mutável.

Para vermos como podemos adicionar dados, remover e outras coisas, temos que ir para o arquivo de metodos, aqui dentro
da pasta listas

Uma pequena observação (que parece até meio obvia) é que listas são iteráveis, então podemos acesssar elemento por
elemento dela usando um loop for, por exemplo.

Uma outra observação é que quando queremos acessar um elemento que está dentro de
uma lista, que por usa vez está dentro de uma lista, nós vamos ter um aninhamento de listas
o acesso a esse elemento será de uma forma um pouco diferença. Veja no arquivo de aninhamento.py
'''