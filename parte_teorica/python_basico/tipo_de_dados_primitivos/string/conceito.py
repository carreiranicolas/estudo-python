'''
STRINGS


Strigs são


'''


'''
Uma coisa interessante é que existem duas funções que são usadas com casarcteres (caracter é literalmente uma string, como 'a' ou 'b', por exemplo)
as funções são: ord() e chr()

--> ord(): A função ord() em Python retorna o código Unicode (inteiro) correspondente ao caractere que foi passado.

--> chr(): Se quiser converter um número para o caractere correspondente, usa-se essa função

lembrando que letras minusculas e maiusculas tem codigo unicode diferentes!!

Veja exemplos
'''

# FUNÇÃO ORD

print(ord('A')) #Irá retornar 65, que é o código Unicode do caracter 'A' maiusculo

print(ord('b')) #Irá retornar 98, que é o código Unicode do caracter 'b' minusculo


# FUNÇÃO CHR

print(chr(80)) #Irá retornar 'P', que é a letra correspondente ao código unicode 80


print(chr(67)) #Irá retornar 'C', que é a letra correspondente ao código unicode 80
