'''
Em Python, coersão de tipo se trata de transformar um tipo de dado em outro tipo de dados. Isso é bem simples

Para fazer isso em python basta usar: tipodedado(argumento que queremos converter)

'''
#EXEMPLO 1

int('1') # Aqui nós estamos fazendo a conversão de str para int

# Vamos visualizar:

print(type('1')) # Aqui podemos ver que o tipo de dado de '1' é str (string)

print(type(int('1'))) # Aqui podemos ver que, ao converter o tipo de dado, teremos que '1' é int (inteiro)

# EXEMPLO 2

float(2) #Aqui nós estamos fazendo a conversão de int para float

# Vamos visualizar:

print(type(2)) # Aqui podemos ver que o tipo de dado de 2 é int (inteiro)

print(type(float(2))) # Aqui podemos ver que, ao converter o tipo de dado, teremos que 2 é float (decimal)