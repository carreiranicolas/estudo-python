'''
CONDICIONAIS

Dentro da estrutura de uma linguagem da programação, nós temos as condicionais ou estruturas de seleção

As condicionais ou estruturas de seleção serve para "escolher" um caminho de código que será executado a depender de
algumas condições e isso está presenta em basicamente TODAS as linguagens e é EXTREMAMENTE importante.

Em python então, nós temos:

if (condição): 
    script que será executado (ou não) após a condição

elif (condição): → o elif é outra condição que você coloca e dependerá do if, pois caso ele (o if) não seja exceutado você poderá ter outra condição a ser executada
    script que será executado (ou não) após a condição

else: → else é quando nenhuma das condições if e elif são atendidas, é a última opção
    script que será executado


Uma observação é que depois do elif, não precisamos ter OBRIGATORIAMENTE um else, podemos seguir colocando quantos elif nós quisermos até o momento em que nenhum
dos elifs forem atendidos, aí deverá vir o else

Uma outra observação interessante é que existe algo chamado "operação ternária", que é basicamente um 'if else' de uma linha. Veja sua estrutura:

<valor a ser retornado se a condição for TRUE> if <condição> else <outro valor>

Uma última coisa é que podemos seguir fazendo vários ifs na operação ternária, mas não é recomendado que se faça isso, pois pode ficar muito confuso. 

'''

# EXEMPLO CONDICIONAIS

n = int(input('insira um número: '))

if n >6:
    print('maior que 6')
elif n == 6:
    print('igual a 6')
elif 3< n < 6:
    print('maior que 3 menor que 6')
else:
    print('menor que 3')

# Perceba que eu poderia seguir colocando quantos elif's eu quisesse. Além disso, perceba que o else só será acionado se NENHUM if ou elif for acionado.


# EXEMPLO OPERAÇÃO TERNÁRIA

n = int(input('insira um número: '))

print('maior que 6') if n > 6 else print('igual a 6') if n == 6 else print('maior que 3 menor que 6') if 3< n < 6 else print('menor que 3')

# O que vai acontecer nessa operção ternária é que será exibido 'maior que 6' se n > 6 (condição), caso contrário será exibido 'igual a 6', mas SOMENTE se n == 6 
# (condição), caso contrário será exibido 'maior que 3 menor que 6', mas SOMENTE se 3 < n < 6 (condição), aí no fim, se nenhum funcionar, vai exibir 'menor que 3'