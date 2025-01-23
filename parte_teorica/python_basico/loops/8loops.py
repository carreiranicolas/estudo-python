'''
Da mesma forma que as condicionais, outro aspecto que temos em uma estrutura de linguagem de programação são os LOOPS/estruturas de repetição

Os loops ou estruturas de repetição são extremamente importantes em praticamente todas as linguagens de programação e dão inicio a uma parte mais robusta
dentro da programação, pois é a partir deles que conseguimos fazer coisas que envolvem uma lógica maior e mais complexa. O que os loops fazem é, basicamente
repetir um pedaço de código, porém há diferentes tipos de loops que irão repetir o trecho de código em um número diferente de vezes. 

Nós temos, no Python:

Loop while (condição):

O loop while irá repetir o trecho de código enquanto a condição for verdadeira (True), o que é um pouco perigoso, pois muitas pessoas acabam não lembrando disso
e se esquecendo de fazer uma forma para tornar a condição ao lado do while falsa (False), criando um loop infinito. Sua estrutura é:

while (condição):
    TRECHO DE CÓDIGO A SER REPETIDO

'''

while True:
    print('oi')

    # Se pararmos por aqui e deixarmos nosso código assim, estaremos criando um loop infinito, pois a condição ao lado do while será SEMPRE True
    # então, para evitar de criar um loop infinito nesse caso, podemos colocar um 'break', como fizemos abaixo
    
    break # O break busca o loop mais mais próximo dele e quebra. Dessa forma, nosso loop deixará de ser infinito e será controlado.

# outra coisa que podemos fazer para que nosso loop não seja infinito é utilizar a atribuição, onde utilizaríamos uma váriavel e os operadores
# lógicos para criar uma condição que possa se tornar falsa em algum momento, quebrando o loop.

contador = 0 # Não colocamos a varíavel dentro do loop, pois seu valor iria reiniciar sempre que o loop rodasse e neste caso queremos ACUMULAR valores para parar o loop
while contador < 10:
    print('oi')
    
    contador += 1 # Dessa forma, cada vez que o loop rodar iremos adicionar +1 à variavel 'contador' de forma a acumular valores, até o momento que nossa váriavel 
                  # 'contador' estiver com um valor maior ou igual a 10, encerrando assim o loop.

'''
Além do loop while, outro loop que temos no pyhton é o Loop 'for in':

O loop 'for in' é um loop utilizado para coisas finitas, ou seja, ele é utilizado quando sabemos precisamente o número de repetições que temos que ter,
diferentemente do loop while que, apesar de poder ser utilizado para coisas finitas, costumamos utilizá-lo para coisa sinfinitas, onde não sabemos o
número de vezes que teremos que repetir o código. Veja a estrutura do loop for:

nome = 'Nicolas'

for letra in nome:
    print(letra)

A variável “letra” foi criada. Isso porque o “for” passa de carácter em caracter na string “nome”, então ficou definido que “letra” seria cada caracter 
de “nome” que o loop for itera.

Além disso, Perceba que não ocorreu um loop infinito, porque o for sabe que ele deve rodar seu loop até o fim da string “nome”, diferente do while 
que temos que definir um contador ou algo do tipo para ele parar.


Além disso, temos uma função chamada range que, apesar de não ser dependente do loop for e vice e versa, utilizamos bastante os dois juntos.
Ela funciona da seguinte forma: 

range(start, stop, step), onde o start é o número onde começa e o stop é o número onde para (sendo que em python ele sempre irá parar em um número antes 
do que definimos no stop. Exemplo: definimos o stop como 10, ele irá parar no 9) e também temos o step que é de quanto em quanto ele vai conatr/iterar
(semelhante a razão que temos em uma PA)

for n in range(0, 10, 2):
    print(n)

O que acontecerá nesse loop é que será exibido os números 0, 2, 4, 6, 8

É importante ressaltar que tudo que vimos em while (break e continue) funciona no loop for também
'''
