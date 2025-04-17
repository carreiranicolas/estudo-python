'''
--> FORMATAÇÃO DE STRINGS (f-strings)

Usando o f-string nós habilitamos a possibilidade de utilizar váriaveis dentro de strings. Isso é bem útil
em diversos contextos, uma vez que com o uso de f-string, precisaríamos ter o trabalho de ficar colocando 
várias vírgulas durante a função print para exibir o texto com as variaveis, que seria bem trabalhoso

'''

variavel_idade = 20
variavel_altura = 1.72

texto = f'Tenho {variavel_idade} anos de idade e {variavel_altura} de altura'

print(texto) #Nesse texto, teremos exibido: Tenho 20 anos de idade e 1.72 de altura



#Outro detalhe do f-string é que podemos especificar quantas casas decimais queremos exibir nos números float. Veja:


variavel_peso = 70.802

texto2 = f'Tenho {variavel_peso:.1f} quilos' #Estamos especificando 1 casa decimal para nosso float variavel_peso

print(texto2) #Será exibido: Tenho 70.8 quilos

'''
Uma curiosidade em f-strings é que podemos colocar pad nas variaveis, ou seja, colocar alinhamento nas variaveis dentro de f-string.
A estrutura é print(f'{variavel: >10}') ou print(f'{variavel: <10}') ou print(f'{variavel: ^10}'), sendo “>” alinhamento à direita , 
“<” alinhamento à esquerda e “^” centraliza. Veja:
'''

var = 'alinhe'

print(f'{var: >10}') #Será alinhado em 10 à direita
#print(f'{var:< 10}') #Será alinhado em 10 à esquerda (como está colado na esquerda, não mudará nada)
print(f'{var: ^10}') #Será centralziado em 10


#Uma última curiosidade é que nas f-strings podemos obter o hexadecimal de algum número. Veja:

print(f'O hexadecimal de 15 é {15:x}')

'''
--> FORMATANDO STRINGS COM FORMAT

Outra forma de utilizar a formatação de strings é utilizando a funçãozinha “format”.
Veja sua estrutura abaixo: 
'''

a = 'AAAA'
b = 'B'
c = 1.72

formatando = 'a={}'.format(a,b,c) 
print(formatando) #Será exibido a=AAAA

'''
O que acontece acima é que dentro do parênteses do “.format”, nós vamos passar como argumento as variáveis. 
A partir disso, nós temos uma string, onde dentro das chaves {} será substituido o valor de cada variável, 
NA ORDEM EM QUE ESTIVER OS ARGUMENTOS, então se o primeiro argumento dentro do parênteses .format fosse a variável “b”, 
então seria exibido para nós “a=B”, pois a váriavel que vai para dentro do parênteses está na ordem. Nesse caso, 
o primeiro argumento era a variável “a”, então foi exibido AAAA
'''

'''
Caso não queiramos depender da ordem, bastaria nomear os argumentos dentro do formaat e passar para as chaves {} o nome do argumento, 
funcionaria também. Veja:
'''

a2 ='A2'
b2 = 'B2'
c2 = 1.82

formatando2 = 'a2={azinho} b2={bzinho} c2={czinho}'.format(azinho=a2, bzinho=b2, czinho=c2) #Demos meio que um "aliás" para os argumentos para passar eles para as chves {}
print(formatando2) #Será exibido a2=A2 b2=B2 c2=1.82 (ou seja, conforme o local que botamos os argumentos nomeados)

#Outro detalhe é que obviamente poderíamos definir quantas casas decimais queremos exibir para algum número. Veja:

argumento = 1.11
argumento2 = 1.71

formatando3 = 'argumento={:.1f} argumento2={:.5f}'.format(argumento, argumento2)
print(formatando3) # Será exibido argumento=1.1 argumento2=1.71000

# Um último detalhe do format é que poderíamos obter o hexadecimal de algum número fazendo:
n1= 12

hexa_format = formatando3 = 'n1={}, n1 hexa={:x}'.format(n1, n1)
print(hexa_format) # Será exibido: o hexadecimal de 12 é c

'''
--> INTERPOLAÇÃO DE STRING COM %

Interpolação é basicamente a mesma coisa que fizemos com o format, mas dessa vez, de um jeito diferente. É uma outra forma de formatação de strings.
Veja:
'''
name = 'Nicolas'
age = 19

#  para strings usamos %s, para int usamos %d e %i, para float usamos %f, para hexadecimal %x ou %X

variavel_text = '%s tem %i anos'%(name,age) # os valores precisam estar respectivos nos parenteses

print(variavel_text) # Irá exibir: Nicolas tem 19 anos

# Uma curiosidade é que poderíamos ver o hexadecimal de algum número usando a interpolação (%) da seguinte forma:

hexa_text = 'o hexadecimal de %i é %x'%(12,12)
print(hexa_text) # Iria exibir: o hexadecimal de 12 é c