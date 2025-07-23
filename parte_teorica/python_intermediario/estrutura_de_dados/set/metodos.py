'''
METODOS - SET

vamos ver agora sobre alguns métodos úteis para se usar com conjuntos:
'''

conjunto = {1, 2, 3, 'Nicolas'}

#Método .add(): Usado para quando queremos adicionar valores ao set

conjunto.add('José')

print(conjunto) #Retorna: {1, 2, 3, 'Nicolas', 'José'} (não necessariamente nessa ordem)

#OBS: Uma observação é que se criarmos o set a partir do set() e depois irmos adicionando iteraveis, por exemplo 
# a esse set a partir do método .add(), o set não irá iterar os valores. Veja:

conjunto2 = set('Ola')

conjunto2.add('Nicolas')

print(conjunto2) #Retorna: {'a', 'Nicolas', 'l', 'O'} (não necessariamente nessa ordem)

# Método .update(): Nesse aqui, você adiciona valores ao set, porém, diferentemente do método .add(), os valores 
# serão iterados.

conjunto3 = set('OLA')

conjunto3.update('ni')

print(conjunto3) #Retorna: {'n', 'i', 'L', 'A', 'O'} (não necessariamente nessa ordem)

#OBS: É interessante isso porque Se quisermos passar vários valores para dentro do set de uma vez, poderíamos criar 
# uma tupla e utilizar o update. Veja:

conjunto3.update((1, 2, 'José'))

print(conjunto3) # Retorna: {'n', 1, 'A', 2, 'José', 'L', 'O', 'i'} (não necessariamente nessa ordem)


#Método .discard(): passamos um valor para dentro dele e ele elimina aquele valor do nosso set

conjunto3.discard('José')
print(conjunto3) #Retorna: {1, 2, 'O', 'L', 'n', 'i', 'A'} (não necessariamente nessa ordem)

# Método .clear(): Limpa o set

conjunto3.clear()

print(conjunto3) #Retorna: set()

