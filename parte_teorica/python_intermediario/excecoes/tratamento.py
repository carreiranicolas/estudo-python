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

Portanto, o código acima, irá executar 

Certo, mas existe outro ponto, porque o except, caso ocorra qualquer exceção, irá exibir a mensagem 'ERRO: Divisão por 0'.
Isso é ruim, pois se ocorrer uma exceção que não seja relacionada a divisão por 0, não iremos saber sobre o que é essa
exceção, então estamos deixando de cobrir vários outros erros. Veja o código abaixo, por exemplo:


try:
    a = 18
    print('linha antes da divisão') # Isso seria exibido
    c = a/b  #Divisão por 0 que gerá a execção
    print('linha depois da divisão') #Isso não seria exibido, pois ao dar a exceção, ele iria DIRETO PARA O EXCEPT
except:
    print('ERRO: Divisão por 0') # Aconteceu a exceção na divisão de a/b e isso seria exibido logo após

print('Continua')

No exemplo acima, ele dará uma exceção (uma vez que a variavel b não foi definida, mas foi utilizada na divisão) que
tem o nome de NameError, porém a mensagem que aparecerá na exceção será 'ERRO: Divisão por 0' , sendo que sabemos que 
sabemos que nossa exceção não é ZeroDivisionError, porque a variavel b não está nem definida. Perceba então que o 
erro que apareceu nunca seria encontrado fazendo o try except da maneira que fizémos. Portanto, precisamos informar 
então qual erro em específico estamos tratando naquela exceção especificamente. Veja como fazer isso:

try:
    a = 18
    b = 0
    print('linha antes da divisão') # Isso seria exibido
    c = a/b  #Divisão por 0 que gerá a execção
    print('linha depois da divisão') #Isso não seria exibido, pois ao dar a exceção, ele iria DIRETO PARA O EXCEPT
except ZeroDivisionError:
    print('ERRO: Divisão por 0') # Aconteceu a exceção na divisão de a/b e isso seria exibido logo após

print('Continua')

Portanto, podemos ver que o erro de divisão por 0 acima foi tratado. Agora se ocorresse um erro que não fosse 
divisão por 0, ele apareceria para nós, o que não acontecia no caso anterior, pois para todas as exceções ele exibia
a mensagem 'ERRO: Divisão por 0'. Agora, da forma que fizemos, somente se fosse um erro de divisão por zero que ele
exibiria essa mensagem. Veja abaixo:


try:
    a = 18

    print('linha antes da divisão') # Isso seria exibido
    c = a/b  #Divisão por 0 que gerá a execção
    print('linha depois da divisão') #Isso não seria exibido, pois ao dar a exceção, ele iria DIRETO PARA O EXCEPT
except ZeroDivisionError:
    print('ERRO: Divisão por 0') # Aconteceu a exceção na divisão de a/b e isso seria exibido logo após

print('Continua')

Acima, nós temos aquele caso onde a váriavel b não está definida e foi utilizada na divisão. Isso resultaria em uma
exceção que já vimos que é NameError. Agora, utilizando o except da forma que estamos utilizando acima, a exceção
do NameErro apareceria para nós e não a mensagem 'ERRO: Divisão por 0', uma vez que essa mensagem só será exibida 
quando tivermos um ZeroDivisionError.

Mas agora surge um questionamento. Como podemos tratar essa exceção de NameError sendo que já temos um except? Bastaria
utilizar outro except com o nome da exceção, assim trataremos outro erro. Veja abaixo:

try:
    a = 18

    print('linha antes da divisão') # Isso seria exibido
    c = a/b  #Divisão por 0 que gerá a execção
    print('linha depois da divisão') #Isso não seria exibido, pois ao dar a exceção, ele iria DIRETO PARA O EXCEPT
except ZeroDivisionError:
    print('ERRO: Divisão por 0') # Aconteceu a exceção na divisão de a/b e isso seria exibido logo após
except NameError:
    print('ERRO: Variavel não definida')

print('Continua')

Agora, como a variavel b não está definida dará uma exceção NameError, que irá pular direto para o except do 
NameError e exibir a mensagem 'ERRO: Variavel não definida'. 

Uma coisa que poderíamos fazer é utilizar a exceção Exception. Ela é a classe superior que trata qualquer erro
(chegamos a citar isso no arquivo de conceito). Então, no nosso código acima, se incluirmos um except com o 
Exception, qualquer erro que não for ZeroDivisionError ou NameError, irá para o except da Exception. Veja abaixo

