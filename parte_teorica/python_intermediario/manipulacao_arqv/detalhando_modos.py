'''
DETALHANDO MODOS

Bom, nos outros arquivos (metodos e criando_arquivos), nós já conseguimos ver bastante dos modos, mas fazendo um 
apanhado geral:

Sabemos que o r, podemos ler um arquivo que exista. w é um modo de escrita, que não faz leitura e cria o arquivo se 
ele não existir. O + adiciona a possibilidade de escrita no r e adiciona a possibilidade de leitura no w, ou seja,
com o '+', o 'w' e o 'r' passam a fazer basicamente tudo.

A diferença entre o w e o a é que o w abre o arquivo, apaga tudo que estava nele e escreve o que você mandar, enquanto
o 'a' não apaga nada e começa a escrever no final do arquivo. O modo 'a' é muito útil para escrever arquivos de log,
por exemplo, que são arquivos onde precisamos ter o registro constante de algo


Além disso, temos o modo 'b'. Ele dificilmente é utilizado para é interessante saber seu uso. Ele serve para abrir
arquivos em modo binário. Com ele, conseguimos trabalhar com imagens, videos, PDFs, audios e arquivos compactados


Um detalhe MUITO IMPORTANTE de se saber é que, quando vamos escrever em qualquer arquivo, existem alguns caracteres
que podem dar algum problema. Exemplo:


with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Atenção\n')


Isso acima poderia dar problema no arquivo que estamos tentando escrever porque o 'ç' e o 'ã' são caracteres que
costumam dar problema, então para que isso não aconteça, quando formos escrever em qualquer arquivo, é interessante
que passemos o encoding='utf8' da seguinte forma:

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')

Assim, não teriamos problemas no arquivo que estamos escrevendo
'''