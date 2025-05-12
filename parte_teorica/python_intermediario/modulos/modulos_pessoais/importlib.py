'''
RECARREGANDO MODULOS COM IMPORTLIB

Bom, agora que já entendemos sobre a importação de modulos. Algo que precisamos falar é que
O módulo que nós importamos para o nosso programa é o que conhecemos como Singleton. 

Singletons  quer dizer que só pode existir uma instancia daquela coisa no programa inteiro e
nquanto o programa está executando. Ou seja, se fizermos um for para importar um módulo 10 vezes, 
por exemplo, o código será executado, óbvio, mas o módulo é importado apenas uma vez, por que ele é 
um singleton, o que significa que só podemos ter uma instancia dele no programa.

Esse conceito ainda é algo avançado que veremos bem mais pro futuro, mas a importancia de entendermos 
isso é por conta de um modulo chamado de importlib

O importlibnos permite recarregar algum modulo que quisermos. Para isso, faríamos:

import importlib

importlib.reload(nome_modulo).

A partir disso, no exemplo que demos do loop for, se tivéssemos dentro do loop for: importlib.reload(modulo)
ao invés de import modulo, o modulo seria carregado as 10 vezes que o loop for rodasse

Para visualizar isso melhor, podemos pensar no seguinte exemplo:

Nós temos um arquivo (modulo) chamado importe e temos um outro arquivo (modulo) chamado principal.
No arquivo que chamamos de importe, nós temos dentro dele: print('Olá, sou o __name__) e dentro do
arquivo principal, suponhamos que tivesse o seguinte código:

for c in range(3):
    import importe

print('Sou o principal')

O retorno do código acima seria:

# Olá, sou o importe
# Sou o principal

Já sabemos o porquê do "Olá, sou o importe" ser exibido, caso queira rever isso, vá ao arquivo de conceito de
modulos_pessoais. O ponto de atenção no código acima é que colocamos o import importe dentro do loop for, então
não era para o modulo importe ser importado 3 vezes (porque temos o range(3)) e consequentemente exibir 
"Olá, sou o importe" 3 vezes? 

A resposta para isso é NÃO, uma vez que modulos são Singletons, como dissémos mais acima. No entanto, 
caso você quisesse mesmo assim importar um modulo várias vezes (chamamos isso de RECARREGAR UM MODULO)
você poderia utilizar o modulo importlib, então você faria:

import importlib

for c in range(3):
    import importlib.reload(importe)

print('Sou o principal')

Dessa forma, utilizando o importlib, o módulo importe seria recarregado 3 vezes (e consequentemente exibindo 
"Olá, sou o importe" 3 vezes). Assim, o retorno do código acima seria:

# Olá, sou o importe
# Olá, sou o importe
# Olá, sou o importe
# Sou o principal

Portanto, para RESUMIR. Se quisermos "REIMPORTAR" modulos, ou seja, importar um mesmo modulo mais de uma vez durante
a execução do nosso programa, podemos utilizar o importlib

'''