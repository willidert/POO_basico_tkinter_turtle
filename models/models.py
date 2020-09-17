from abc import ABC, abstractmethod  # p usar as propriedades de uma classse abstrata
from math import pi  # biblioteca matemática p usar o valor de Pi
import turtle  # pacote p desenhar as figuras


class FigGeometrica(ABC):
    """Classe abstrata p aplicar herança e polimorfismo"""
    def __init__(self):
        """em python as variaveis são publicas
            porem existe uma convenção em que _nome representam
            variaveis privadas
            somos todos adultos concordando aqui"""
        self._ponto = (0, 0)

    @abstractmethod
    def calc_area(self):
        pass

    def get_ponto(self):
        return self._ponto


class Quadrado(FigGeometrica):
    """docstring for Square"""
    def __init__(self, lado=0):
        super().__init__()  # chamando o construtor do pai
        self._lado = lado    # em python os atributos são publicos

    def get_lado(self):
        return self._lado

    def set_lado(self, lado):
        self._lado = lado

    def calc_area(self):
        print(self._lado**2)
        return self._lado**2


class Circulo(FigGeometrica):
    """docstring for Square"""
    def __init__(self, raio=0):
        super().__init__()
        self._raio = raio

    def get_raio(self):
        return self._raio

    def set_raio(self, raio):
        self._raio = raio

    def calc_area(self):
        return pi * self._raio**2


class FigDraw(object):
    """
        docstring for FigDraw
        No meu ponto de vista, a responsabilidade de desenhar
        n deve estar na figura geometrica, e sim numa outra classe.
        A única responsabilidade dela é pintar as figuras.
    """
    def __init__(self, canvas):
        self.canvas = canvas
        self.flag = False
        self.t = turtle.RawTurtle(canvas)
        self.t.shape('blank')
        self.t.penup()

    def desenhar(self, figura):
        if isinstance(figura, Quadrado):
            # apenas para corrigir a posição da tartaruga e o desenho n sair torto
            self.t.setpos(-1 * (figura.get_lado()/2), -1 * (figura.get_lado()/2))
            self.t.pendown()

            for i in range(4):
                # densenhando um quadrado
                self.t.forward(figura.get_lado())
                self.t.left(90)

        elif isinstance(figura, Circulo):
            # desenhando o circulo
            self.t.setpos(0, figura.get_raio() * -1)
            self.t.pendown()
            self.t.circle(figura.get_raio())
        self.t.penup()
