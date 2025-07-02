'''
CRIACAO E DE AMBIENTES VIRTUAIS


1 - Para criar:

No windows tem algumas particularidades, mas para criar nosso ambiente virtual, fazemos: python -m venv nome

OBS: no nome do ambiente virtual, podemos colocar qualquer coisa, mas normalmente usamos "venv"


Ao fazer isso, vamos ter nosso ambiente virtual criado. Dentro dele nós temos a pasta include, a pasta lib, que tudo 
que instalarmos de terceiros no nosso ambiente virtual quando ele estiver ativo irá para a pasta lib. Temos também a 
pasta scripts, que tem todos os executaveis que formos utilizar no nosso ambiente virtual, dentre eles:

→ activate: para ativar o ambiente virtual (tanto no cmd quanto no powershell). Geralmente usamos esse

→activate.bat: para o cmd

→activate.ps1: só para o powershell

→deactivate.bat: quando meu ambiente estiver ativo, podemos usar deactivate para desativá lo

→pip.exe: instalador de pacotes do python

→ pip3.10.exe, pip3.11.exe, pip3.exe, python.exe, pythonw.exe: executaveis python


2 - Para ativar:

Para ativar o ambiente virtual no windows, nós remos que acessar a pasta do nosso ambiente virtual, depois scripts e 
depois activate, ou seja, vamos digitar no terminal: nome_ambiente_virtual\Scripts\activate

Uma coisa interessante é que se chegarmos no terminal antes de ativar o ambiente virtual e digitar:
gcm python.exe -Syntax, veremos que será retornado para nós um caminho (path), esse caminho é local do nosso
python global (ou seja, o python instalado em nossa maquina), o que indica que é esse python que está sendo
utilizado por nós no momento. Após ativarmos o ambiente virtual, se fizermos gcm python.exe -Syntax, veremos que
será nos retornado um caminho diferente, isso acontece porque a partir do momento que ativamos o ambiente virtual
estaremos utilizando o python venv, ou seja, o python do ambiente virtual. Esse comando é importante para nos 
certificarmos que estamos utilizando o python correto 

Outra maneira de verificar isso é, antes de ativar o ambiente virtual, ir no canto inferior direito do nosso VSCode 
e haverá uma opção com uma versão assim: 3.xx.x.Ao ver essa opção, se depois da versão não tiver algo como 
('venv': venv), mas sim 64-bit, isso siginifica que estamos usando nosso python global, então bastaria clicar nessa 
opção e aí abrirá uma aba no topo de nossa tela com duas opções:

Python 3.xx.x ('venv': venv) .\venv\Scripts\python.exe    

Python 3.xx.x 64-bit ~\AppData...

A partir disso, selecionariamos a opção ('venv': venv) para utilizar o python do ambiente virtual e depois ativamos
o ambiente virtual escrevendo apenas activate no terminal

3 - Para desativar:

Para desativar nosso ambiente virtual, basta ter o ambiente virtual ativado e digitar: deactivate

'''