'''
PACOTEs (PACKAGES) EM PYTHON 

Outra coisa importante a se falar é sobre pacotes. Vimos que modulos são basicamente arquivos que tem codigo python
(um arquivo .py). Os pacotes são basicamente pastas que possuem dentro delas modulos python.

Veja um exemplo:

meu_pacote/
│
├── modulo1.py
└── modulo2.py

Suponhamos acima que dentro do modulo2 nós tenhamos a função soma abaixo:

def soma(a,b):
    return a + b

Agora suponhamos que nós temos um arquivo (modulo) chamado teste.py (que como podemos ver, não está dentro de 
meu_pacote), e queremos utilizar a função soma (que está dentro do modulo2 que está dentro do pacote meu_pacote).

Para fazer isso, como a função soma acima que está detnro do modulo2, que por sua vez está dentro do pacote 
meu_pacote não temos que importar o pacote, pois ele não faz NADA. Temos que importar o modulo 
dentro do pacote. Ou seja, temos que fazer:

#from meu_pacote.modulo2 import soma --> fazendo dessa forma, usaríamos a função soma fazendo: soma(1,2), por exemplo

Outras forma seria fazer:

#from meu_pacote import modulo2 --> fazendo dessa forma, usaríamos a função soma fazendo: modulo2.soma(1,2), por exemplo

Tem uma terceira forma também:

# import meu_pacote.modulo2 --> fazendo dessa forma, usaríamos a função soma fazendo: meu_pacote.modulo2.soma(1,2), por exemplo

Uma obseervação é que fazendo das duas últimas formas acima, imporataríamos tudo de dentro do modulo2 e não somente 
a função soma.


Agora uma outra coisa que poderia ser feita (e que já vimos no arquivo de conceito de modulos que é uma má prática)
é fazer:


from meu_pacote.modulo2 import *

Já vimos que o uso do asterisco é uma prática, porém, algo interessante sobre o uso do asterisco é que  podemos ir 
no módulo que estamos importando tudo com o asterisco e utilizar um __all__. Ao fazer isso, podemos incluir o que 
dentro daquele módulo nós queremos importar para outro módulo.

Ou seja, poderíamos ir lá no modulo2 que fica dentro de meu_pacote e adicionar o __all__ da seguinte forma abaixo:

__all__ = [
    'saudacao',
    'temperatura'
]

Ao adicionar isso dentro de modulo2, quando formos importá-lo para o nosso arquivo de teste.py fazendo 
from meu_pacote.modulo2 import *, o que seria importado, na prática, seria só a variavel saudacao e temperatura.
A função soma() não seria importada, porque ela não está dentro de __all__. Portanto, se tentarmos utilizar 
a função soma dentro do nosso arquivo de teste.py, daria erro, pois ele não foi importada, o que seria diferente
se tentarmos utilizar as variaveis saudacao e temperatura, que foram adicionadas dentro de __all__ e portanto foram
importadas quando utilizamos from meu_pacote.modulo2 import *

'''


'''

ARQUIVOS DENTRO DO MESMO PACOTE

Até agora, tudo que vimos envolvia modulos dentro de pacotes e modulos que estavam fora do pacote. Portanto, até o
exato momento, tudo que vimos relacionado a importação de modulos/importação de funções de modulos dentro de pacotes
estava relacionado com um arquivo (modulo) que não pertencia ao pacote que queriamos importar os modulos/funções  

Mas agora, e se estivéssemos dentro do modulo1 que assim como o modulo2 está dentro de meu_pacote e quiséssemos utilizar somente a função
soma que está dentro do modulo2? Aí como ambos estão dentro do mesmo pacote, bastaria fazer:

--> from modulo2 import soma


(Portanto, para arquivos de um mesmo pacote, a importação é feita NORMALMENTE (da mesma forma que vimos no arquivo de conceito de modulos))

Nada que não tenhamos visto. Mas agora, um GRANDE DETALHE:

Se formos para o nosso teste.py (que está FORA de meu_pacote) e tentarmos importar qualquer coisa do modulo1 fazendo:

from meu_pacote.modulo1 import algo

Se tentarmos fazer isso acima, isso dará ERRO. O que acontece é que dentro de modulo1 nós temos: from modulo2 import soma
Com isso, o python, quando vai fazer a importação de algo do modulo1, também tenta fazer essa importação que está sendo feita no
modulo1 (from modulo2 import soma), mas ele não consegue encontrar o módulo modulo2.py, pois o teste.py, que é o nosso main
não está dentro de meu_pacote


Para resolver isso, nós teríamos que ir lá em modulo1.py e reescrever o import dele. Veja:

ANTES:

--> from modulo2 import soma


DEPOIS:

--> from meu_pacote.modulo2 import soma


Portanto, podemos fazer "import modulo" ou "from modulo import algo" para arquivos que estão no mesmo pacote. No entanto, temos que
ficar atento se estivermos fazendo isso e o nosso main for um arquivo de fora do pacote.

'''
