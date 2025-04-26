'''
O exercicio a seguir consiste na prática dos conteúdos de: Loops, variaveis, condições (e continue e break), função 
len, flag coerção, operadores aritiméticos comparativos e de identidade, formatação de string e aninhamento de loops. 
(Também aplicamos try-except, mas como esse exercicio foi feito na época de estudo de módulo básico, nós nem 
sabiamos o porque estavamos aplicando, pois isso só foi estudado afundo no modulo intermediário)

Este é um programa que conta quantas vogais totais tem contando a partir de todas as palavra que o usuário digitou,
até que ele digite 1 para parar
'''

vogais = 0

while True:

    palavra = input('Digite uma palavra (digite 1 para sair): ').lower()
    i = 0
    vogal = 'aeiou'
    if palavra == '1':
        break

    else:

        while i < len(palavra):
            letra = palavra[i]

            if letra == ' ':
                i += 1
                continue
            else:
                if letra in vogal:
                    vogais +=1
                i += 1
print(f'A quantidade de vogais é: {vogais}')