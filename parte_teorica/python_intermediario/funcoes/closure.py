'''
CLOSURE

Falando sobre conceito, podemos dzer que closure é quando uma função interna acessa variáveis do escopo de uma 
função externa mesmo após a função externa ter sido encerrada.

Para entender melhor sobre closure, vamos a um exemplo:
'''

def saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

saudacao1 =saudacao('Bom dia', 'Nicolas')
saudacao2 = saudacao('Bom dia', 'Luiza')
print(saudacao1) # Retorna: Bom dia, Nicolas
print(saudacao2) #Retorna: Bom dia, Luiza

'''
Agora pare para pensar o seguinte: Se estivermos utilizando várias vezes a função saudacao e mudando apenas o 
bom dia para boa noite e tivermos que ficar mudando os nomes que passamos toda hora também? Isso não é nada dinamico,
correto?

Podemos utilizar do closure para tornar isso mais dinamico, facilitar esse processo. Vamos primeiro detalhar closure,
depois vamos fazer essa saudacao dinamica:
'''

def saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar

saudacao1 = saudacao('Bom dia', 'Nicolas')
saudacao2 = saudacao('Bom dia', 'Luiza')

'''
Ao fazermos isso que fizemos acima, o que acontece é que estamos criando a funcao saudacao que recebe os parametros
saudacao e nome. Além disso, a funcao saudar é definida dentro da funcao saudacao e retorna a saudacao e o nome em
uma string. Por fim, a funcao saudar (SEM SER EXECUTADA!!) é retornada da funcao saudacao.

Quando fazemos saudacao1 =  saudacao('Bom dia', 'Nicolas') e saudacao2 = saudacao('Bom dia', 'Luiza'), o que acontece
é que estamos executando a função saudacao com os argumentos que passamos. Como a funcao saudacao está retornando
o alocamento na memória da função saudar, as variaveis saudacao1 e saudacao2, irão armazenar o local da memória
da funcao saudar com os argumentos da funcao saudacao passados para dentro dela ('Bom dia' e 'Nicolas' no caso de 
saudacao1 e 'Bom dia' e 'Luiza' no caso de saudacao2)

Se fizermos print(saudacao1) e print(saudacao2), por exemplo, será exibido o local da memória onde está. É 
importante observar que apesar de ser as mesmas funções que estão sendo utilizadas em ambas as variaveis 
(saudacao1 e saudacao2), elas estão alocadas em lugares diferentes na memória. Isso significa que ele está criando 
duas funções separadas (uma vai para saudacao1 e outra para saudaca2) 

Agora, se fizermos:

print(saudacao1())
print(saudacao2())

As duas serão executadas, retornando, respectivamente: 

Bom dia, Nicolas 
Bom dia, Luiza

Dessa forma closure (fechamente em portugues) significa que a função que tinha ficado em aberto 
(pois não retornamos nenhum valor da função saudacao, apenas um alocamento da memória da função saudar) será 
fechada ao colocarmos o parenteses do lado da variavel e executar o que deveria ter sido executado, concluindo por 
total a função. 

Agora que entendemos o closure de fato, pra lidar com aquele caso onde usaríamos o closure para fazer um bom dia e 
um boa noite dinamico, nós faríamos:
'''

def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

saudacao1 = saudacao('Bom dia')
saudacao2 = saudacao('Boa noite')
print(saudacao1('José'))
print(saudacao2('José'))

'''
Nós padronizamos o 'Bom dia' e 'Boa noite' (Isso acontece porque será executada a função saudacao, que irá receber o 
argumento saudacao, depois irá criar a função saudar (que deve receber o parametro nome) e irá passar o argumento 
saudacao recebido para a função saudar, pois o escopo dela permite que isso aconteça) e lá no closure, 
nós podemos tornar a execução da nossa função dinâmica, passando o nome que quisermos para ela. Ou seja, é como se 
estivéssemos executando a função saudar de forma separada (e utilizando para isso apenas a função saudacao), para 
torná-la mais dinamica, podendo ser utilizada em problemas mais robustos. Se recebessemos uma lista de nomes e 
tivéssemos que dar bom dia e boa noite para cada nome, poderíamos utilizar isso que fizémos acima, por exemplo. 
Veja abaixo:
'''

def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = saudacao('Bom dia')
falar_boa_noite = saudacao('Boa noite')

for nome in ['Maria', 'João', 'José', 'Felipe']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
