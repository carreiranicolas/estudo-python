'''
RETORNO DE FUNÇÕES

Sempre  que executamos determinada ação com uma função, essa função retorna um determinado valor. 
Lembre-se que as funções retornam, por padrão, valores None, ou seja, um não valor. 

Veja o exemplo abaixo:
'''

def soma(x,y):
    print(x+y)

'''
A função soma acima não retorna um valor (na verdade retorna um valor None, mas sabemos que é um não valor), ela 
apenas exibe o resultado da soma entre x e y. Portanto suponha que quiséssemos, no nosso código, utilizar os valores
da soma de diferentes argumentos x e y, como no exemplo abaixo:
'''

soma1 = soma(2,3)
soma2 = soma(3,3)

#soma_total = soma1 + soma2 #Resultaria em erro


'''
Isso acima não daria certo, pois como a função soma retorna apenas valor None, estaríamos somando None + None e 
isso não é possível. Portanto, para que isso desse certo, seria necessário que a função soma retornasse valores de 
fato e não um valor None (valor padrão).

Dessa forma, Para que a nossa função deixe de retornar None e passe a retornar outra coisa, nós vamos utilizar o return.

Veja abaixo:
'''

def somandoo(x,y):
    return x + y # Com esse comando, nossa função deixará de retornar None e passará a retornar o valor da soma de x + y.

#Agora veja abaixo:

somaum = somandoo(2,3)
somadois = somandoo(4,5)

somatotal = somaum + somadois
print(somatotal) # retorna a soma dos valores retornados por somandoo(2,3) e somandoo(4,5)

'''
Antes, utilizando o print para tentar fazer isso, vimos que há muitas limitações, pois o print serve apenas para 
exibir alguma coisa. Então, não conseguimos jogar o valor que resultou da soma para uma variável, por exemplo, porque
só retornava None. Algo que é importante de se pontuar é que podemos retornar da nossa função qualquer tipo de dado
(int, float, texto, tupla, lista..)

Uma observação é que depois do return em uma função, não conseguimos executar mais nada na nossa função. 
Ou seja, é como se ela disesse para o python “Termina a função”. Veja:

def somandoo(x,y):
    return x + y 
    print('Feito')

Na função acima, o print('Feito') não será executado. Inclusive, no VSCode, se você tiver alguma coisa depois do
return de uma função em Python, ele aparecerá o trecho de código depois do return mais apagado com uma mensagem
escrita "Code is unreachable Pylance", significando que esse código não será exercutado

Outra coisa se falar é que poderíamos também utilizar fluxos de código (condicionais) para basear o retorno da nossa 
função. Veja:

def somandoo(x,y):
    if x < 10:
        return x + 1
    else:
        return x + y

Na função acima, dependendo do argumento que passarmos para x, ele poderá executar um dos dois returns, mas é 
importante dizer: APENAS UM RETURN SERÁ USADO POR FUNÇÃO. No exemplo acima, não poderíamos por exemplo utilizar o
return x+1 e também o return x + y

'''