'''
O exercicio a seguir consiste na prática dos conteúdos de: Loops, variaveis, condições, coerção operadores 
aritiméticos e comparativos e formatação de string. (Também aplicamos try-except, mas como esse exercicio foi feito 
na época de estudo de módulo básico, nós nem sabiamos o porque estavamos aplicando, pois isso só foi estudado afundo
no modulo intermediário)

A instrução é fazer uma espécie de "verificador" que vê se um número é par ou impar
'''


while True:

    try:
        numero = int(input("Informe um número que você quer verificar: "))
        if numero % 2 == 0:
            print(f"O número {numero} é PAR!")
        else:
            print(f"O número {numero} é IMPAR!")
        break
    
    except:
        print("Erro na entrada de dados. Por favor, informe um número inteiro.")