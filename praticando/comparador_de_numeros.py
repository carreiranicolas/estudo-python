'''
O exercicio a seguir consiste na prática dos conteúdos de: Loops, variaveis, condições, coerção operadores 
comparativos e formatação de string. (Também aplicamos try-except, mas como esse exercicio foi feito 
na época de estudo de módulo básico, nós nem sabiamos o porque estavamos aplicando, pois isso só foi estudado afundo
no modulo intermediário)

A instrução é fazer uma espécie de "comparador" que compara os numeros recebidos
'''

while True:
    try:
        numero_1 = float(input("Digite um número: "))
        numero_2 = float(input("Digite outro número: "))

        if numero_1 > numero_2:
            print(f'{numero_1} é maior que {numero_2}')
        elif numero_1 < numero_2:
            print(f'{numero_1} é menor que {numero_2}')
        else:
            print("Os números são iguais.")
        break
    
    except:
         print("Por favor, digite apenas números")