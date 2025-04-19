'''
FUNÇÃO RANGE

A função range é uma função que gera uma sequencia de números inteiros. Apesar de ser uma função totalmente
independente do for, ela é muito utilizada com o for. Ela funciona da seguinte forma:

range(start, stop, step), onde o start é o número onde começa e o stop é o número onde para (sendo que em 
python ele sempre irá parar em um número antes do que definimos no stop. Exemplo: definimos o stop como 10, 
ele irá parar no 9) e também temos o step que é de quanto em quanto ele vai conatr/iterar (semelhante a razão 
que temos em uma PA)

Vamos ver na prática:
'''

for n in range(0, 10, 2):
    print(n)

# O que acontecerá acima nesse loop é que será exibido os números 0, 2, 4, 6, 8