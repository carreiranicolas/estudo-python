'''
VALORES PADRÃO PARA PARÂMETROS DE FUNÇÕES

Uma outra coisa interessante que em funções Python, podemos definir valores de parametros padrões 
para nossas funções, assim, caso o usuário não forneça nenhum argumento para aquele parametro, ao 
chamar a função, o valor padrão que foi definido no parametro da função será utilizado.

Vejamos um exemplo abaixo:

'''

def soma(x,y,z=0):
    print(x+y+z)

soma(1,2) #Irá retornar 3

soma(1,2,1) # Irá retornar 4

'''
Portanto, perceba que nossa função funcionou perfeitamente. Quando não passamos o argumento do parametro z,
o valor padrão do parametro z foi utilizado e quando passamos um argumento para o parametro z, o argumento
que passamos foi utilizado. 

Se não tivéssemos o valor de parametro padrão e nossa função fosse:

def soma(x,y,z):
    print(x+y+z)

Se fizessemos soma(1,2), isso daria erro, uma vez que o argumento do parametro z é OBRIGATÓRIO. Como vimos,
ele só se tornará opcional se utilizarmos o valor de parametro padrão, como fizémos mais acima.

Agora suponha que nossa função seja a função abaixo:
'''

def somando(x,y,z=0):
    if z:
        print(f'{x=} {y=} {z=}', x + y +z)
    else:
        print(f'{x=} {y=}', x + y)

'''
Na função cima, se a pessoa enviar o valor de z, o que deveria acontecer, na teoria, é o if ser executado exibindo 
o valor de x, y e z e exibindo a soma deles. Caso contrário (a pessoa não enviar o valor de z) seria exibido apenas o valor de x e y e a soma deles. 
Porém, note o que acontece se passarmos o z como 0 nos argumentos: 
'''

somando(1,2,0) #Irá retornar: x=1 y=2 3

'''
Acima, quando passamos os argumentos e executamos a função, ele nos retorna x=1 y=2 3. Ou seja, ele entrou no if e não
no else (que é o que queriamos e esperavamos ao passar qualquer argumento para o parametro z). Isso acontece porque
o valor (o argumento) que passamos para o parametro z foi 0 e como sabemos que 0 é um valor considerado False, ele não
entra no if e então ele roda o código do else, que é o código onde nós não passamos valores para z nos argumentos 
(o que não é o caso, pois nós passámos 0 como argumento para z). Para resolver esse problema, uma das maneiras muito 
utilizadas nas funções é ir lá nos parametros definir o valor padrão de z como None (não valor). Isso nos permite utilizar o is None e o 
is not None para resolver nosso problema.

Veja abaixo:
'''

def somandoo(x,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y +z)
    else:
        print(f'{x=} {y=}', x + y)


somandoo(1,2,0) #Irá retornar: x=1 y=2 z=0 3


'''
Perceba que agora deu certo. Passamos o valor 0 como argumento e ele executou o que queríamos. Isso aconteceu porque como o parametro de z é None (que é um não valor), 
quando passamos um argumento 0, mesmo que 0 seja considerado False, ele ainda é um valor. Sabendo disso, z deixará de ser um None(não valor), executando assim a condição 
if z is not None e fazendo o que queríamos. 
'''