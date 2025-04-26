'''
O exercicio a seguir consiste na prática dos conteúdos de: Loops, variaveis, condições (break e continue), flags coerção, operadores 
comparativos e de identidade, formatação de string. (Também aplicamos try-except, mas como esse exercicio foi feito 
na época de estudo de módulo básico, nós nem sabiamos o porque estavamos aplicando, pois isso só foi estudado afundo
no modulo intermediário)

A instrução é programa simples recebe uma série de números inteiros e identifica o menor e o maior entre eles
'''

try:
    numero_minimo = None
    numero_maximo = None

    while True:
        numero = int(input('Informe um número inteiro (digite -1 para parar): '))
        if numero == -1:
            break
        else:
            if numero_minimo is None or numero < numero_minimo:
                numero_minimo = numero
            if numero_maximo is None or numero > numero_maximo:
                numero_maximo = numero
    
    if numero_minimo is not None and numero_maximo is not None:
        if numero_maximo == numero_minimo:
            print('Os números inseridos são iguais')
        else:
            print(f"O menor número inserido foi: {numero_minimo}")
            print(f"O maior número inserido foi: {numero_maximo}")
    else:
        print('Nenhum número foi inserido')
except:
    print('Erro na entrada de dados. Digite números inteiros')