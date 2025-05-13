'''
SOBRE __init__.py


Continuando com a estrutura das aulas de pacote, suponhamos que tivéssemos:

meu_pacote/
│
├── modulo1.py
└── modulo2.py
teste.py

Quando vamos em teste.py e fazemos:

import meu_pacote

Ao fazer isso, sabemos que não estamos fazendo NADA, pois a importação de pacotes
não faz nada. Vimos isso na aula de conceito de pacotes. 

Mas agora, imagine vamos criar o arquivo __init__.py em nosso pacote:

meu_pacote/
├──__init__.py
├── modulo1.py
└── modulo2.py
teste.py

Agora imaginemos que dentro do arquivo (modulo) __init__.py nós temos:

saudar = 'Olá!'

despedir = 'tchauu'


O que acontece é que esse arquivo __init__.py meio que engana o python. Quando quisermos utilizar a váriavel saudar
que está dentro do módulo __init__, nós não precisamos escrever “from meu_pacote.__init__ import saudar”, 
ao invés disso, podemos importar diretamente do pacote fazendo “import meu_pacote” e obtendo a variavel saudar que está dentro de __init__.py.
É como se nosso pacote passasse a se comportar como um módulo


Agora, suponhamos que estamos no nosso modulo teste.py e queremos usar uma função soma, por exemplo, que esteja em modulo2 sem ter que fazer toda aquela importação verbosa e chata.
Queremos apenas dar um "import meu_pacote" e poder utilizar a função soma que está no modulo2 (que por sua vez está dentro de meu_pacote, assim como __init__.py). Para fazer isso, 
podemos ir lá no modulo __init__.py e fazer:

from meu_pacote.modulo2 import * --> (obs: como vamos fazer algo que envolve o teste.py que está fora do pacote, faremos a importação do modulo2 em __init__.py desta maneira.
Caso queira saber mais detalhes sobre isso, vá até o arquivo de conceito de pacotes e veja a parte de ARQUIVOS DENTRO DO MESMO PACOTE (e pontos de vista) )

Ao fazer isso, quando nós vamos em teste.py e fazemos:

import meu_pacote

Nós poderemos utilizar sem problemas aquilo que era do modulo2.py que fica dentro de meu_pacote

Portanto, o __init__.py é muito prático e permite que nosso pacote se comporte quase como um módulo. Torna tudo mais simples

'''