#POO básico com Tkinter e Turle

Trabalho de Processo e modelagem de Software para reforço dos conceitos básicos de POO.
Usei o mesmo exemplo base proposto e adaptei aplicando os mesmos conceitos na linguagem Python.

##Executando

Em qualquer interpretador Python3, rode `python3 app.py`. Não tem misterio.

##Abstração

Serve para representar um conceito. A classe abstrata `FigGeometrica` que serve de base para outras figuras. Uso as classes `Circulo` e `Quadrado`. E na class `FigDraw` responsavel p desenhar as figuras.

##Encapsulamento

Ocultar informação dentro da classe, de modo que apenas o objeto possa manipular seus atributos.
Em Python os atributos são publicos por padrão e não existem modificadores de visibilidade. A a convenção da comunidade `_nome` que representa um atributo privado na linguagem. Implemento ainda métodos `get` e `set` para manipular os atributos agora 'privados'.

##Herança

É um mecanismo que permite reaproveitar caracteristicas comuns a diversas classes. Uso nas classe `Circulo` e `Quadrado` que herdam caracteristicas comuns de `FigGeometrica`

##Polimorfismo

É caracteristica que ocorre quando duas ou mais classes derividas de uma superclasse apresentam o mesmo método porém com comportamento diferente. Uso no método `calc_area()` onde a formula é diferente para cada figura geométrica.

##MVC(Model View Controller)

Uma técnica de desenvolvimento onde se busca isolar as partes comuns do sistema, apliquei usando tkinter. Tive alguns problemas uma vez que a manipulação dos dados em tkinter não me permitia aplicar o MVC eficientemente, fiz muitas adaptações para chegar no resultado final.

##MUITO OBG!!!