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

Dessa forma, se agora fizermos:

v = executa(saudacao('Oi'))

Isso acima dará certo. Executamos a função executa, que recebeu como argumento a função saudacao e o argumento ‘Oi’. 
A partir disso, a função executa retornou a função saudacao executada com o argumento ‘Oi’ que foi recebido pela 
própria função executa.

Perfeito, agora vamos imaginar que nossa função saudacao passe a receber dois argumentos agora: o msg (a mensagem de 
saudação) e o nome (um nome qualquer) e retornasse uma string com esses dois argumentos, como abaixo:
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

'''
Tendo nossa nova função saudação acima, se tentarmos fazer:

v = executa(saudacao, 'Oi')

Dará erro. Isso acontece porque na função executa, no return dela, estamos executando a função saudacao, porém 
estamos executando-na passando um argumento a menos que ela deveria ter (o argumento nome, no caso), então temos que 
fazer essa alteração na função executa para correr tudo certinho. No entanto, o que podemos fazer é deixar essa 
função executa dinâmica, pois se a cada parametro que adicionarmos a mais na função saudacao, nós tivermos que fazer 
a alteração na função executa, estaremos fritos. Portanto, ao invés de ir na função executa e adicionar mais um 
parametro chamado “nome”, nós vamos lá e vamos apagar o parâmetro msg e adicionar o parametro chamado *args. 
Isso porque o *args poderá receber uma série de valores e passa-los para função saudacao, sem precisarmos alterar o 
numero de parametros recebidos pela função executa sempre que alterarmos isso função saudacao. Veja:

def executa(funcao, *args): --> o *args aqui recebe os valores de maneira empacotada
    return funcao(*args) --> o *args aqui passa os valores de maneira desempacotada

'''







