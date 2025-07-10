''''
HIGH ORDER FUNCTIONS


Antes de começar a falar sobre high order functions, temos que entender que funções em python são tratadas como 
qualquer tipo de dado, como uma string, por exemplo. Um exemplo disso é que podemos armazenar funções dentro de
variaveis, como abaixo:
'''

def saudacao(msg):
    return msg

v = saudacao('Oi')

saudar = saudacao 

'''
Acima, nós temos dois exemplos da função saudacao sendo armazenada em variaveis. A diferença é que na variavel v,
a funcao saudacao foi executada, então será armazenado 'Oi' na variavel v, pois é o retorno da função saudacao com
o argumento 'Oi'. Por outro lado, no segundo caso, a variavel saudar não está executando a função saudacao e guardando,
como consequencia, o retorno da função saudacao assim como o variavel v fez, mas o que ela está fazendo é apontando 
para o mesmo lugar da memória onde a função saudacao está. Isso nos possibilita a fazer o seguinte:
'''
print(saudar('Oi'))

'''
A variavel..

Além disso, pensando no fato de que funções são como tipo de dados comuns e que podemos fazer várias coisas com
elas (como armazenar em variaveis, por exemplo), uma coisa que poderiamos ter é uma função que executa uma função.
Ou seja, teríamos uma função que recebe outra função como parametro e retorna a função recebida executada.

Esse é exatamente o conceito de Higher Order Function. São funções que recebem outras funções como argumento ou 
retornam uma função como resultado. Veja abaixo um exemplo:
'''

def executa(funcao):
    return funcao()


v = executa(saudacao)

'''
O exemplo acima da função executa com a função saudacao até daria certo, mas retornaria um erro, pois a função
saudacao recebe o argumento posicional "msg" e nós não passamos nada. Para solucionar isso, teríamos que fazer:

def executa(funcao, msg):
    return funcao(msg)
'''



