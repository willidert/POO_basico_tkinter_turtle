from tkinter import Tk
from models.models import Quadrado, Circulo, FigDraw
from views.views import View, TelaPintura


class Controller(object):
    """docstring for Controller"""
    def __init__(self):
        self.root = Tk()
        # arrumar aqui
        self.tela = TelaPintura(self.root)
        self.desenhista = FigDraw(self.tela.canvas)
        self.quadrado = Quadrado()
        self.circulo = Circulo()
        self.view = View(self.root,
                         self.quadrado,
                         self.circulo,
                         self.desenhista,
                         self.tela)

    def run(self):
        self.root.title("Tkinter MVC with POO")
        self.root.deiconify()
        self.root.mainloop()
