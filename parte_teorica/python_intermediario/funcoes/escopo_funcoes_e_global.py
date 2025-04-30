'''
ESCOPO DE FUNÇÕES E GLOBAL

Em python (e em qualquer linguagem), algo muito importante de se entender é sobre o escpo das funções. 
Escopo significa o local onde aquele código pode atingir.Ou seja, se eu tenho um escopo fechado dentro de uma função, quer 
dizer que o meu código não vai afetar o que estiver fora da função. O que fazemos dentro da função, fica na função.

Vamos entender com um exemplo prático:
'''

def escopo():
    x = 1
    print(x)


#print(x) -->Se tentarmos fazer isso, ele nos retorna um erro dizendo que a variavel x não está definida.

'''
Isso acima acontece porque orque a variável x até está definida, porém ela está definida dentro do ESCOPO DA FUNÇÃO.
Portanto, como diz o ditado: O que fazemos dentro da função, fica dentro da função


'''