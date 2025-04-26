'''
ANINHAMENTO DE LOOPS 

Outra coisa muito importante a pontuar quando falamos sobre loops é o aninhamento deles.
Aninhar loops (ou "loops dentro de loops") é quando colocamos um loop dentro do corpo de outro loop.


Aninhamento de loops é útil sempre que você precisa:

- Trabalhar com problemas de lógica mais complexos

- Trabalhar com listas dentro de listas (listas aninhadas)

- Criar combinações ou permutação de valores (gerar pares de elementos)

É importante compreender aninhamento de loops porque para diversas situações do mndo real que vamos representar no
código, temos que utiliza-lo, como um sistema de notas pode ter alunos, matérias e notas e um mapa é feito de linhas 
e colunas, por exemplo. Além disso nos ajuda a desenvolver o pensamento lógico e Abre as portas para entender algoritmos
mais avançados depois.

Veja alguns exemplos:
'''

# EXEMPLO 1 (loop for): pegando os numeros de uma matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')


#EXEMPLO 2 (loop while): fazendo matriz com while

linha = 0

while linha < 3:
    coluna = 0
    while coluna < 3:
        print(f'({linha},{coluna})', end=' ')
        coluna += 1
    print()  # Pula linha depois de cada linha
    linha += 1

'''
Uma observação é que o aninhamento aumenta a complexidade. Ou seja, loops aninhados podem deixar o programa mais lento 
em grandes volumes de dados. Veremos isso mais afrente quando formos estudar sobre DSA
'''