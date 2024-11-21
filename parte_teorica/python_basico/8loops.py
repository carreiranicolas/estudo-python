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
Além do loop while, outro loop que temos no pyhton é o Loop 'for':





'''
