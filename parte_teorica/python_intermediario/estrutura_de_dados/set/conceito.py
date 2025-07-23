'''
TIPO SET

O tipo set em python é basicamente um conjunto (sim os mesmos que aprendemos na matemática) e 
é um tipo de dado mutavel, mas eles são esquisitos, pois sets só aceitam tipos IMUTÁVEIS dentro deles.

------------------------------------------------------------------------------------------------------------
Para criar o set nós temos duas formas:


#Forma 1

conjunto = set()

Se criarmos um sets usando a forma acima (set()), nós temos que passar para dentro do set ITERAVEIS. Caso contrário, 
teríamos um erro. Isso acontece, porque ao criar um set dessa forma, ele irá iterar sobre os elementos do iteravel e 
inserir cada elemento individualmente no conjunto. Se passarmos uma lista então para set(), ele irá iterar os elementos
dessa lista e adicionar cada um individualmente no conjunto. Se passarmos uma string 'Nicolas' (string são iteraveis)
para set(), ele irá iterar cada caracter da string e adicionar cada um individualmente no conjunto. 

Uma observação é  que se passarmos para set() uma lista, onde dentro dessa lista nós tenhamos uma lista, dará erro. Isso
acontece porque o set() irá iterar a lista mais externa e irá adicionar os elementos dela dentro do conjunto um a um e então 
quando ele chegar na lista, ele não conseguirá, pois os sets só aceitam tipos IMUTAVEIS dentro deles


#Forma 2

conjunto = {} --> isso é um dicionario vazio, para ser set, deveremos ter elementos: {1,2,4,'José'}


Ao criarmos sets dessa forma estamos passando diretamente os elementos que queremos no conjunto. Estamos meio que
inserindo os elementos individualmente no conjunto.

Dessa forma, se tentarmos fazer: {[1,2,3], 'José'}, dará erro, pois estamos tentando inserir uma lista 
dentro de um conjunto (set)
------------------------------------------------------------------------------------------------------------------------------

Uma das particularidades do tipo set é que ele gosta de elementos únicos dentro dele — ou seja, não curtem duplicatas.

Se criarmos: meu_set = {1, 2, 3, 2, 1} e fizermos print(meu_set), ele irá exibir apenas os elementos 1,2,3, sem repetição

Outra particularidade do tipo set é que ele não consegue garantir a ordem dos elementos dentro dele. Se criarmos o seguinte set:

set_nomes = {'Nicolas', 'Luiza'}

Ao dermos print(set_nomes), poderemos ter tanto {'Luiza', 'Nicolas'} quanto {'Nicolas', 'Luiza'}. Não dá pra garantir


Dito tudo isso, vamos a alguns exemplos:
'''

conjunto1 = set(['Nicolas', 1, 2, 4, 'José'])
print(conjunto1) #Irá retornar: {1, 'Nicolas', 2, 4, 'José'} (não necessariamente nessa ordem)

conjunto2 = {'Nicolas', 'Maria', 40, 20}
print(conjunto2) #Irá retornar: {'Nicolas', 40, 'Maria', 20} (não necessariamente nessa ordem)

conjunto3 = set('Nicolas')
print(conjunto3) #Irá retornar: {'i', 'c', 'o', 'N', 's', 'l', 'a'}  (não necessariamente nessa ordem)

conjunto4 = set(['Nicolas', 20, 10, ['José', 1]]) #Irá dar erro, pois passamos uma lista dentro de lista


'''
Como sets curtem valores únicos, eles são muito uteis para eliminar valores duplicados de outras estrutura de dados.
Veja abaixo como isso pode ser feito:
'''

lista_valores_repetidos = [1,2,3,1,2,3,1,2,3]

conjunto = set(lista_valores_repetidos) 

#Acima, estamos criando um conjunto com cada elemento da lista_valores_repetidos, mas como os sets curtem valores
# unicos, os valores repetidos da lista foram eliminados. Veja:

print(conjunto) # Retorna: {1,2,3}

#Agora, bastaria transformar esse conjunto com os valores duplicados eliminados em uma lista:

lista_valores_unicos = list(conjunto)

print(lista_valores_unicos) # retorna: [1,2,3]


'''
Como os sets não tem index ( e isso é até meio previsível, pois como falamos, sets não conseguem garantir a ordem dos elementos ),
sempre que quisermos encontrar uma coisa especifica dentro de um set, podemos fazer:
'''

conjunto_nome = set('Nicolas')


if 's' in conjunto_nome:
    print('s', True) #Retorna: s True
else:
    print('Não há essa letra')


