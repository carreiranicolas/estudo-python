'''
USO DE REQUIREMENTS PARA FACILITAR 

A partir do nosso pip freeze (lista todos os pacotes instalados no ambiente virtual), podemos criar um arquivo 
chamado requirements.txt. Nesse arquivo, nós teremos todos os pacotes, bibliotecas, dependencias que foram instalados
em nosso ambiente virtual. Isso é muito útil porque, a partir disso que teremos dentro do nosso requirements.txt,
nós podemos recriar nosso ambiente virtual de forma ágil, sem ter que instalar as bibliotecas do antigo ambiente
virtual uma a uma

Para gerar o requirements.txt, basta fazer: pip freeze > requirements.txt 

Agora, para instalar as coisas do requirements.txt em um novo ambiente virtual, por exemplo, nós fazemos:
pip install -r .\requirements.txt


'''