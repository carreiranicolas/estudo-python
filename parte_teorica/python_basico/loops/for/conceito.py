'''
Loop for in:

O loop 'for in' é um loop utilizado para coisas finitas, ou seja, ele é utilizado quando sabemos precisamente
o número de repetições que temos que ter. Veja a estrutura do loop for:

iteravel 

for iteracao in iteravel:
    print('oi')

Vamos ver na prática:
'''

nome = 'Nicolas'

for letra in nome:
    print(letra)

'''
No exemplo acima, nós temos a string 'Nicolas' (strings são iteraveis) e o loop for vai rodar até acabar 
a quantidade de letras da string. 

Uma observação é que uma variavel “letra” foi criada. Isso porque o “for” passa de carácter em caracter na 
string “nome”, então ficou definido que “letra” seria cada caracter de “nome” que o loop for itera.

Certo, mas então temos que criar um iteravel (uma string, lista, tupla.. e etc) toda vez que formos utilizar o
loop for? Na verdade não, existe uma função chamada range que é bem utilizada com o loop for, onde falando de 
forma bem geral, nós podemos utiliza-la para gerar uma sequência de números inteiros, onde o loop for vai 
iterar essa sequencia de numeros criada até o final, encerrando o loop. Se quiser saber mais detalhes sobre 
o loop range veja o arquivo function_range

É importante pontuar que no loop for, assim como no loop while, nós também temos os mecanismos de break e
continue. Falando de forma geral, o break faz a interrupção do loop mais próximo dele e o continue pula para a
próxima repetição do loop, ignorando o que vem depois dele no loop atual. Se quiser ver em mais detalhes, vá
até o arquivo de break_e_continue
'''