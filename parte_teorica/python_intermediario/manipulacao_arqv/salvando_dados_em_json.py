'''
SALVANDO DADOS PYTHON EM JSON

Bom, uma coisa MUITO IMPORTANTE que veremos em python é salvar dados python em json
e converter dados json em dados python. Isso é muito útil e importante porque futuramente
veremos o conceito de APIs. Não precisamos entrar muito afundo nesse conceito, mas saiba que
API é algo amplamente utilizado em desenvolvimento web e que envia e recebe dados em formato JSON.
Portanto, é importante que saibamos como fazer essa conversão

Certo, agora que entendemos a importancia e utilidade disso, temos que entender sobre o que é
JSON.

- O que é JSON:

JSON (JavaScript Object Notation) é basicamente uma estrutura de dados que foi criada para nós 
transportamos ou salvarmos dados. Ela vai ser muito similar ao dicionário do python

Para criar um arquivo JSON colocamos a extensão .json no arquivo.

No JSON podemos ter 6 tipos de dados: boolean, númerto (tanto int como float), null, string, 
array e um objeto (alguma coisa que tem mais de um valor) 
....

Agora que entendemos sobre o que é JSON, vamos entender como podemos converter dados python para JSON

#1 Para começar, importamos o modulo json e preparamos nosso dicionário

import json


pessoa = {
    'nome: 'Nicolas',
    'sobrenome': 'Carreira',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55}
    ],
    'altura': 1.7,
    'numeros_preferidos': (2,4,6,8,10),
    'dev': True
    'nada': None
}

#2 Depois, com o modulo importado e nosso dicionário em mãos, como queremos salvar nossos dados do dicionário 
em um arquivo, vamos fazer o with open utilizando .json na extenção do arquivo e utilizando o modo w (para escrever)

with open('arquivo.json', 'w') as arquivo:
    json.dump(dicionario, arquivo)

Feito isso, pronto. Nosso arquivo JSON estará criado. O único problema, é que o JSON todo do nosso dicionário estará
em uma linha só do arquivo, de uma maneira meio estranha. Então para deixar certinho, da mesma forma que criamos o
dicionário, bastaria ir em json.dump e adicionar um argumento de indent=2, ficando:

with open('arquivo.json', 'w') as arquivo:
    json.dump(dicionario, arquivo, indent=2)


Além disso se alguns caracteres tiverem ficado meio estranhos na conversão de dicionario para JSON (normalmente são 
os caracteres com acento), poderíamos adicionar ao nosso json.dump um argumento chamado ensure_ascii=False, ficando:

with open('arquivo.json', 'w') as arquivo:
    json.dump(dicionario, arquivo, indent=2, ensure_ascii=False)


    
Perfeito. Agora, para converter de JSON para python, faremos:

with open('arquivo.json', 'r') as arquivo:
    json.load(arquivo)

OBS: Note que agora usamos o modo 'r' (modo de leitura), pois vamos ler o que está no JSON e depois carregamos (load)
o que está nele.

Certo, agora vamos a algumas observações da conversão dicionario/JSON:

# 1 - A tupla, ao convertermos para JSON vira um array e se voltarmos para python novamente, vira uma lista 

# 2 - a estrutura de dados JSON é muito simples, ela não suporta coisas que executam ações (funções, métodos, classes..), 
mas coisas que conseguimos converter de python para o json (como vimos anteriormente), podem ser convertidas.



...





'''