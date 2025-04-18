'''
FLAGS

Se quisermos saber se o interpretador entrou dentro do if, caso a condição for verdadeira ou não entrou, 
caso a condição for falsa, nós podemos fazer o uso das Flags. Veja:
'''
condicao = True
passou_no_if = False

if condicao:
    passou_no_if = True
else:
    print('Não passou')

print(f'Passou no if: {passou_no_if}')

'''
Perceba acima, que como a varivel que como a variavel condicao é True, irá passar no if. A partir disso, a 
a variavel passou_no_if que era False, deixará de ser False e virará True, significando que passou no if. Se
a condição fosse False e não pasasse no if, seria exibido 'Não passou' e a variavel passou_no_if continuaria 
False. Outra forma de fazer isso é utilizando 'None', que é um não valor. Veja:
'''

condition = True
passou = None

if condition:
    passou = True
else:
    print('não passou')

'''
Esse código acima é basicamente a mesma coisa do anterior, porém o None que irá desempenhar o papel da Flag.
Um detalhe interessente é que podemos utilizar os operadores de identidade 'is' e 'is not' para verificar se
a variavel passou no exemplo acima é None ou não, fazendo com que possamos manipular isso da forma que 
quisermos. Veja:
'''

if passou is not None: #Irá atender a condição, pois passou deixou de ser None e virou True (não é None)
    print('Executou pq passou') 
else:
    print('Não executou pq não passou')
