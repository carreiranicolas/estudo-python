'''
FUNÇÃO ISINSTANCE

Essa função é super útil quando queremos saber de que tipo é um objeto — especialmente em códigos onde o tipo 
pode variar. Para usá-la, utilizamos o seguinte formato: isinstance(item, tipo de dado). A função retorna 
True ou False:

--> True se o objeto for do tipo informado (ou de uma subclasse dele).

--> False caso contrário.

Veja um exemplo:
'''

lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2),
    {0,1}, {'nome': 'Nicolas'}
]

for item in lista:
    print(item, isinstance(item, set)) # Retorna: a False
                                                # 1 False
                                                # 1.1 False
                                                # True False
                                                # [0, 1, 2] False
                                                # (1, 2) False
                                                # {0, 1} True
                                                # {'nome': 'Nicolas'} False




'''
Acima, nós utilizamos o isinstance() para verificar se cada item da lista é um set. Se for, será retornado True, 
se não for, será retornado False. 

Poderíamos passar para o isinstance checar se é mais de um tipo. Então se queremos checar se determinado item é 
numérico (ou int ou float), ao invés de criar dois isinstance um com int e outro com o float, criaríamos apenas 
um com uma tupla de int e float. Veja abaixo:
'''

for item in lista:
    if isinstance(item, (int, float)):
        print(item, item * 2) #Retorna: 1 2
                                        # 1.1 2.2
                                        # True 2


'''
Portanto, veja que passamos int e float no isinstance e caso for UM DOS DOIS, ele irá retornar True, entrar no if e 
executar o código dentro dele. Perceba ainda que um dos itens nao é um número, é um booleano. Acontece que em Python, 
os valores booleanos são tratados como númericos, 1 e 0, respectivamente. Por isso, aparece True 2, pois o 1 (que 
representa o True), foi multiplicado por 2.

'''