'''
EXCEÇÕES

Em python (e em qualquer linguagem), quando executamos o nosso código, poderá ocorrer erros. Esses
erros são chamados de EXCEÇÕES. Dessa forma: 

Python viu algo de errado --> para tudo --> lança a exceção (erro)

Algumas das principais ações que geram uma exceção são:

--> Divisão por zero

--> Acesso a índice inexistente de uma lista

--> Chamada de função com tipos errados

--> Conversão inválida de tipos (como int("abc"))

--> Tentativa de abrir um arquivo que não existe

Veja abaixo:
'''

n1 = 10

n2 = 0

n1/n2 # Aqui estamos fazendo uma divisão por 0, isso gerará uma exceção (parara o programa e gerará o erro)


print('Aqui não exibe')  # Isso não será exibido, pois o programa parou acima


'''
Quando vemos a exceção no terminal, nós vemos, por exemplo:

ZeroDivisionError: division by zero

--> O "ZeroDivisionError" indica o TIPO DA EXCEÇÃO

--> O "division by zero" indica a DESCRIÇÃO DA EXCEÇÃO


Uma curiosidade é que toda exceção é uma insantancia de uma classe que herda de uma classe base chamada Exception.
O ZeroDivisionError, por exemplo, é uma instancia da classe ArithmeticError que herda da classe-base (Exception).
Ainda entenderemos melhor sobre isso, veremos mais afrente. Não se preocupe. Caso queira ver a hierarquia das
exceções, veja abaixo:

https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

'''