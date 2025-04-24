import decimal #Você entenderá nas explicações mais abaixo

'''
FLOATS

Já citamos rapidamente no arquivo de tipos de dados que numeros floats são basicamente
números decimais. Ou seja, números com virgulas. Para usar esse tipo de dados, basta digitar um número, depois
digitar um ponto com outros números em seguida. Veja:

1.12

Ele é um tipo númerico normal, podemos utiliza-lo com todos os operadores numéricos para fazer as operações
normalmente

Números decimais em qualquer linguagem de programação é algo um pouco problematico, pois existem algumas coisas
relacionadas a imprecisões e arredondamentos

Veja na prática
'''

print(0.1 + 0.2)  # retorna 0.30000000000000004, o que é incorreto

print(0.1 + 0.7) # retorna 0.7999999999999999, o que é incorreto


#Para contornar isso, podemos utilizar o print formatado


print(f'{0.1 + 0.2: .2f}') #Retorna  0.30

print(f'{0.1 + 0.7: .2f}') #Retorna  0.80

# Outra forma seria utilizando a função round, onde fazemos round(numero, casas decimais). Veja:

print(round(0.1 + 0.2, 3)) #Retorna  0.3

print(round(0.1 + 0.7, 2)) #Retorna  0.8

'''
Uma observação é que o round não irá nos mostrar os zeros que não tem importância em um float, então 
se tivermos o número 0.800000000, ele só irá me mostrar 0.8, pois os zeros não tem valor/importância nesse caso. 

'''

'''
Outra forma, seria importar o modulo decimal (veremos melhor sobre importação de modulos em python intermediario)
e utilizar a função Decimal dela. 

Existem duas formas de utiliza-la: Passando para dentro do parâmetro da função um float ou passando para dentro do 
parâmetro da função uma string de um float. No entando, existe até uma questão envolvendo a primeira forma


Veja na prática:
'''
n1 = decimal.Decimal(0.1)

n2 = decimal.Decimal(0.2)

print(n1 + n2) # Irá retornar 0.3000000000000000166533453694

'''
Portanto, perceba que o nosso problema ficou maior ainda. Com isso, a recomendação é que se use uma string de um float

Veja prática
'''

n1 = decimal.Decimal('0.1')
n2 = decimal.Decimal('0.2')

print(n1 + n2)