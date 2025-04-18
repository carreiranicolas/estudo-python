'''
Veja agora alguns métodos interessantes que podemos utilizar com strings
'''

string = 'nicolas'

# Método capitalize: Torna o primeiro caracter da string maiusculo

print(string.capitalize()) # Retornará 'Nicolas'

# Método upper: Converte todos os caracteres para maiúsculas

print(string.upper()) # Retornará 'NICOLAS'

# Método lower: Converte todos os caracteres para minusculas

print(string.lower()) # Retornará 'nicolas'

# Método replace: Substitui partes da string por partes que quisermos

print(string.replace('s', 'u')) #Retornará 'nicolau'

# Método count: Conta quantas vezes um parametro aparece na string

print(string.count('s')) #Retornará 1

# Método startswith: Irá retornar um bool checando se a string começa com o valor do parametro

print(string.startswith('n')) # Retornará True

# Método endswith: Irá retornar um bool checando se a string começa com o valor do parametro

print(string.endswith('s')) # Retornará True

# Método isalpha: Irá retornar um bool checando se a string tem apenas letras

print(string.isalpha()) #Retornará True

# Método isdigit: Irá retornar um bool checando se a string tem apenas digitos (numeros)

print(string.isdigit()) #Retornará False

# Método isspace: Irá retornar um bool checando se a string tem apenas espaços

print(string.isspace()) #Irá retornar False

# Método isalnum: Irá retornar um bool checando se a string tem apenas letras ou numeros, sem espaço ou simbolos

print(string.isalnum()) #Irá retornar True

# Método islower: Irá retornar um bool checando se a string tem todos os caracteres minusculos

print(string.islower()) #Irá retornar True

# Método isupper: Irá retornar um bool checando se a string tem todos os caracteres maiusculos

print(string.isupper()) #Irá retornar False

# Método find: Irá retornar o indice 




'''
Além dos métodos de string que vimos acima, temos alguns métodos um pouco mais complexos que
requerem uma explicação mais detalhada para o entendimentos. São eles: split, join e strip

--> SPLIT

O split  divide uma string em determinado caractere que você passar como parâmetro 
(Observação: Se não passarmos nada como parâmetro, ele irá, por padrão, dividir as strings por espaços 
em branco).


--> STRIP

corta pedaços do começo e do fim da string. Se não passarmos nada como parâmetro, será cortado os espaços 
em branco da string que estiverem no começo e no final ). 

O strip ainda tem suas variações, que é  o rstrip, que corta só os pedaços da direita e o lstrip, que corta 
só os pedaços da esquerda


--> JOIN

basicamente une strings. Dentro do parâmetro do join, nós vamos passar nosso iterável (nossa string) e antes 
do .join, vamos passar uma outra string, pois vai ser aí que diremos qual separador iremos utilizar para unir 
a nossa string. Ou seja, será o SEPARADOR que UNE a STRING que passamos como parâmetro no join

Vamos aos exemplos:
'''

#Exemplo de SPLIT


#Exemplo de STRIP


#Exemplo de Join

