'''
OPERADORES DE ATRIVUIÇÃO

Os operadores de atribuição servem para atribuir valores a variáveis. Eles basicamente
são uma mão na roda para simplificar nosso código. Veja abaixo um exemplo de código com
o operatodr de atribuição e sem 

SEM O OPERADOR DE ATRIBUIÇÃO:

variavel = variavel += 1 (novo valor da variavel será o antigo valor + 1)

COM O OPERADOR DE ATRIBUIÇÃO:

variavel += 1  (novo valor da variavel será o antigo valor + 1)


Os operadores de atribuição:

 = → é o mais básico, faz uma atribuição simples

 += → soma um valor à variavel

 -= → subtrai um valor à variavel

 *= → multiplica um valor à variavel

 **= → exponencia a variavel a um dado valor

 /= → divide a variael por um dado valor

 //= → faz uma divisão inteira da variael por um dado valor

 %= → pega o resto da divisão da variavel por um número e atribui à variavel o valor do resto
'''

#ALGUNS EXEMPLOS

variavel = 10 # Fizemos a atribuição simples do valor 10 à variavel

print('atribui',variavel) #Retornará 10

variavel += 1 #Somamos 1 a variavel

print('soma 1',variavel) #Retornará 11

variavel -= 1 #Subtraimos 1 a variavel

print('subtrai 1',variavel) #Retornará 10

variavel *= 2 # Multiplica a variavel por 2

print('multiplica por 2',variavel) #Retornará 20

variavel **= 2 #Exponencia a variavel por 2

print('exponencia',variavel) #Retornará 400

variavel /= 2 #Divide a variavel por 2

print('divide por 2',variavel) #Retornará 200

variavel //= 16 #Irá fazer a divisão inteira da variavel e atribuir à variavel esse valor

print('divisão inteira',variavel) #Retornará 12 (desconsidera o resto)

variavel %= 2 #Irá pegar o resto da divisão da variavel por 2 e atribuir à variavel esse valor

print('reste de divisão por 16',variavel) #Retornará 0
