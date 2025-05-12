'''
SOBRE __init__.py


Continuando com a estrutura das aulas de pacote, suponhamos que tivéssemos:

meu_pacote/
│
├── modulo1.py
└── modulo2.py
teste.py

Agora, vamos criar o arquivo __init__.py em nosso pacote

meu_pacote/
├──__init__.py
├── modulo1.py
└── modulo2.py
teste.py

Esse arquivo __init__.py meio que engana o python. Quando quisermos utilizar a função somar() 
que está dentro do módulo __init__, nós não precisamos escrever “from meu_pacote.__init__ import soma”, 
ao invés disso, podemos importar diretamente o pacote fazendo “import meu_pacote” e obtendo a função somar que está dentro de __init__.py.

É como se nosso pacote passasse a se comportar como um módulo

Algo interessante é que podemos ir lá no modulo __init__.py e fazer:

from meu_pacote.modul import *

Ao fazer isso, quando nós vamos em teste.py e fazemos:

import meu_pacote

Nós poderemos utilizar sem problemas aquilo que era do modulo2.py que fica dentro de meu_pacote



'''