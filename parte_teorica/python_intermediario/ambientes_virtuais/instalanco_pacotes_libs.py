'''
INSTALANDO PACOTES E BIBLIOTECAS

pip é o gerenciador de pacotes oficial do Python. Ele serve para instalar, atualizar, remover e listar bibliotecas 
que outras pessoas criaram e disponibilizaram no Python Package Index (PyPI) (para acessar, basta ir em pypi.org)

1 - Instalação (e outros detalhes como versões e atualizações):

Se quiséssemos instalar um pacote pymysql no nosso ambiente virtual, por exemplo, bastaria o ambiente virtual primeiro
e depois digitar no terminal: pip install pymysql

O interessante é que se ficarmos de olho na pasta do nosso ambiente virtual, em Lib, podemos ver que será adicionado 
pymysql

Uma observação é que podemos instalar algo na versão que quisermos. Para listar as versões existentes daquilo que 
vamos instalar nós fazermos, por exemplo: pip index versions pymysql. A partir disso, nós teremos todas as versões, 
aí basta escolher uma e fazer pip install pymysql==1.0.3 e então instalaremos o pymysql nessa versão 

A versão 1.0.3 não é a versão mais recente do pymysql, então se quisermos dar um upgrade no pacote pymysql para a
sua versão mais recente, basta fazer: pip install pymysql -upgrade


2 - Desinstalação:

Se quiséssemos desinstalar o pacote pymysql do nosso ambiente virtual, basta ter o ambiente ativado e digitar no
terminal: pip uninstall pymysql

Novamente, se ficarmos de olho na pasta do nosso ambiente virtual, em Lib, poderemos ver que pymysql será removido

3 - Listar pacotes instalados

Para listar os pacotes que estão instalados em nosso ambiente virtual, basta ter ele ativo e utilizar o comando
pip freeze


'''