'''
BREAK E CONTINUE

break e continue são mecanismos para controle de loops e podem ser usados para qualquer um dos loops 
(for e while). Com eles, podemos fazer manipulações interessantes dos nossos loops, tornando até o loop
infinito que o while pode criar em algo tranquilo de se lidar. Vamos ver sobre cada um:


--> BREAK: O break busca o loop mais mais próximo dele e quebra, ou seja, para. Dessa forma, se tivermos
um loop infinito, por exemplo, onde dentro dele temos um break, ele estará controlado, pois ele poderá ser
interrompido

--> CONTINUE: O continue irá pular para a próxima repetição do loop, ignorando o que vem depois dele no loop
atual. Então depois do continue ser acionado, se tivermos um código depois dele, aquilo não será executado,
pois ele irá pular para a próxima repetição do loop

Veja na prática:
'''

#BREAK

i = 0
while True:
    if i ==3:
        break
    print(i) #Irá exibir 0 1 2 --> quando chega no 3, ele dá o break
    i+=1

print('-' * 40)

for n in range(5):
    if n == 3:
        break
    print(n) #Irá exibir 0 1 2 --> quando chega no 3, ele dá o break

print('-' * 40)
# CONTINUE

for n in range(6):
    if n == 3:
        continue
    print(n) #Irá exibir 0 1 2 4 5 (lembre-se que o for não conta o valor colocado, mas sim f-1), pulando assim o 3

print('-' * 40)
c = 0
while c < 6:
    if c == 3:
        continue
    print(c) #Era pra exibir 0 1 2 4 5, pulando assim o 3
    c+=1
