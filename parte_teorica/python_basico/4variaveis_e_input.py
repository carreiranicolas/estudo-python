'''
VARIAVEIS

Uma coisa extremamente importante em qualquer que seja a linguagem que estejamos trabalhando são as váriaveis.

As variáveis são usadas para salvar algo na memoria do computador, ou seja, uma váriavel armazena valores.

Devemos escrever variáveis com letras minúsculas, podemos usar números após essa letra minúscula e podemos usar underlines para separar palavras compostas 

Para criar uma variável em Python basta usar: nome_variavel = valor que queremos passar. Exemplo: nome = ‘Nicolas’. Neste exemplo, passamos uma string ‘Nicolas’ como valor
para a nossa varíavel.

Variáveis não são usadas para abreviar código, muito pelo contrário. Variáveis são feitas para você fazer o código mais legível e para você não repetir código
em lugares que você vai usar a mesma coisa (mesmo valor)

'''

nome = 'José'
idade = 20
maior_de_idade = idade >= 18 #Neste caso, como passamos uma operação para essa váriavel, o valor que será armazenado nesta varíavel é booleano (True ou Falso)




'''
INPUT

Uma outra coisa muito importante em diversas lingugens da computação é a coleta de dados.

Em Python, para coletarmos dados do usuário usamos a função “input()”. A função dados por si só não faz nada, apenas coleta dados. PORÉM, o que podemos fazer é 
criar uma variável para armazenar o dado que foi recolhido. Exemplo: nome = input(‘Qual o seu nome’). Vale ressaltar que o input rexebe dados no tipo string e SOMENTE 
nesse tipo, portanto é importante saber coerção de tipos

Essa coerção pode ser feita na própria função input (apesar de não ser muito recomendado) da seguinte forma: idade = int(input(‘Qual sua idade’))

'''

nome = input('Qual o seu nome: ') #Nesse caso, não vamos fazer coerção porque queremos string mesmo
idade = int(input('Qual sua idade: ')) #Nesse caso, vamos fazer coerção porque queremos a idade, que é um número

print(nome, idade)
