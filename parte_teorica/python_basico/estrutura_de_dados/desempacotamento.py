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
e passa os elementos individualmente para a função print, como se fossem argumentos separados.

Enquanto isso, ao usar print(resto), ele exibirá a lista inteira


Uma curiosidade é que quando não formos usar os nomes que restaram, ao invés de criar a variável *resto, ficou 
convencionado com os desenvolvedores python de criar uma variável chamada *_.
'''