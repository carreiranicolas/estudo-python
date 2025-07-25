'''
FILTRO DE DADOS EM LIST COMPREHENSION

Aqui, vamos falar sobre filtro, onde podemos FILTRAR o que vai entrar na lista ou não. Para isso, 
vamos adicionar um if APÓS o for e sem o else. Veja:
'''

lista = [n for n in range(10) if n > 5]

print(lista) # Retorna: [6, 7, 8, 9]

'''
Agora, faremos um exemplo mais complexo que envolverá, inclusive, dicionarios, mas será importante
para que possamos entender de maneira plena o uso do filtro e sua utilidade em list comprehension. Dessa 
forma, caso precise ver sobre dicionarios antes, basta acessar a pasta de dicionarios. 
Vamos ao exemplo:
'''
produtos = [
    {'nome': 'n1', 'preco': 20},
    {'nome': 'n2', 'preco': 30},
    {'nome': 'n3', 'preco': 40}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 2} if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] < 40 # O pulo do gato
]

'''
O que aconteceu acima é que na nossa lista novos_produtos, após o loop for, foi filtrado que só 
entraria na lista novos_produtos o produto da lista produtos no qual o preço fosse menor que 40 
(aí entrariam os produtos p1 e p2, onde os preços são 20 e 30, respectivamente). Após entrar na lista, 
caso o valor que entrou na lista for maior que 20, ele será multiplicado por dois, como podemos ver 
ali antes do loop for
'''