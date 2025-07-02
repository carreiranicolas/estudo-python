'''
AMBIENTES VIRTUAIS

Ambientes virtuais em Python são usados para isolar dependências de projetos. Isso significa que cada projeto 
pode ter suas próprias bibliotecas, sem conflito com outras.


Suponhamos que sejamos web developer e criamos servidores com Django, e aí temos alguns clientes. Ao criar o site do 
primeiro cliente, vamos usar várias coisas para criá-lo (para manipulação de imagem, a versão do django pode ser 
outra, coisas relacionadas a gráficos..) e aí subimos o site deste cliente. Após isso, vamos criar o site de outro 
cliente que faz aplicações de investimento na bolsa, por exemplo, e aí fazemos o site que irá usar coisas 
completamente diferentes. Dessa forma, o site do primeiro cliente possui coisas que não são necessariamente usadas 
no segundo cliente e o segundo cliente pode também ter coisas que não são usadas no primeiro cliente. Isso seria um 
caso de aplicação de ambientes virtuais, pois criaríamos um espaço isolado para cada um dos clientes

Além disso, pense que cada um desses sites desses clientes podem utilizar as mesmas bibliotecas, porém em versões
diferentes, então, se não tivéssemos um ambiente que isolasse esses projetos, pode ser que algum desses projetos
deixasse de funcionar por conta de incompatibilidade de versão.

Geralmente, a versão do python que estamos usando para criar um ambiente virtual é a que será carregada para esse 
ambiente virtual. Se criarmos um ambiente virtual com a versão 3.11 do python, o meu venv geralmente vai ter essa 
versão do python também


Para a criação de ambientes virtuais, o python utiliza nativamente o venv, que é o modulo usado para criar ambientes 
virtuais. Ele é MUITO utilizado

Para entender como é feita a criação do ambiente virtual, vá para o arquivo criacao.py 
'''