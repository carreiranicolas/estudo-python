'''
ESCOPO DE FUNÇÕES 

Em python (e em qualquer linguagem), algo muito importante de se entender é sobre o escpo das funções. 
Escopo significa o local onde aquele código pode atingir. Ou seja, se eu tenho um escopo fechado dentro de uma função, quer 
dizer que o meu código não vai afetar o que estiver fora da função. O que fazemos dentro da função, fica na função.

Vamos entender com um exemplo prático:
'''

def escopo():
    x = 1
    print(x)


#print(x) -->Se tentarmos fazer isso, ele nos retorna um erro dizendo que a variavel x não está definida.

'''
Isso acima acontece porque a variável x até está definida, porém ela está definida dentro do ESCOPO DA FUNÇÃO, o nome
disso é ESCOPO LOCAL (variáveis criadas dentro de uma função, que só existem ali dentro). Portanto, como diz o 
ditado: O que fazemos dentro da função, fica dentro da função

Agora, se formos definir a variavel x fora da função e quisermos utiliza-la dentro da função, podemos fazer isso de duas
formas:

----------------------------------------------------------------------
# FORMA 1 - definir a variável x antes da definição da função

x = 1 --> Variavel x definida fora da função
def escopo():
    print(x)  --> usando a variavel x que foi definida fora da função

escopo() --> executando a função

# FORMA 2 - definir a variavel x antes da execução da função

def escopo():
    print(x) --> usando a variavel x que foi definida fora da função

x = 1 --> Variavel x definida fora da função
escopo() --> executando a função
----------------------------------------------------------------------

Em 99% das vezes vamos utilizar a forma 1, porém, a forma que utilizamos não importa, apenas lembre-se: Se definirmos 
uma varivavel fora da função e formos utilizar essa variavel dentro da função, essa variavel DEVE ser definida ANTES
DA EXECUÇÃO DA FUNÇÃO. Caso contrário, dará erro

Uma observação importante é que quando essa variavel x = 1 é definida fora da função, ela assume o nome de 
ESCOPO GLOBAL (são variáveis criadas fora de qualquer função)
'''


'''
ESCOPO EM FUNÇÕES DENTRO DE FUNÇÕES

Agora, suponhamos que tivéssemos o seguinte código:

x = 1 --> variavel sendo definida fora da função

def escopo1(): --> definindo função escopo 1
    def escopo2(): --> definindo função escopo 2
        y = 2 --> variavel sendo definida dentro da função escopo 2
        print(x,y)
    escopo2()
    print(x)

escopo1() --> executando a função

Perceba na imagem acima que dentro da função escopo1 eu tenho a função escopo2. Algo que é importante dizer é que se 
quiséssemos utilizar a variável y = 2 na função escopo1, não poderíamos, pois essa variável está definida dentro do 
escopo da função escopo2. Por outro lado, tanto a função escopo1 quanto a função escopo2 conseguem utilizar a 
varívavel x = 1 que foi definida do lado de fora da função (escopo global). Isso quer dizer que as funções conseguem utilizar aquilo 
que é definido fora da função, em escopos mais externos. Um exemplo disso é que se a váriavel x = 1 fosse definida 
dentro da função escopo1, a função escopo2 continuaria conseguindo utilizar essa varíavel, pois é uma variavel que 
foi definida em um escopo mais externo . Por outro lado, a função escopo1 continua não podendo acessar a variavel 
y = 2, pois ela está definida dentro da função escopo2, que é um escopo mais interno.

Algo interessante de se dizer também é que, suponhamos que no escopo global, nós definimos a variável x como x =1. 
No escopo da função escopo1, nós definimos a mesma variável x como x = 10 e no escopo da função escopo2, nós 
definimos a mesmíssima variável x como x = 20, assim como no códico abaixo:

Agora, suponhamos que tivéssemos o seguinte código:

x = 1 --> variavel sendo definida fora da função

def escopo1(): --> definindo função escopo 1
    x = 10
    def escopo2(): --> definindo função escopo 2
        x = 20
        y = 2 --> variavel sendo definida dentro da função escopo 2
        print(x,y)
    escopo2()
    print(x)

print(x)
escopo1() --> executando a função
print(x)

Quando o código acima é executado, o primeiro print irá exibir o “x” que está no escopo GLOBAL (x = 1). Isso acontece 
porque, como eu falei anteriormente, não conseguimos acessar as variáveis que são definidas em escopos mais internos 
e como o escopo GLOBAL é o escopo mais externo de todos, ele só conseguirá acessar as variáveis que foram definidas 
no próprio escopo global, que será x= 1. Agora, depois disso, nós executamos a função escopo1, que primeiro irá 
definir a variável x como x =10 e depois irá definir a função escopo2, onde definimos a variável x como sendo x=20 e 
a variável y como sendo y= 2. Neste caso, a função escopo2, tem acesso à variavel x que foi definida no escopo1 
(x=10), pois é um escopo mais externo a ela. Apesar disso, a função escopo2, dará prioridade à variável que foi definida 
dentro do seu próprio escopo. Após isso, a função escopo2 será executada (ela exibe 20 e 2) e por fim, a função 
escopo1 exibe a variável x, que será 10, pois ela não consegue acessar a variavel x definida no escopo2 (x = 20) por 
ser mais interna e até consegue acessar a variável x definida no escopo GLOBAL (x = 1), mas dará prioridade à 
variável x definida em seu próprio escopo (x = 10), exibindo assim x=10. No final ainda, o print irá exibir o “x” 
que está no escopo GLOBAL (x = 1), pois não tem acesso as variáveis que são definidas em escopos mais internos.

'''


'''
USO DO GLOBAL

Agora que entendemos melhor sobre escopos, uma coisa que eu poderia fazer também (que não é uma boa prática) é 
manipular a variável que está no escopo mais externo a partir da variavel que está no escopo mais interno. 
Para isso, utilizamos a palavra “global”. Dessa forma, podemos dizer que a palavra-chave global serve para dizer ao 
Python que uma variável usada dentro de uma função não é local, e sim aquela variável global que já foi definida 
fora da função. Ou seja, permite modificar variáveis globais de dentro de funções.

Veja um exemplo no código abaixo 



O que aconteceu é que, ao executar o código, o primeiro print exibiu o “x” que está no escopo GLOBAL (x = 1). Após 
isso, a função escopo1 é executada e, dentro da função escopo1, a primeira coisa que é feita é a utilização do global x, 
onde há a manipulação da variável x que é definida no escopo mais externo (x = 1) para a variável que foi definida 
naquele escopo logo em seguida (x = 10). Depois disso, dentro da função escopo1, é definida a função escopo2, onde 
definimos a variável x como sendo x=20 e a variável y como sendo y= 2. Após isso, a função escopo2 será executada 
(ela exibe 20 e 2) e por fim, a função escopo1 exibe a variável x, que será 10, pois ela não consegue acessar a 
variavel x definida no escopo2 (x = 20) por ser mais interna, exibindo assim x=10. Por fim, no último print, como
manipulamos a variável x que é definida no escopo mais externo com o “global x”, será exibido o x que foi definido 
naquele escopo, ou seja, x = 10.


'''