'''
Em Python, coersão de tipo se trata de transformar um tipo de dado em outro tipo de dados. Isso é bem simples

Em python, a coerção de tipos pode acontecer de duas formas:

-->IMPLICITA: Feita pelo próprio Python quando ele percebe que faz sentido. 

-->EXPLICITA (manual): Nós forçamos a coerção usando tipodedado(argumento que queremos converter)


Veja abaixo alguns exemplos para entendermos melhor sobre:
'''

# COERÇÃO IMPLICITA

num_inteiro = 5
num_float = 2.5

resultado = num_inteiro + num_float
print(resultado)  # 7.5
print(type(resultado))  # <class 'float'>

'''
Perceba acima que na hora de fazer a operação, o python viu que num_float é float, então ele converte
num_inteiro (int) para float também, para não perder precisão. Isso acontece sem perdirmos ou forçamos, por isso implicita

Essa coerção implicita acontece de forma mais comum em operações entre int e float. Em outros casos é super raro e 
especifico
'''


# COERÇÃO EXPLICITA 

# 1

int('1') # Aqui nós estamos fazendo a conversão de str para int

# Vamos visualizar:

print(type('1')) # Aqui podemos ver que o tipo de dado de '1' é str (string)

print(type(int('1'))) # Aqui podemos ver que, ao converter o tipo de dado, teremos que '1' é int (inteiro)

# 2

float(2) #Aqui nós estamos fazendo a conversão de int para float

# Vamos visualizar:

print(type(2)) # Aqui podemos ver que o tipo de dado de 2 é int (inteiro)

print(type(float(2))) # Aqui podemos ver que, ao converter o tipo de dado, teremos que 2.0, que é float

# 3

bool('') #Aqui nós estamos fazendo a conversão de str para bool

# Vamos visualizar:

print(type('')) # Aqui podemos ver que o tipo de dado de '' é str (string)

print(type(bool(''))) # # Aqui podemos ver que, ao converter o tipo de dado, teremos False, que é bool


#OBS: Obtivemos False porque é uma string vazia, para ver mais sobre isso, vá ao arquivo de bool. 

'''
Um detalhe interessante sobre coerção de tipos é que a corerção do int tem algumas particularidades.
Veja abaixo

int(12.99)       # → 12 (trunca, não arredonda)
int(True)        # → 1 (ao converter o bool True para int retorna 1. O contrario também acontece)
int(False)       # → 0 (ao converter o bool False para int retorna 0. O contrario também acontece)

'''