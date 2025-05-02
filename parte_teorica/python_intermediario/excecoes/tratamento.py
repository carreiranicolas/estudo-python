'''
TRATAMENTO DE EXCEÇÕES

Bom, agora que já entendemos o que são as exceções, temos que ver como tratamos elas,
mas antes, o que é o tratamento de exceções?

Tratar uma exceção significa capturar o erro quando ele ocorre (veremos como fazer isso) 
e tomar uma ação apropriada — como exibir uma mensagem amigável, registrar um log ou seguir 
com uma alternativa.


Para tratar exceções, vamos utilizar o try-except em python (veremos depois mais algumas
clásulas que servirão para o tratamento de execções). Para entendermos, vamos supor que
nós tenhamos o código abaixo:
'''

a = 18

b = 0

c = a/b #Aqui teremos uma divisão por zero, que gerará uma exceção (parar o programa e mostrar um erro)

try:
    ...
except:
    ...

print('Continua') #Não será executado

'''
Quando executamos o código acima, acontecerá o erro ZeroDivisionError: division by zero

Isso acontece porque em c = a/b, estamos dividindo 18 por 0 e não existe divisão por 0,
levantando uma exceção, então todo o código que vem depois não será nunca executado quando tivermos 
a exceção (o print('Continua') não acontece). Caso não tivéssemos 0 como o valor de “b” e tivéssemos 2, 
por exemplo, a divisão seria feita e não levantaria nenhuma exceção, executando o restante do código (o
print('Continua') seria executado).

Agora, suponhamos que coloquemos a divisão c = a/b dentro do try, como no código abaixo:

a = 18

b = 0


try:
    c = a/b 
except:
    ...

print('Continua')


No código acima, o print('Continua') será executado. O que acontece é que não haverá a interrupção
do programa porque o try serve para EVITAR QUE O PROGRAMA SEJA INTERROMPIDO POR UMA EXCEÇÃO NÃO
TRATADA. Além disso, estamos cometendo uma MÁ PRÁTICA no código acima, pois estamos SILENCIANDO
o ERRO. Estamos silenciando o erro porque quando a exceção ocorre dentro do try, ele pula 
imediatamente para o except, porém, no código acima, não temos nada no except, então ele
não exibe nada (nem uma mensagem ou algo do tipo) e segue com a execução do programa, executando
assim o print('Continua'), que está logo abaixo.

Outra coisa que poderíamos ter feito é:

a = 18

b = 0


try:
    c = a/b 
except:
    print('ERRO: Divisão por 0')

print('Continua')

No código acima, estariamos fazendo algo que não é muito interessante também, pois estamos cobrindo 
o erro de divisão por 0, mas se no nosso código ocorresse outro erro além da divisão por 0? Ele não 
seria coberto.

Enfim, agora para simplificarmos, o fluxo do try-except é:

O try irá executar o nosso código e se ocorrer uma execção --> pula direto para o except e 
executa o que tem lá dentro --> se tiver código depois, será executado

Veja na prática isso acontecendo:


try:
    a = 18
    b = 0
    print('linha antes da divisão') # Isso seria exibido
    c = a/b  #Divisão por 0 que gerá a execção
    print('linha depois da divisão') #Isso não seria exibido, pois ao dar a exceção, ele iria DIRETO PARA O EXCEPT
except:
    print('ERRO: Divisão por 0') # Aconteceu a exceção na divisão de a/b e isso seria exibido logo após

print('Continua')


'''