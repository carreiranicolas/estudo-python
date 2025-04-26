'''
Suponhamos que temos uma lista de nomes: nomes = [Maria, José, João], podemos desempacotar essa lista criando variáveis e 
ir extraindo o valor. Para isso, basta fazer: nome1, nome2, nome3 = [Maria, José, João] (também poderia ser feito:
nome1, nome2, nome3 = nomes) . Assim teremos variáveis com os valores da lista (nomes) extraídos. O nome1, neste exemplo, 
será Maria, o nome2 seria José, o nome3 seria João.

Caso tenhamos mais variáveis que valores ou mais valores que variáveis, receberemos um erro. Isso acontece porque não 
teríamos valores suficientes para o número de variáveis (mais variáveis que valores) OU não teríamos variáveis suficientes
para o número de valores (mais valores que variáveis).

Se tivermos uma lista com 3 valores, por exemplo, e quisermos pegar só um valor desses 3, temos que fazer o seguinte: 
nome1, *resto = [Maria, José, João]. Assim estaremos pegando apenas o nome1 (Maria) e jogando os nomes restantes em 
*resto. Essa váriavel *resto é uma OUTRA lista com os valores que restaram 
(nesse caso, José e João).

Veja na prática:
'''

nomes = ['Maria', 'José', 'João']

nome1, *resto = ['Maria', 'José', 'João']

print(nome1) #Retornará: 'Maria'
print(resto) #Retornará: ['José', 'João']
print(*resto) #Retornará: José João

'''
Dessa forma *resto fará a coleta de múltiplos valores em um desempacotamento.

Além disso, uma observação é que, como podemos ver no exemplo prático, ao utilizar o print(*resto) e o print(resto),
obtivemos coisas um pouquinho diferentes. 

Isso acontece porque o *resto, quando usado como argumento no print (e em qualquer função), ele abre "abre" a lista, 
e passa os elementos individualmente para a função, como se fossem argumentos separados.

Enquanto isso, ao usar print(resto), ele exibirá a lista inteira

Uma curiosidade é que quando não formos usar os nomes que restaram, ao invés de criar a variável *resto, ficou 
convencionado com os desenvolvedores python de criar uma variável chamada *_.
'''

'''
Outro detalhe muito importante sobre desempacotamento é o seguinte: Suponhamos que nós tenhamos a seguinte lista:

lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']

Se quisséssemos extrair dessa lista, por exemplo, apenas o primeiro e último elemento e deixar o resto de lado
Como fáriamos? 

Veja abaixo:
'''
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']

primeiro, *_, ultimo = lista

print(primeiro, ultimo) #Retorna: Maria Edurada

'''
Mas e se quiséssemos pegar também o penúltimo elemento (o número 3)? Para pegar o penúltimo elemento, bastaria 
adicionar uma variável antes da variável “ultimo” no desempacotamento. 

Veja:
'''

primeiro, *_, tres, ultimo = lista

print(primeiro, tres, ultimo) #Retorna: Maria 3 Edurada

'''
Agora, uma pergunta mais dificil, e se nos quiséssemos pegar apenas o número 2 e o nome Eduarda? Como faríamos? 

Veja abaixo:
'''

*_, numero2, _, ultimo = lista

print(numero2, ultimo) #Retorna: 2 Edurada

'''
Acima, o que acontece é vamos pegar apenas o numero 2 e o nome Eduarda, mas aí você deve estar se perguntando:
Como ele sabe exatamente onde começa o numero 2 na lista pra ele pegar? Por que nessa variavel numero2 ele não peria ter
pego o numero 1, por exemplo? 

O que acontece é que ele vai se basear no último elemento que estamos desempacotando. A variavel ultimo está desempacotando 
o último elemento da lista, então quando ele idendifica que a variavel ultimo é o último elemento da lista e que antes de 
ultimo temos a variavel _ (que guardará o 3), ele se localiza e sabe que a variavel numero2 terá que armazenar o valor 2

Além disso, quando escrevemos: *_, numero2, _, ultimo = lista
o _ começará guardando ['Maria', 'Helena', 1], mas depois, quando aparece o segundo _, ele é reatribuído ao valor 3. (como
não vamos usar esses valores guardados na variavel _ não tem importancia se perdemos eles em uma reatribuição, por exemplo)
'''