'''
List Comprehension, falando a grosso modo, é uma forma de criar lists usando uma linha de código em Python, o que pode ser muito 
útil para simplificar e diminuir código. Para utiliza-lo, faríamos:

list_comprehension = [expressão for item in iterável]

Suponhamos que nós tenhamos a lista [0,1,2,3,4,5,6,7,8,9]. A forma tradicional que nós temos para criar essa lista é:

lista = []
for n in range(10):
    lista.append(n)
print(lista)

Perceba portanto que é muito trabalhoso fazer da forma tradicional, então poderíamos utilizar o list comprehensiona. Veja:

list_comprehension = [numero for numero in range(10)] --> Irá nos retornar: [0,1,2,3,4,5,6,7,8,9]

Dessa forma, perceba que utilizando o list comprehension nós simplificamos bastante o processo. Nós fazemos um loop for para gerar uma iteração e 
à esquerda do loop for, nós temos o valor que será incluído na lista para cada iteração. 

Algo interessante do list_comprehension é que conseguimos alterar/modificar o elemento que será adicionado à lista para cada iteração de forma muito simples, tornando
as coisas dinamicas e sendo muito útil para fazer algumas lógicas de operar sobre o valor da iteração. Veja abaixo:

Se quiséssemos multiplicar o valor da iteração por algum número, por exemplo, para depois incluí-lo na lista, veja como faríamos:

list_comprehension = [numero * 2 for numero in range(10)] --> Irá nos retornar: [0,2,4,6,8,10,12,14,16,18]

Portanto, perceba acima que estamos aplicando uma lógica nas iterações do loop for, tornando a adição dos valores da lista dinamica
'''