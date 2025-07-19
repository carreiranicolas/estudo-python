'''
RECURSIVIDADE

Quando falamos de recursividade, estamos falando de uma coisa que chama ela de volta basicamente. Como estamos 
falando de funções, são funções que se chamam de volta (imagine que temos uma função e na hora de retornar um valor, 
ao invés de retornar um valor, retornamos ela)

Funções recursivas são interessantes para dividir problemas grandes em partes menores. A questão é a gente precisa 
de um problema que POSSA ser divido em partes menores e de forma uniforme. Quanto mais uniforme for o problema, 
mais facil de criar a função recursiva. Então se temos um problema que geralmente eu resolvo com muita iteração e 
loop, geralmente (nem sempre) eu consigo converter isso em função recursiva

Portanto, se a gente pega um problemão, dividindo esse problemão em vários pequenos problemas, a gente tem que ter 
um caso onde a função se chama de volta (caso recursivo) e resolve este pequeno problema. Resolvendo todos os 
pequenos problemas, a gente precisa ter um CASO BASE, ou seja, quando chega num ponto que a função fala: “beleza, 
problema resolvido, vamos retornar esse valor”. E é assim que as funções recursivas funcionam. Veja um exemplo
simples:
'''

#Suponhamos que nosso problema seja contar até 10

def recursiva(inicio=0, fim=10):
    inicio += 1
    return recursiva(inicio, fim)


'''
Se executarmos essa função acima da maneira que está, vamos causar um StackOverflow. Ou seja, um erro. 
Stackoverflow siginifca que estamos colocando muita coisa na callstack  (podemos encontrar a callstack ao utilizar 
o debugger). O callstack começa a encher e o python fala “Olha.. eu não quero estourar o seu computador”, Então 
o Python por livre espontanea vontade para e te dá um erro quando começa a acontecer um Stackoverflow.  

Para corrigir esse problema, precisamos de um CASO BASE, ou seja, quando eu quero retornar o valor e parar. 
Veja abaixo:
'''

def recursiva(inicio=0, fim=10):
    if inicio >= fim: # -> Caso base
        return fim
    inicio += 1
    return recursiva(inicio, fim)

'''

Primeiro a função recursiva é definida e depois executada no print. Na execução, entramos no escopo da função onde 
inicio = 0 e fim = 10. Agora estamos dentro da função com inicio = 0. Como 0 >= 10 é falso, o código continua e será 
incrementado +1 ao nosso “início” e após isso chamamos a função novamente no return com o novo valor de “inicio”: 
return recursiva(1,10). A chamada faz com que a execução atual fique em espera na call stack, enquanto a nova 
chamada acontece. Agora estamos em uma nova chamada da função com inicio=1, onde como 1 >=10 é falso, continuamos e i
ncrementamos 1 a “início” e em seguida chamamos a função novamente no return com o novo valor de “inicio”: return 
recursiva(2,10). Isso acontecerá sucessivamente. 

Quando chegarmos a recursiva(10,10), será feita  a verificação no caso base, que será verdadeira 
(uma vez que 10 >= 10) e então entrará na condição e fará a função recursiva(10,10) retornar fim 
(que tem valor 10). Agora que recursiva(10, 10) retornou 10, acontecerá o desempilhamento: 
Quando temos recursiva(10,10) (que vimos que retorna 10), a recursiva(9,10) também retornará 10. 
Isso acontece porque no retorno da função recursiva(9,10), teremos um return recursiva(10,10) 
(ou seja, um retorno do resultado da execução de recursiva(10,10) e como o resultado da execução de recursiva(10,10) 
é 10, então o resultado de recursiva(9,10) será a mesma coisa (10). Isso acontecerá para recursiva(8,10) também, que 
irá ter em seu retorno return recursiva(9,10), que teve o resultado de sua execução como 10 por conta do que falamos 
anteriormente, então a função recursiva(8,10) irá retornar 10 também como resultado e assim por diante, até eliminar 
todas as chamadas da call stack e printar a primeira que foi feita, com o resultado 10, obviamente


Uma observação é que nossa função recursiva pode quebrar mesmo estando correta. Se a função fosse:

def recursiva(inicio=0, fim=1000):
    if inicio >= fim: 
        return fim
    inicio += 1
    return recursiva(inicio, fim)

Ela daria o erro de StackOverFlow mesmo tendo o seu caso base, uma vez que, por ter um fim muito grande
(1000), seriam feitas varias chamadas, aí ele pode bater um limite. Podemos alterar o limite de recursão a partir 
do módulo sys e usando o .setrecursionlimit():

import sys

sys..setrecursionlimit(1004) --> Isso resolveria o problema de nossa função acima

Entendido sobre recursividade, o problema mais clássico que se resolver usando ela é o fatorial. Veja abaixo:

'''

def factorial(n):
    if n <=1:
        return 1
    return n * factorial(n-1)

'''
Primeiro, a função factorial(n) é definida e depois executada no print(). Suponha que a chamada seja 
print(factorial(5)). Na execução, entramos no escopo da função onde n = 5. Agora estamos dentro da função com n = 5. 
Como 5 <= 1 é falso, o código continua e executa return 5 * factorial(4). A partir disso, estamos chamando 
factorial(4), e a execução de factorial(5) fica em espera na call stack, aguardando o retorno dessa nova chamada. 
Agora estamos em uma nova chamada da função com n = 4. Como 4 <= 1 é falso, continuamos e chamamos novamente a 
função no return 4 * factorial(3). Isso acontece sucessivamente.

Cada chamada fica empilhada na call stack, aguardando o retorno da próxima chamada, até que cheguemos à chamada 
factorial(1). Quando n = 1, será feita a verificação do caso base, que será verdadeira (uma vez que 1 <= 1), e 
então a função retorna 1. Agora que factorial(1) retornou 1, acontece o desempilhamento: factorial(2), que tinha 
retornado a execução factorial(1), agora pode continuar sua execução. Como o retorno de factorial(1) foi 1, 
temos: return 2 * 1, isso faz com que factorial(2) retorne 2. factorial(3), que estava esperando factorial(2), 
agora recebe o valor 2 e continua: return 3 * 2, Isso faz com que factorial(3) retorne 6. factorial(4), 
que estava esperando factorial(3), agora recebe 6 e continua: return 4 * 6, isso faz com que factorial(4) retorne 24. 
factorial(5), que foi a primeira chamada feita no programa, agora recebe 24 e continua: return 5 * 24. 
Como factorial(5) foi a primeira chamada feita, o retorno final da função será 120, e este valor será impresso no 
print().


'''