try:
    a = 18
    b = 0
    print(a[0])
    print('linha antes da divisão') # Isso seria exibido
    c = a/b  #Divisão por 0 que gerá a execção
    print('linha depois da divisão') #Isso não seria exibido, pois ao dar a exceção, ele iria DIRETO PARA O EXCEPT
except ZeroDivisionError:
    print('ERRO: Divisão por 0') # Aconteceu a exceção na divisão de a/b e isso seria exibido logo após
except NameError:
    print('ERRO: Variavel não definida')
except Exception:
    print('ERRO DESCONHECIDO')

print('Continua')

No código acima, estamos tentando acessar um indice de um inteiro. Isso não é possivel. Isso dispararia uma exceção
que não está relacionada a ZeroDivisionError e nem a NameError, então iria para o except do Exception, exibindo assim
a mensagem 'ERRO DESCONHECIDO'

Uma coisa interessante que poderíamos fazer é utilizar tuplas para passar mais de uma exceção no mesmo except.
Assim, as exceções serão capturadas e poderão ser tratadas no mesmo except. Veja:

try:
    a = 18
    b = 0
    print('linha antes da divisão') # Isso seria exibido
    c = a/b  #Divisão por 0 que gerá a execção
    print('linha depois da divisão') #Isso não seria exibido, pois ao dar a exceção, ele iria DIRETO PARA O EXCEPT
except (ZeroDivisionError, NameError):
    print('ERRO: Divisão por 0 + Name error') # Aconteceu a exceção na divisão de a/b e isso seria exibido logo após
except Exception:
    print('ERRO DESCONHECIDO')

print('Continua')

Acima, seria feita a divisão por zero e resultaria em uma exceção, ai ele iria para o except que tem o ZeroDivisionError
(que inclusive tem junto dele a exceção NameError) e exibiria a mensagem 'ERRO: Divisão por 0 + Name error'

Uma observação é que caso você tiver um except de mais de uma exceção e  precise tratar uma exceção específica que 
ocorreu, faz mais sentido você fazer um except só para aquela exceção específica 

Certo, outra coisa que dá pra fazer é dar um alias para o erro. Esse alias meio que captura a mensagem da exceção. 
Na nossa tupla com os erros de ZeroDivisionError e NameError, por exemplo, poderiamos dar um aliás para o erro e 
depois dar um print(erro) dentro. Veja abaixo para entendermos melhor:

try:
    a = 18
    b = 0
    print('linha antes da divisão') # Isso seria exibido
    c = a/b  #Divisão por 0 que gerá a execção
    print('linha depois da divisão') #Isso não seria exibido, pois ao dar a exceção, ele iria DIRETO PARA O EXCEPT
except (ZeroDivisionError, NameError) as error:
    print('ERRO: Divisão por 0 + Name error') # Aconteceu a exceção na divisão de a/b e isso seria exibido logo após
    print(erro)
except Exception:
    print('ERRO DESCONHECIDO')

print('Continua')


No código acima, daria a exceção de divisão por zero, então ele iria direto para o except onde está o ZeroDivisionError
e portanto exibiria a mensagem: 'ERRO: Divisão por 0 + Name error' e logo depois, com o print(error), exibiria a 
mensagem do ZeroDivisionError, que é: division by zero

Algo interessante é que a partir da mensagem da exceção, poderíamos pegar o nome da exceção fazendo error.__class__.__name__
Veja no código abaixo:

try:
    a = 18
    b = 0
    print('linha antes da divisão') # Isso seria exibido
    c = a/b  #Divisão por 0 que gerá a execção
    print('linha depois da divisão') #Isso não seria exibido, pois ao dar a exceção, ele iria DIRETO PARA O EXCEPT
except (ZeroDivisionError, NameError) as error:
    print('ERRO: Divisão por 0 + Name error') # Aconteceu a exceção na divisão de a/b e isso seria exibido logo após
    print(erro)
    print(error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('Continua')


Acima, daria uma exceção de divisão por zero, então iria direto para o except do ZeroDivisionError, exibindo assim
a mensagem 'ERRO: Divisão por 0 + Name error', a mensagem da exceção (division by zero) que foi capturada a partir do 
alias (as error) e depois o nome da Exceção que é ZeroDivisionError que foi recuperada a partir da mensagem da exceção
por error.__class__.__name__

'''
