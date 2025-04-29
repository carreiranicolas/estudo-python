'''
FUNCOES

Função é um conceito muito importante dentro de programação. Funções são blocos de código reutilizáveis que executam uma tarefa 
específica. Elas permitem organizar o programa de forma mais clara, evitar repetição de código e facilitar a manutenção.

Apesar de ser estranho dizer isso, nós basicamente já aprendemos função em python, mesmo sem saber. O print(), por exemplo, é uma função.

Podemos criar nossas próprias funções. Para definir nossas funções em python, nós fazemos: def nome_função():. Após isso, dentro da função, 
escrevemos o código para algo qualquer. Quando estamos definindo a função, podemos passar valores para dentro do parenteses, que são os 
parametros da função. Exemplo:

def nome_função(a, b, c):
    ...
    
O “a”, “b”, “c”  que passamos para dentro do parênteses da função ao defini-la é o que chamaremos de parâmetro.


Uma observação é que, futuramente, quando formos utilizar essa nossa função “nome_função()” dentro do nosso código, nós não poderíamos chamar 
essa função sem passar nada ou sem preencher todos os valores “a”, “b”, “c”, caso contrário, teremos um erro na nossa tela dizendo que estão faltando três argumentos “a”, “b”, “c” 
(argumento são os valores que temos que passar para dentro da função quando vamos executar ela no nosso código, já os parâmetros, como dissemos, são as variáveis “a”, “b”, “c” 
que passamos para dentro do parênteses ao definir a função). Portanto, pra executar a função no nosso código, faríamos:

nome_função(a,b,c)

Os argumentos podem ser ainda nomeados ou posicionais (não nomeados), mas isso é explicado em detalhes no arquivo de argumentos nomeados e posicionais


Por padrão, funções python retornam um valor None (um não valor). Isso quer dizer, falando de forma grossa, que  quando uma função não tem um return explícito, ela 
automaticamente retorna o valor None. Podemos ver isso em detalhe no arquivo de..

Veja um exemplo de função simples abaixo:
'''

def saudacao(nome):
    print(f'Saudação, {nome}!')

saudacao('Nicolas') # Retornará: Saudação, Nicolas!


saudacao('José') # Retornará: Saudação, José!

'''
Perceba acima então que cada vez que executamos nossa função, podemos passar argumentos diferentes e é isso que torna as funções tão incríveis. O fato de podermos passar os 
argumentos diferentes, pode nos dar valores diferentes da função. Isso é uma grande mão na roda, pois não precisamos ficar reescrevendo aquele trecho de código repetidas vezes a cada vez 
que quisermos passar argumentos diferentes, para obter resultados diferentes, basta chamar a função e passar os argumentos. 

Uma curiosidade é que se dermos um print na nossa funcao saudação, ele nos dirá que aquilo que estamos printando é uma function, vai dizer o nome da função e nos dirá onde, na memória, ela está. 
Veja abaixo:
'''

print(saudacao)



'''
Isso acima é a DEFINIÇÃO da função. A EXECUÇÃO da função, como já vimos, utiliza paranteses. Veja abaixo:

definições da função: nome_função

execução da função: nome_função()


Além disso, um detalhe é que se fizermos print(saudacao('Nicolas')), por exemplo, veja o que acontece:
'''

print(saudacao('Nicolas')) # Nos retorna: Saudação, Nicolas!
                           #              None

'''
Isso acontece porque a função foi executada com os argumentos que passamos para ela (1 e 2) e ao ser executada, ela faz o print, assim como temos na definição dele. Por outro lado, o print que está do lado 
]de fora, ele exibe o valor que retorna DA FUNÇÃO e, como bem sabemos, funções retornam, por padrão, valores None. Portanto, para resumir o que acontece: A função soma é executada com os argumentos que passamos 
(por isso o 3 é exibido primeiro) e depois o print exibe o valor que retorna DA FUNÇÃO, que é None (por isso o None aparece por último).
'''