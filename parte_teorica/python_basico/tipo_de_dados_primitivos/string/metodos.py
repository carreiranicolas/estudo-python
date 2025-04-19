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

# Método find: retorna o indice onde temos a primeira ocorrencia do parametro que você passar (se não encontrou = -1)

print(string.find('s')) #Retorna 6, que é o indice da string que aparece a letra 's'


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

frase = 'Oi, tudo bem com você, meu amigo' 

print(frase.split(',')) 

'''
O exemplo acima irá retornar uma lista: ['Oi', ' tudo bem com você', ' meu amigo']. Perceba que são três 
elementos. Nós temos o 'oi', que tem uma virgula que o separa de 'tudo bem com você', que por sua vez tem
uma virgula que o separa de 'meu amigo'. Como passamos para o split o caracter ',', ele irá dividir os 
elementos da string a partir da virgula, gerando 3 elementos ('oi', 'tudo bem com você', 'meu amigo') que
são todos separados por virgula

'''


#Exemplo de STRIP

palavra_com_espacamento = ' ' * 20 + 'oi' #Adicionando espacamento a nossa palavra 'oi'
print(palavra_com_espacamento) # Aqui estamos mostrando como fica nossa palavra com o espaçamento
print(palavra_com_espacamento.strip()) # Aqui nos mostramos a aplicação do strip cortando o espaçamento

'''
No exemplo acima, nós adicionamos um espacamento a nossa palavra só para conseguir visualizar a aplicação
do strip(). Quando aplicamos o strip à palavra com o espaçamento, ele cortará o espaçamento e deirará só
a palavra

'''
#Exemplo de Join

frases_unidas = '-'.join('abc')
print(frases_unidas)

'''
No exemplo acima, teremos como retorno a-b-c.  Na prática, o que acontece é que para cada item do 
nosso iterável que está dentro do join, você adiciona a string que está antes do join (o separador)
'''

