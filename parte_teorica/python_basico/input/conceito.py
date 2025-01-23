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
