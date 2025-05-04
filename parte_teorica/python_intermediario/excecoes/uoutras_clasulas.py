'''
OUTRAS CLÁSULAS

Além do try-except, temos outras clásulas que são usadas no tratamento de erros (poderíamos inclusive combinar clásuslas). 
Dentre elas, temos:

--> finally

O finally, ele é SEMPRE executado. independentemente de ter ocorrido uma exceção ou não dentro do try;

Dessa forma, ao utilizar o try-finally, o try executa o que está dentro dele e independente de ocorrer um erro ou
não, o finally será executado. Veja abaixo
'''

# --> SE NÃO HOUVER EXCEÇÃO

# try:
#     print('ABRIR ARQUIVO') # Exibe isso
    
# finally:
#     print('FECHAR ARQUIVO') # Após terminar o try, exibe isso



# --> SE HOUVER EXCEÇÃO

# try:
#     print('ABRIR ARQUIVO') # Exibe isso
#     8/0 # Dará a exceção de divisão por 0
#     print('depois da divisão') # Isso não será exibido por conta da exceção
# finally:
#     print('FECHAR ARQUIVO') #Assim que der a exceção ele virá pra cá e exibirá isso

'''
Portanto, o finally será sempre executado, acontecendo uma exceção ou não. Então, poderíamos ter uma finally no 
nosso código para executar um bloco de código independente de ter erro ou não. Inclusive, poderíamos, ter um except 
também tratando a exceção caso ele ocorra no try. Veja abaixo:
'''

# try:
#     print('ABRIR ARQUIVO') # Exibe isso
#     8/0 # Dará a exceção de divisão por 0
#     print('depois da divisão') # Isso não será exibido por conta da exceção
# except ZeroDivisionErro:
#     print('Dividiu por 0')
# finally:
#     print('FECHAR ARQUIVO') #Assim que der a exceção ele virá pra cá e exibirá isso

'''
Perceba então que o try foi executado, ocorreu a exceção que foi logo tratada no except e o finally foi executado, mesmo acontecendo 
um erro. 

Isso é interessante porque imaginemos a situação onde o try abre um arquivo, mas esse arquivo dá erro. No 
finally, que é executado independente de acontecer um erro ou não, poderia ter um código para fechar o arquivo

Outra clásula que temos é o else, que não é tão utilizado, mas é importante saber

--> else

O else será executado caso o código ocorre sem erros.


Veja um exemplo abaixo:
'''

# --> COM EXCEÇÃO

# try:
#     print('ABRIR ARQUIVO') # Exibe isso
#     8/0 # Dará a exceção de divisão por 0
#     print('depois da divisão') # Isso não será exibido por conta da exceção
# except ZeroDivisionErro:
#     print('Dividiu por 0')
# else:
#     print('ocorreu tudo bem') #Não será executado, pois ocorreu a exceção de divisão por 0
# finally:
#     print('FECHAR ARQUIVO') #Após dar a execução no try e ter exibido a mensagem de erro do except, ele vem para ca


# --> SEM EXCEÇÃO

# try:
#     print('ABRIR ARQUIVO') # Exibe isso
# except ZeroDivisionError:
#     print('Divisão por 0) # Não será executado, pois não houve divisão por 0
# else:
#     print('tudo ocorreu bem') # Seria executado pois não houve execção
# finally:
#     print('FECHAR ARQUIVO') # Após terminar o try e executar o else, ele vem para cá

'''
Certo, vistas as clásulas e entendido o que cada uma faz, é importante pontuar que existe uma ordem para adicionar
as clásulas. A ordem correta, quando temos TODAS as clásulas é:

try:
    ...
except:
    ...
else:
    ...
finally:
    ...

Onde: 

try é obrigatório e sempre vem primeiro.

except pode aparecer uma ou várias vezes (com tipos de exceções diferentes).

else é opcional, mas se usado, deve vir depois de todos os except.

finally também é opcional, mas deve ser o último bloco, se presente.

Podemos ter portanto:

--> try + except

--> try + finally

--> try + except + finally

--> try + except + else

--> try + except + else + finally

Sendo que o else só pode existir se houver ao menos um except, então não poderiamos ter
try + else ou try + else + finally, por exemplo
'''
