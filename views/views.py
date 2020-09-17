from tkinter import Frame, Button, Canvas, Label, Radiobutton, Entry, StringVar


class SidePanel(object):
    """docstring for SidePanel"""
    def __init__(self, root):
        self.frame1 = Frame(root)
        self.frame1.pack(side="top", fill="both", expand=1)

        # radio_btn
        self.frame4 = Frame(self.frame1, pady=5, padx=20)
        self.frame4.pack()
        self.opc = StringVar()

        self.lblopc1 = Label(self.frame4,
                             text="Quadrado").pack(side="left", fill="both")
        self.opc1 = Radiobutton(self.frame4,
                                variable=self.opc,
                                value="Quadrado",
                                command=self.call_rdbtn
                                ).pack(side="left", fill="both")

        self.lblopc2 = Label(self.frame4,
                             text="Circulo").pack(side="right", fill="both")
        self.opc2 = Radiobutton(self.frame4,
                                variable=self.opc,
                                value="Circulo",
                                command=self.call_rdbtn
                                ).pack(side="right", fill="both")

        # container com os inputs
        self.container = Frame(self.frame1, pady=10, padx=20)
        self.container.pack()

        self._lblfig = Label(self.container,
                             text="Lado:",
                             font=("Verdana", "10"),
                             width=10, padx=20, pady=5)
        self._lblfig.pack(side="left")

        self.txtfig = Entry(self.container, font=("Verdana", "10"), width=10)
        self.txtfig.pack(side='left')

        self._lblarea = Label(self.frame1, text='',
                              font=('Verdana', '10', 'italic'), padx=0, pady=0)
        self._lblarea.pack()

        # btns
        self.frame3 = Frame(self.frame1, pady=5, padx=20)
        self.frame3.pack(side="top")
        self.btndesenhar = Button(self.frame3, text="Desenhar")
        self.btndesenhar.pack(side="top", fill="both")
        self.btncalc_area = Button(self.frame3, text="Calcular Área")
        self.btncalc_area.pack(side="top", fill="both")
        self.btnlimpar = Button(self.frame3, text="Limpar")
        self.btnlimpar.pack(side="top", fill="both")

        # msgs
        self._lblmsg = Label(self.frame1, text='',
                             font=('Verdana', '9', 'italic'), pady=5, padx=20)
        self._lblmsg.pack()

    def call_rdbtn(self):
        # criar as entradas p capturar os dados
        # alterar apenas o texto delas
        guest = self.opc.get()
        if guest == "Quadrado":
            self._lblfig["text"] = "Lado:"
        else:
            self._lblfig["text"] = "Raio:"
        self.limpar_area()

    def set_lblmsg(self, msg):
        self._lblmsg["text"] = msg

    def set_lblarea(self, msg):
        self._lblarea["text"] = msg

    def get_lblfig(self):
        return self._lblfig["text"][:-1]

    def limpar_tela(self):
        self.limpar_area()
        self.limpar_msg()
        # self.txtfig.delete(0, "end")

    def limpar_msg(self):
        self._lblmsg["text"] = ''

    def limpar_area(self):
        self._lblarea["text"] = ''


class TelaPintura(object):
    """docstring for TelaPintura"""

    def __init__(self, root):
        self.frame = Frame(root)

        self.canvas = Canvas(master=self.frame, width=400, height=400)

    def limpar_tela(self):
        self.canvas.delete("all")


class View(object):
    """docstring for View"""

    def __init__(self, root, quadrado, circulo, desenhista, tela):

        self.quadrado = quadrado
        self.circulo = circulo
        self.desenhista = desenhista
        self.tela = tela
        self.tela.frame.pack(side="left", fill="both", expand=1)

        self.side_panel = SidePanel(root)
        self.side_panel.btndesenhar.bind("<Button>", self.desenhar)
        self.side_panel.btncalc_area.bind("<Button>", self.calc_area)
        self.side_panel.btnlimpar.bind("<Button>", self.clear)
        self.tela.canvas.grid(padx=2, pady=2, row=0, column=0)

    def desenhar(self, event):
        # limpar os campos após desenhar
        # self.clear("teste")
        guest = self.side_panel.opc.get()
        self.side_panel.limpar_msg()
        self.side_panel.limpar_tela()
        try:
            x = float(self.side_panel.txtfig.get())
            if guest == "Quadrado":
                # c = self.model[0](float(self.side_panel.txtfig.get()))
                self.quadrado.set_lado(x)
                self.desenhista.desenhar(self.quadrado)
            else:
                # c = self.model[1](float(self.side_panel.txtfig.get()))
                self.circulo.set_raio(x)
                self.desenhista.desenhar(self.circulo)
            # c.desenhar(self.canvas)
        except ValueError:
            self.exbir_msg()

    def clear(self, event):
        # self.canvas.delete("all")
        self.tela.limpar_tela()
        self.quadrado.set_lado(0)
        self.circulo.set_raio(0)

        # arrumar os buttons
        self.side_panel.limpar_tela()

    def calc_area(self, event):
        guest = self.side_panel.opc.get()
        self.side_panel.limpar_msg()
        try:
            x = float(self.side_panel.txtfig.get())
            if guest == "Quadrado":
                self.quadrado.set_lado(x)
                area = round(self.quadrado.calc_area(), 2)
            else:
                self.circulo.set_raio(x)
                area = round(self.circulo.calc_area(), 2)
            msg = f'Área do {guest}: {area}'
            self.side_panel.set_lblarea(msg)
        except ValueError:
            self.exbir_msg()

    def exbir_msg(self):
        msg = "Valor de " + self.side_panel.get_lblfig()
        msg += " está incorreto.\n Preencha com um valor adequado!!!"
        self.side_panel.set_lblmsg(msg)
