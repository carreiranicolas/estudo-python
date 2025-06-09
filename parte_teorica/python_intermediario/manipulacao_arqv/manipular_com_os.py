'''
MANIPULANDO OS ARQUIVOS COM OS

Já que estamos falando bastante sobre arquivos, um modulo que não poderia ficar de fora é o modulo python
os. Nós veremos ele mais em detalhe no curso, porém esse modulo é muito útil e tem coisas que é importante
de sabermos desde já.

Bom, para importar o modulo, fazemos, obviamente: 

import os

Certo, com isso, tem 3 coisas principais que é importante de sabermos a fazer com esse modulo:

- Apagar arquivos

- Renomear arquivos

- Mover arquivos

Perfeito, entendido isso, vamos dizer que temos um arquivo txt criado a partir com o with open:

import os   

caminho_arquivo = '/teste/arquivo.txt'

with open(caminho_arquivo, 'w', encoding ='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Nicolas\n')

A partir disso, podemos remover (excluir) o arquivo fazendo:

os.unlink(caminho_arquivo)  OU os.remove(caminho_arquivo) --> (Ambos fazem a mesma coisa.)

Se o arquivo não existir, obviamente dará erro.

Perfeito. Agora, outra coisa que pode ser feita é renomear o nome do nosso arquivo fazendo:

os.rename('velho_nome.txt', 'novo_nome.txt')

Além disso, o os.rename() pode ser utilizado para mover arquivos/diretórios. Veja:

os.rename('arquivo.txt', 'subpasta/arquivo.txt')



'''