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
Um detalhe sobre váriaveis é que quando salvamos algo na memória a partir de váriaveis, esse elemento tem uma
identidade e utilizando id() em python, nós conseguimos ver a identidade do elemento que está na memória.
'''
print(id(nome))
