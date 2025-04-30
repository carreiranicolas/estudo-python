'''
RETORNO DE FUNÇÕES

Sempre  que executamos determinada ação com uma função, essa função retorna um determinado valor. 
Lembre-se que as funções retornam, por padrão, valores None, ou seja, um não valor. 

Veja o exemplo abaixo:
'''

def soma(x,y):
    print(x+y)

'''
A função soma acima não retorna um valor (na verdade retorna um valor None, mas sabemos que é um não valor), 
portanto suponha que quiséssemos, no nosso código, utilizar os valores da soma de diferentes argumentos x e y, 
como no exemplo abaixo:
'''

soma1 = soma(2,3)
soma2 = soma(3,3)

soma_total = soma1 + soma2 #Resultaria em erro



'''
Isso acima não daria certo, pois como a função soma retorna apenas valor None, estaríamos somando None + None e 
isso não é possível. Portanto, para que isso desse certo, seria necessário que a função soma retornasse valores de 
fato e não um valor None (valor padrão).

Dessa forma, Para que a nossa função deixe de retornar None e passe a retornar outra coisa, nós vamos utilizar o return.

Veja abaixo:
'''

def somandoo(x,y):
    return x + y # Com esse comando, nossa função deixará de retornar None e passará a retornar o valor da soma de x + y.

#

'''



'''