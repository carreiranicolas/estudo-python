'''
OPERADORES DO SET

Ao longo do nosso estudo sobre set, podemos ver que eles são bastante semelhantes a conjuntos matemáticos 
e eles possuem operadores que reforçam isso mais ainda:
'''

s1 = {1,2,3}
s2 = {2,3,5}

# | → operador union que faz a união:

s3 = s1 | s2

print(s3) #Retorna {1, 2, 3, 5}

# & → operador de intersecção, que retorna apenas os valores que tem nos dois sets

s3 = s1 & s2

print(s3) #Retorna: {2, 3}

# – → diferença, que irá mostrar apenas os itens presentes no set da esquerda (portanto perceba que a ordem importa)

s3 = s1 - s2 

print(s3) #Retorna {1}

s4 = s2 - s1

print(s4) #Retorna: {5}

# ^ → diferença simétrica, que retorna os itens que estão presentes em apenas um dos sets

s1 = {1,2,3}
s2 = {2,3,5}

s3 = s1 ^ s2

print(s3) #Retorna: {1, 5}


