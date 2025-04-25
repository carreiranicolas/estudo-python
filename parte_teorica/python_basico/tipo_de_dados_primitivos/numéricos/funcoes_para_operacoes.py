import math #Avance na explicação para entender

'''
Existem funções prontas em python para realizar algumas operações. Isso é muito interessante, pois
facilita a lógica do nosso código. 

Veja abaixo:
'''

#Funções Nativas (podem ser usado sem ter que dar import em nada):


#--> Valor absoluto 'abs': Cálcula basicamente o módulo de um número, sempre retornará positivo

print(abs(-5)) #Retornará 5

#--> Potencia 'pow': Cálcula basicamente a potência. Para isso passamos o número e o expoente

print(pow(2,3)) #Retornará 8

#--> div e mod 'divmod': Cálcula basicamente a divisão inteiro de dois numeros (//) e o resto da divisão deles

print(divmod(10,3)) #Retornará uma tupla: (3,1)

#--> maximo 'max': Cálcula o maior valor passado alguns numeros como parametro

print(max(3,7,6)) #Retornará 7

#--> minimo 'min': Cálcula o menor valor passado alguns numeros como parametro

print(max(3,7,6)) #Retornará 3

#--> Soma 'sum': Cálcula a soma dos valores passados dentro de um iteravel e somente em iteraveis

print(sum([2,3,5,6])) #Retornará 16


'''
Além dessas funções que vimos acima, tem outras funções que podem ser utilizadas ao fazermos
um import math. Dentro dela temos algumas funções mais cabulosas
'''

#Funções da biblioteca math (podem ser usadas dando import math):


#--> Fatorial 'math.factorial': Cácula o fatorial de um número

print(math.factorial(5)) #Retornará 120

#--> Raiz quadrada 'math.sqrt': Cácula a raiz quadrada de um número

print(math.sqrt(9)) #Retornará 3.0

#--> Arredondar para cima 'math.ceil': Arredonda para o inteiro mais próximo acima

print(math.ceil(2.3)) #Retornará 3

#--> Arredondar para baixo 'math.floor': Arredonda para o inteiro mais próximo abaixo

print(math.floor(2.9)) #Retornará 2

#--> Truncar número 'math.trunc': Remove a parte decimal de um número

print(math.trunc(3.9)) #Retornará 3

#--> Logaritmo natural 'math.log': Cálcula o logaritmo natural de um número

print(math.log(10)) #Retornará 2.302585092994046

#--> Logaritmo base 10 'math.log10': Cálcula o logaritmo na base 10 de um numero

print(math.log10(1000)) #Retornará 3.0

#--> Logaritmo base 2 'math.log2': Cálcula o logaritmo na base 2 de um numero

print(math.log2(8)) #Retornará 3.0

#--> Exponencial 'math.exp': Cálcula o valor de e (exponencial) elevado pelo numero passado

print(math.exp(1)) #Retornará 2.718281828459045

#--> Máximo divisor comum 'math.gcd': Cálcula o maior divisor comum entre dois números

print(math.gcd(12, 18)) #Retornará 6

#--> Mínimo múltiplo comum 'math.lcm': Cálcula o menor múltiplo comum entre dois números

print(math.lcm(4, 6)) #Retornará 12

#--> Raiz quadrada inteira 'math.isqrt': Cálcula a raiz quadrada inteira de um número

print(math.isqrt(10)) #Retornará 3

#--> Copiar sinal 'math.copysign': Copia o sinal de um número para outro

print(math.copysign(3, -1)) #Retornará -3.0

#--> Resto da divisão 'math.fmod': Cálcula o resto da divisão com sinal

print(math.fmod(5, 3)) #Retornará 2.0

#--> Verificar proximidade 'math.isclose': Verifica se dois números são próximos

print(math.isclose(1.0, 0.9999, rel_tol=1e-3)) #Retornará True

#--> Converter para graus 'math.degrees': Converte o radiano passado em graus

print(math.degrees(math.pi)) #Retornará 180.0

#observação: com o modulo math, temos acesso ao valor de pi usando math.pi

#--> Converter para radianos 'math.radians': Converte o grau passado em radianos

print(math.radians(180)) #Retornará 3.141592653589793
