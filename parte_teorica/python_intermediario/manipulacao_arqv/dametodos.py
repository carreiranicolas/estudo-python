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

    
# Usando o modo 'r'

--> .read()
    





'''