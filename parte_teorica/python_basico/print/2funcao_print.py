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

Se usarmos print(argumento1, argumento2, sep=’-’), por exemplo, no lugar dos espaços vazios que ficam entre um argumento e outro, 
ele vai colocar o que colocamos em sep=.

'''
print(123, 'Olá, mundo!', sep='-') #Irá exibir: 123-Olá, mundo!

