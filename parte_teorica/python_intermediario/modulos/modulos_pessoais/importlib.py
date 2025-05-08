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

Veja abaixo um exemplo:
'''