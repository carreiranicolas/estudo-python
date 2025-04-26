'''
O exercicio a seguir consiste na prática dos conteúdos de: Loops, variaveis, condições (e break), coerção operadores 
comparativos, formatação de string e flags. (Também aplicamos try-except, mas como esse exercicio foi feito 
na época de estudo de módulo básico, nós nem sabiamos o porque estavamos aplicando, pois isso só foi estudado afundo
no modulo intermediário)

A instrução é fazer uma espécie de programa que calcula o IMC a partir dos dados de peso e altura coletados do 
usuário e classifica, com base no IMC, o nível de obesidade ou magreza.
'''

while True:
   
   #ENTRADA DE DADOS

   peso = input("Digite seu peso em KG (ex: 67.2): ")
   altura = input("Digite sua altura em metros (ex: 1.70): ")

   #VALIDADOR

   try:
      peso_float = float(peso)
      altura_float = float(altura)
      flag = True
   except:
      flag = None
   
   if flag == None:
      print("Por favor, informe valores válidos.")
      continue

   if peso_float and altura_float != 0:
      
      #ALGORITMO
       imc = peso_float / altura_float**2
       
       o_3 = f'Seu imc é {imc:.2f} e seu nível é: Obesidade grau 3'
       o_2 = f'Seu imc é {imc:.2f} e seu nível é: Obesidade grau 2'
       o_1 = f'O seu imc é {imc:.2f} e seu nível é: Obesidade grau 1'
       sp = f'O seu imc é {imc:.2f} e seu nível é: Sobrepeso'
       n = f'Seu imc é {imc:.2f} e seu nível é: Normal'
       abn = f'O seu imc é {imc:.2f} e seu nível é: Abaixo do normal'

       if(imc > 40.0):
         {
            print(o_3)
         }
       elif(40.0 > imc >= 35.0):
         {
            print(o_2)
         }
       elif(35.0 > imc >= 30.0):
         {
            print(o_1)
         }
       elif(30.0 > imc >= 25.0):
         {
            print(sp)
         }
       elif(25 > imc >= 18.6):
         {
            print(n)
         }
       elif(imc <= 18.5):
         {
            print(abn)
         }
       else:
          print("Ok, isso não deveria chegar até aqui")
   else:
      print("Por favor, informe valores diferentes de zero.")
      continue
  
   #PARTE PARA SAIR DO PROGRAMA
   
   sair = input("Digite 's' para sair do programa: ").lower().startswith('s')

   if sair == True:
      print("Você saiu do programa.")
      break