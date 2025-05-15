'''
SALVANDO DADOS PYTHON EM JSON

Bom, uma coisa MUITO IMPORTANTE que veremos em python é salvar dados python em json
e converter dados json em dados python. Isso é muito útil e importante porque futuramente
veremos o conceito de APIs. Não precisamos entrar muito afundo nesse conceito, mas saiba que
API é algo amplamente utilizado em desenvolvimento web e que envia e recebe dados em formato JSON.
Portanto, é importante que saibamos como fazer essa conversão


Certo, agora que entendemos a importancia e utilidade disso, temos que entender sobre o que é
JSON.

- O que é JSON

JSON (JavaScript Object Notation) é basicamente uma estrutura de dados que foi criada para nós 
transportamos ou salvarmos dados. Ela vai ser muito similar ao dicionário do python

Para criar um arquivo JSON colocamos a extensão .json no arquivo.

No JSON podemos ter 6 tipos de dados: boolean, númerto (tanto int como float), null, string, 
array e um objeto (alguma coisa que tem mais de um valor) 

....


Agora que entendemos sobre o que é JSON, vamos entender como podemos

#1 Para começar, importamos o modulo json

import json

#2 Depois, com o nosso dicionário em mãos, como queremos salvar nossos dados do dicionário num arquivo, 
vamos fazer  with open utilizando .json na extenção e utilizando o modo w (para escrever)

with open('arquivo.json', 'w') as arquivo:
    json.dump(dicionario, arquivo)

Feito isso, pronto. Nosso arquivo JSON estará criado

...





'''