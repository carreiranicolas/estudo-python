'''
*ARGS PARA A QUANTIDADE DE ARGUMENTOS NÃO NOMEADOS VARIÁVEIS

Bom, já vimos sobre parâmetros e argumentos que é algo de muita importante em funções. Vimos isso no arquivo
de conceitos. Inclusive, uma coisa que vimos no arquivo de conceito é que o print é uma função.

Algo muito importante é que se pararmos para observar, a função print pode receber inúmeros argumentos sem dar um
bug dizendo que passamos um número de argumentos não correspondente ao número de parâmetros da função. 
Mas como isso é feito?

Para isso acontecer, não precisamos colocar inúmeros parâmetros na nossa função, nós podemos utilizar um parâmetro 
chamado de *args, que é basicamente o empacotamento dos argumentos que nós passamos. 
Veja na nossa função abaixo, por exemplo:
'''

def soma(*args):
    print(args)

soma(1,2,3,4,5) # Irá retornar (1, 2, 3, 4, 5)

'''
Veja que poderíamos executar a nossa função soma passando vários argumentos NÃO NOMEADOS e não daria nenhum erro. 

Além disso, perceba que, se exibirmos o que é esse args, veremos que é uma tupla com todos os nossos argumentos.
Já tinhamos visto algo parecido com isso em empactoamento/desempacotamento de listas na parte basica, porém quando davamos
print(args), ele exibia uma lista e não uma tupla. Nas funções, ele faz isso em uma tupla porque Tuplas são imutáveis
e isso traz segurança, uma vez que argumentos não nomeados são apenas valores passados para a função 
(sem nomes específicos), então não há motivo para que sejam alterados dentro da função.

No entanto, se quiséssemos transformar em uma lista, que é um tipo mutável, poderíamos fazer isso da seguinte forma:


Agora voltando, para nós fazermos a soma de todos os valores que passamos no argumento, nós precisaríamos iterar a 
tupla a partir de um loop for e ir acumulando esses valores em uma variável, assim como fizemos abaixo:


Assim, ele iteraria, faria o acumulo dos números no total e depois nos retornaria o total

'''

