"""
Em Python (e em outras linguagens em geral), uma das funções mais básicas que aprendemos é o print().

Dentro do print, passamos aquilo que queremos exibir (mostrar) na nossa tela. Muito simples

"""

print(123) # Irá exibir na nossa tela o número 123

print('Olá, mundo!') #Irá exibir na nossa tela a frase: Olá, mundo!

#Vale dizer que podemos passar mais de um argumento na função print, basta separá-los por vírgula

print(123, 'Olá, mundo!') #Neste caso, irá exibir: 123 Olá, mundo!

'''
Além disso, existem alguns detalhes interessantes sobre a função print

Se usarmos print(argumento1, argumento2, sep='-'), por exemplo, no lugar dos espaços vazios que ficam entre um argumento e outro, 
ele vai colocar o que colocamos em sep=.

'''
print(123, 'Olá, mundo!', sep='-') #Irá exibir: 123-Olá, mundo!

'''
Outro detalhe é que no print nós podemos passar um end= (assim como passamos o sep), onde aquilo que colocarmos no end= 
será colocado no final da linha impressa.Por padrão, o print() coloca uma quebra de linha ao final. Quando você usa end=, 
você substitui essa quebra de linha por outro caractere ou string qualquer. 

'''

print('Nicolas', end='#')
print('José')

#Acima, será impresso na tela: Nicolas#José

'''
No print, por padrão temos uma quebra de linha de um print para o outro, mas também podemos forçar uma quebra de linha
utilizando o \r\n
'''

print('Nicolas\r\n')
print('José')

# Acima, o que teremos exibido é: Nicolas (pula uma linha por causa da quebra de linha padrão do print + \r\n) José

'''
Um último detalhe é que podemos combinar o end= e o \r\n. Então ao combinar os dois, podemos fazer com que haja a adição
do caracter que queremos no final da linha impressa e a adição de linha
'''
print('Nicolas', end='#\r\n')
print('José')

#No caso acima, por conta do end= que inibe a quebra de linha padrão do print, teremos: Nicolas# (quebra de linha pelo \r\n) José
