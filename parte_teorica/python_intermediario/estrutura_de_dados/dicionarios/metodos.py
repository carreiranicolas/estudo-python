'''
METODOS - DICIONARIOS

Vamos ver agora sobre alguns métodos úteis para se usar com dicionários:
'''

pessoa = {
    'nome': 'Nicolas',
    'sobrenome': 'Carreira',
    'idade': 20
}


#Método .__len__(): Retorna o número de chaves do dicionário

print(pessoa.__len__()) #Retorna 3

#OBS: Poderíamos ao invés de usar o método __len__, usar a função len() passando o dicionario para dentro dela

# Método .keys():  retorna as chaves que temos em nosso dicionário em um tipo dict_keys, que pode ser convertido em 
# tuplas ou lista depois, por exemplo.

print(pessoa.keys()) #Retorna: dict_keys(['nome', 'sobrenome', 'idade'])

print(tuple(pessoa.keys())) #Retorna: ('nome', 'sobrenome', 'idade')

for chaves in pessoa.keys():
    print(chaves) #Retorna: nome
                              #sobrenome
                              #idade

#Método .values(): Lembra o método .keys(). Nos retorna só os valores que temos

 
print(pessoa.values()) #Retorna: dict_values(['Nicolas', 'Carreira', 20])

print(tuple(pessoa.values())) #Retorna: ('Nicolas', 'Carreira', 20)

for valor in pessoa.values():
    print(valor) #Retorna: Nicolas
                              #Carreira
                              #20

#Método .items(): Lembra ambos os métodos anteriores (keys e values), mas retorna a chave e o valor

print(pessoa.items()) #Retorna: dict_items([('nome', 'Nicolas'), ('sobrenome', 'Carreira'), ('idade', 20)])

print(tuple(pessoa.items())) #Retorna: (('nome', 'Nicolas'), ('sobrenome', 'Carreira'), ('idade', 20))

for chave, valor in pessoa.items():
    print(chave)
    print(valor) #Retorna: nome
                           #Nicolas
                           #sobrenome
                           #Carreira
                           #idade
                            #20

#Método .setdefault(): Suponhamos que queiramos uma chave que não existe em nosso dicionário (‘altura’, por exemplo), 
# se tentamos pegar essa chave inexistente, irá nos retornar um erro como sabemos, mas podemos configurar o 
# dicionário para retornar um valor por padrão quando essa chave não existir e for requisitada e é apartir do 
# setdefault() que fazemos isso.

pessoa.setdefault('altura', 'Valor padrão' )

print(pessoa['altura']) #Retorna: Valor padrão



# Método .get(): Esse método nos retorna ou o valor da chave passada, ou retorna None (caso a chave não exista)

print(pessoa.get('nome')) # Retorna: Nicolas

print(pessoa.get('altura')) #Retorna: None

#Método .pop(): apaga a chave especificada do nosso dicionário e ainda nos retorna o valor que estava naquela chave.

nome = pessoa.pop('nome')

print(nome) # Retorna: Nicolas
print(pessoa) #Retorna: {'sobrenome': 'Carreira', 'idade': 20}

#Método .popitem():  elimina a última chave do dicionário e ainda retorna o que foi removido (tanto a chave quanto o valor)

ultima_chave = pessoa.popitem()

print(ultima_chave) #Retorna: ('idade', 20)
print(pessoa) #Retorna: {'sobrenome': 'Carreira'}


#Método .update(): podemos fazer várias coisas, como atualizar os valores de chaves existentes, adicionar novas 
# chaves e dentre outras coisas. O melhor é que o update permite que façamos tudo isso ao mesmo tempo.



#OBS: Podemos fazer o update utilizando argumentos nomeados também, veja:

#OBS2: Podemos também fazer o update utilizando tuplas e listas. Veja:


# MÉTODOS DE CÓPIA (.copy() e deepcopy())


#Método .clear(): Limpa tudo dentro do dicionário

pessoa.clear()
