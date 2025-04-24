'''
ANINHAMENTO DE LISTAS E TUPLAS

Como dissémos ao falar o conceito de tuplas e listras, nós podemos ter tudo dentro delas,
incluindo outras listas e tuplas. Portanto, aninhamento de listas/tuplas é quando nós temos 
dentro de listas ou tuplas, outras listas ou outras tuplas.

Veja um exemplo abaixo:
'''

salas = [
    ['José', 'Maria', 'Helena'],
    ['João', 'Dédé', 'Carlos'],
    ['Nicolas', 'Eduarda', 'Sofia']
]

'''
No exemplo acima, por exemplo. Se quiséssemos acessar 'Nicolas', nós faríamos:

sala[2][0] --> Isso quer dizer que na primeira lista estamos acessando a lista de indice 2
e dentro da lista de indice 2, estamos acessando o indice 0

Portanto, a lógica é bem simples. É só pensar que estamos entrando em uma lista de cada vez.

Veja agora utilizando loops for
'''
s = 0
for sala in salas:
    print(f'SALA: {s+1}')
    for aluno in sala:
        print(aluno)
    s +=1

'''
Acima, estamos acessando cada sala a partir do loop for e em seguida, pegamos cada lista de 
sala e acessamos os alunos de dentro dela a partir e outro loop for

'''