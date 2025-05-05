'''
MODULOS PESSOAIS - IMPORTAÇÃO

Bom já entendemos que modulos são arquivos que possuem código Python, mas algo extremamente interessante
é que podemos fazer a importação de modulos pessoais. Aí você deve estar se perguntando como isso é
possível? Nós já não dissémos que módulos são basicamente arquivos que possuem código python? Então,
quando estamos fazendo algo em python, nós temos justamente um arquvio com código python, então podemos
importar as coisas que tem nesse arquivo (funções, variáveis..) em outros arquivos. Mas uma observação
importante é que temos que tomar cuidado para não criar nome de modulos que já existem. Exemplo: 
Você cria um módulo (arquivo) chamado sys, você terá problemas ao importar o módulo sys


Desta forma, nós modularizamos nosso programa, pois se tivermos criado uma função que faz algo em outro
arquivo Python nosso, nós podemos reutiliza-lo em outros arquivos, facilitando as coisas evitando a
repetição de código

Se o arquivo que você estiver, está na mesma pasta do arquivo (módulo) que você quer importar, podemos fazer: 
import modulopessoal, assim como vimos no arquivo de conceitos 

Além disso, para modulos pessoais também conceguimos importar apenas partes do modulo (funções, variaveis..).
Para isso, basta fazer: from modulopessoal import soma, assim como vimos no arquivo de conceitos também

Algo interessante que podemos fazer pasa visualizar a importação do modulo é o seguinte: 

O arquivo principal nosso, aquele que estamos utilizando é chamado de __main__, então se fizermos
print('Este módulo se chama:', __name__) no nosso módulo principal, isso irá retornar:

Este módulo se chama __main__

Uma pequena observação que será importante durante essa explicação é que o primeiro módulo que é executado pelo python 
em nosso programa é chamado de __main__. Ou seja, o __main__ é sempre executado primeiro. Lembre disso.

Agora, suponhamos que nós tenhamos um arquivo (módulo) que queremos importar que se chama importe.
Quando formos para ele e fizermos print('Este módulo se chama:', __name__), isso irá nos retornar
Este módulo se chama __main__, assim como aconteceu no primeiro arquivo. Isso acontece porque abrimos
o arquivo importe, então ele meio que "se torna nosso arquivo principal"

Bom, sabendo disso, se formos ao nosso primeiro arquivo e dermos: import importe e executarmos o
primeiro arquivo (lembrando que o primeiro arquvio tinha dentro dele um print print('Este módulo se chama:', __name__), 
enquanto o arquivo importe também tinha dentro dele print('Este módulo se chama:', __name__)), o que acontecerá é
que será exibido para nós:

Este módulo se chama: importe
Este módulo se chama: __main__

Ou seja, o que aconteceu é que o __main__  que foi exibido é do primeiro arquivo, que foi o módulo executado primeiro 
(uma vez que o __main__ é sempre executado primeiro, lembra?) e o importe que foi exibido pertence ao importe.py, que
foi o módulo executado por último (apesar da ordem que foram exibidas as mensagens não parecer dizer isso). 

Neste momento devem estar se passando por sua cabeça algumas dúvidas:

1 - Mas como sabemos que o __main__ pertence ao primeiro arquivo?

R: Porque o arquivo que estamos UTILIZANDO, aquele que estamos com ele aberto, é sempre o nosso __main__

2 - Por que foi exibido 'Este módulo se chama: importe'?

R: É porque dentro do módulo importe, tem um print('Este módulo se chama:', __name__). Com isso, quando importamos
o modulo importe para o nosso primeiro arquivo e excutamos o primeiro arquivo, ele basicamente executa o modulo
importado (importe) e assim acaba exibindo o print('Este módulo se chama:', __name__) do modulo importe e, como
estamos utilizando o nosso primeiro arquivo, o modulo importe não será o __main__ então seu __name__ será o 
próprio nome do módulo (que é importe)

'''



'''
MODULOS PESSOAIS - USANDO/IMPORTANDO COISAS

Bom, seguindo com o exemplo da aula anterior, se tivéssemos dentro do nosso módulo importe a seguinte
variavel:

saudacao = 'Olá'

Para utilizar essa váriavel do módulo importe no nosso primeiro arquivo, temos algumas formas de fazer:

1- nome_modulo.variavel

A primeira forma é bem simples, basta você 


'''