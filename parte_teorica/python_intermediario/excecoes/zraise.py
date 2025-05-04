'''
RAISE PARA LANÇAR ERROS

Algo super interessante de excções, é que podemos lançar "nossas próprias" exceções. 
Na verdade, o que fazemos é utilizar uma exceção, como ZeroDivisionError, por exemplo, e aí podemos
lançar essa exceção (ou seja executar ela, fazer com que ela aconteça) passando a mensagem que quisermos.
Para isso, basta fazer:

raise Exceção(mensagem)

Veja um exemplo:
'''

#raise ZeroDivisionError('Divisão Nicolau') #Retorna ZeroDivisionError: Divisão Nicolau

'''
É interessante porque poderíamos utilizar o raise nas nossas funções, por exemplo. Veja abaixo

É que no caso do exemplo acima, perceba que dentro da função nós temos um “try execept”, onde se ocorrer tudo 
corretamente retornara o resultado da divisão e se rolar alguma divisão por zero, o except será executado. Dentro 
do except, nós estamos RELANÇANDO o erro. Isso é uma baianagem, visto que naturalmente o python ja exibiria o erro 
de divisão por zero para nós. 

Dessa forma, veja uma forma mais inteligente e dinamica de utilizar o raise na nossa função acima seria:

Outra forma interessante de utilizar raise com uma função seria:

Caso o tipo do valor que recebermos não for int ou float, o programa lança uma exceção falando qual o tipo correto 
que deve ser enviado. Isso que fizemos pode ser mais inteligente ainda se modularizado em uma função. 
Veja:

Assim haveria a checagem em uma função a parre e depois só a divisão.

Isso que fizemos é bem interessante, mas idealmente funções não deveriam tratar erros. Deveríamos passar os valores 
já corretos para função, equanto os valores incorretos seriam tratados fora da função.

'''