'''
ARGUMENTOS NOMEADOS E POSICIONAIS

Para entender, sobre assunto, vamos dizer que nós temos a seguinte função:

def soma(x,y):
    print(x + y)


Nos argumentos posicionais (não nomeados),o que acontece é que, na função soma, por exemplo, se passarmos como argumento os valores “1” e “2”, 
o valor “1” iria para o parâmetro “x” e o valor “2” iria para o parâmetro “y”. Por outro lado, se passássemos como argumento os valores “2” e “1”, 
o valor “2” iria para o parâmetro “x” e o valor “1” iria para o parâmetro “y” . Isso significa que, nos argumentos POSICIONAIS (o nome já entrega bastante), 
você deve passar os argumentos na ordem em que o parâmetro está definido. Se quiséssemos que o valor “1” fosse o “x” e o “2” fosse o “y”, por exemplo, teríamos 
que passar para função soma() primeiro o 1 e depois o 2, assim cada valor ocuparia a posição (x ou y) que queríamos que ele ocupasse

Por outro lado, nos argumentos NOMEADOS, o que acontece é que não precisamos passar os argumentos em alguma ordem específica, basta passar os argumentos para a 
função, mas definir que x=1, por exemplo, e y=2

Veja abaixo:
'''
def soma(x,y):
    print(x + y)

#EXEMPLO DE ARGUMENTOS POSICIONAIS (não nomeados)

soma(1,2) #Retornará 3, onde 1 assumirá o valor de x e 2 assumirá o valor de y, seguindo a ordem em que os parametros foram definidos e a ordem em que os argumentos foram passados


#EXEMPLO DE ARGUMENTOS POSICIONAIS

soma(y=1,x=2) #Retornará 3, onde 1 assumirá o valor de y e 2 assumirá o valor de x, seguindo o nome do parametro dado a cada argumento


'''

Uma observação é que caso você esteja chamando uma função e passando para ela argumentos posicionais E nomeados (ou seja, você está misturando os dois), depois que você definir o 
argumento nomeado, todos os argumentos que virão após o argumentos nomeado, deverão ser nomeados também, caso contrário, retornará um erro. 

Veja exemplos:

def soma(x,y):
    print(x + y)

soma(y=1, 2) --> isso dará erro

FORMA CORRETA:

def soma(x,y):
    print(x + y)

soma(1, y=2) 

A verdade é que o ideal é que ou a gente passe todos os argumentos de forma posicional, ou de forma nomeada, para não ter problema. (mas caso isso não seja possível, saiba que
existe a forma correta acima)
'''
