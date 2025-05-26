'''
METODOS UTEIS PARA A MANIPULAÇÃO DE ARQUIVOS

Agora que já passamos pelo open e entramos finalmente no with open. Veremos alguns métodos que podem ser 
utilizados no with open para a manipulação dos arquivos criados.

É importante dizer antes que os métodos que estarão disponiveis para serem utilizados no with open irão variar
conforme o modo que estivermos utilizando nele. Exemplo: Em um with open com módulo 'r' eu não terei um método 
.write()


Entendido isso, vamos aos métodos


# Usando o modo 'w'

--> .write(): Nesse método, nós passamos uma string para dentro dele e a string que passamos para ele, será
escrita em nosso arquivo. Exemplo:

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Oi') # 'Oi' será escrito em nosso arquivo

OBS: Se fizermos, por exemplo, um arquivo.write('Oi') e depois, embaixo dele, fizermos outro arquivo.write('Tudo bem'), 
não haverá quebra de linha, ficará: OiTudo bem. Portanto, teríamos que fazer:

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Oi\n')
    arquivo.write('Tudo bem\n')  


--> .writelines(): Nesse método, podemos passar várias linhas para serem escritas no nosso arquivo de uma só
vez. Veja um exemplo:


with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Oi\n')
    arquivo.write('Tudo bem\n') 
    arquivo.writelines(('Com\n', 'Você?\n'))


    
OBS: Uma observação muito importante é que se nós estivermos utilizando o modo 'w+' (nesse modo, além de escrever,
conseguimos ler tambem) e após tivermos escrito, nós quisermos ler o que foi escrito, nós precisamos colocar o 
cursor no começo novamente no começo, porque após escrever, o cursor fica lá embaixo. Para colocar o cursor no 
começo do arquivo, fazemos .seek(0,0). Veja abaixo:

ANTES DO .SEEK(0,0):

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Oi\n')
    arquivo.write('Tudo bem\n') 
    arquivo.writelines(('Com\n', 'Você?\n'))
    print(arquivo.read()) #Retornará nada em nosso terminal, pois o cursor está la embaixo, depois do conteudo escrito


DEPOIS DO .SEEK(0,0):

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Oi\n')
    arquivo.write('Tudo bem\n') 
    arquivo.writelines(('Com\n', 'Você?\n'))
    arquivo.seek(0,0)
    print(arquivo.read()) #Retornará em nosso terminal: 
    
# Usando o modo 'r'

--> .read(): Nesse método, ele irá ler tudo o que foi escrito no nosso arquivo e exibir em nosso terminal. Portanto, 
para exemplificar, veja o que acontece se tivéssemos escrito "Oi" no nosso arquivo e quiséssemos ver o que está
escrito no arquivo com o .read():

with open(caminho_arquivo, 'r') as arquivo:
    arquivo.read() # Iria exibir em nosso terminal: 'Oi'
                                                    'Tudo bem'
                                                    'Com'
                                                    'Você?'


--> .readline(): Esse método irá ler linha por linha o que foi escrito no arquivo e exibir em nosso terminal.
Ele é tipo um next(). Veja um exemplo:


with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.readline()) #Irá exibir no terminal: 'Oi'



OBS: Um detalhe é que como nós quebramos a linha a cada linha que escrevemos lá no write, e o print também tem quebra 
de linha, então quando fizermos vários print(arquivo.readline()), pode ser que aconteça dele pular linhas, então 
para resolver isso, podemos utilizar o end='' no print ou o método de string strip(). Veja:


ANTES:

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline()) #Irá exibir no terminal:  'Oi'

                                                        'Tudo bem'

                                                        'Com'

                                                        'Você?'
                                                       

Perceba acima que ele pula linhas.


DEPOIS:
    
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.readline(), sep='')
    print(arquivo.readline(), sep='')
    print(arquivo.readline(), sep='')
    print(arquivo.readline(), sep='') #Irá exibir no terminal:  'Oi'
                                                        'Tudo bem'
                                                        'Com'
                                                        'Você?'


Agora, como tiramos a quebra de linha que acontece por padrão no print fazendo sep='', ele não pulará mais linhas.



--> .readlines(): Esse método irá ler tudo que foi escrito no arquivo e gerar uma lista com o que foi escrito.
Assim, conseguimos iterar o que foi escrito usando o for. Veja:

with open(caminho_arquivo, 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha + 'N', sep='') #Irá exibir no terminal: 'Oi'
                                                            'Tudo bem'
                                                            'Com'
                                                            'Você?'
'''