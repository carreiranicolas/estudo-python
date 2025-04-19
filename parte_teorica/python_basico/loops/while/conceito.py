'''
Loop while (condição):

O loop while irá repetir o trecho de código enquanto a condição for verdadeira (True),
o que é um pouco perigoso, pois muitas pessoas acabam não lembrando disso e se esquecendo de fazer 
uma forma para tornar a condição ao lado do while falsa (False), criando um loop infinito. Sua estrutura é:

while (condição):
    TRECHO DE CÓDIGO A SER REPETIDO

'''

i = 0
while i < 5:
    print('oi')
    i += 1

'''
No exemplo acima, criamos um loop while que irá executar o código print('oi') e adicionar 1 a varíavel i 
repetidas vezes. Essa execução de código ocorrerá até que a variavel i deixe de ser menor que 5 (ou seja, 
até que a variavel i seja igual a 5 ou maior que 5). Quando isso acontecer, a condição i < 5 será Falsa, 
fazendo com que o loop pare de acontecer. Esse uso de operadores de atribuição (+= nesse caso) e operadores 
lógicos (< nesse caso) para tornar a condição Falsa cria um mecanismo para evitar que o loop seja um loop 
infinito, por exemplo. 

Uma observação é que a variavel i = 0 fica fora do loop para que ela possa 
acumular os valores a cada vez que o loop rodar e assim tornar a condição do loop Falsa, quebrando ele. 
Se ela tivesse ficado dentro do loop, i seria reinicializado para i = 0 toda vez que o loop rodar, 
criando um loop infinito

Se o nosso código fosse:

while True:
    print('oi')
    
Acima, nós teríamos um loop infinito, pois a condição seria True para sempre, ela nunca deixaria de ser True.
(existe um mecanismo para que poderia fazer a interrupção desse loop infinito (e qualquer loop na verdade) 
chamado 'break', mas se quiser ver em detalhes, veja no arquivo break_e_continue na pasta loops). Tem também
um mecanismo chamado 'continue', que pode ser visto com mais detalhes no arquivo break_e_continue, mas que de
forma geral irá pular para a próxima repetição do loop, ignorando o que vem depois dele no loop atual

'''

