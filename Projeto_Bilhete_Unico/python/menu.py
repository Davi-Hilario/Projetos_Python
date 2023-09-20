# Importando Bibliotecas
from dashboard import Dashboard

from tkinter import *

from PIL import ImageTk
from urllib.request import urlopen

#Iniciando aplicação
root = Tk()

class App(Dashboard):

    def __init__(self):
        try:
            self.root = root
            self.config()
            self.frame()
            self.label()
            self.logo()
            self.buttons()
            self.root.mainloop()
        except Exception as erro:
            print(erro)

    def config(self):
        self.root.title("Análise de Hardware") 
        self.root.configure(background='#004480')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=300)

    def frame(self):
        self.container = Frame(
            self.root,
            bd=4, bg='#0072AF', 
            highlightbackground='#00BFFF', 
            highlightthickness=3
            )
        self.container.place(relx=0.05 , rely=0.05, relwidth=0.9, relheight=0.9)
    
    def label(self):
        self.titulo = Label(
            self.container, 
            text="Análise de Caixa Eletrônico", 
            font='Arial 18 bold',
            bg='#0072AF',
            fg='white'
            )
        self.titulo.place(relx=0, rely=.1, relwidth=1, relheight=.1)

    def logo(self):
        
        url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5SreHVKgbi9PHq3HZ8DUKKJHQu0IBAfXtkA&usqp=CAU"

        open = urlopen(url)

        data = open.read()

        open.close()

        image = ImageTk.PhotoImage(data=data)

        self.logo = Label(self.container, image=image, bg='#0072AF')
        self.logo.image = image

        self.logo.place(relx=.43, rely=.25, relheight=.2, relwidth=.15)

    def buttons(self):
        
        btn_width = .25
        btn_height = .15
        btn_pos_y = .6

        # Primeira Máquina
        self.btn_maq_1 = Button(
            self.container, 
            command=lambda: self.machine_info_page(1),
            text="Caixa 1", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btn_maq_1.place(relx=.12, rely=btn_pos_y, relwidth=btn_width, relheight=btn_height)
    
        # Segunda Máquina
        self.btn_maq_2 = Button(
            self.container, 
            command=lambda: self.machine_info_page(2),
            text="Caixa 2", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btn_maq_2.place(relx=.375, rely=btn_pos_y, relwidth=btn_width, relheight=btn_height)

        # Terceira Máquina
        self.btn_maq_3 = Button(
            self.container,
            command=lambda: self.machine_info_page(3), 
            text="Caixa 3", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btn_maq_3.place(relx=.63, rely=btn_pos_y, relwidth=btn_width, relheight=btn_height)

        # Sair
        self.btn_finalizar = Button(
            self.container,
            command=self.finalizar, 
            text="Finalizar", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btn_finalizar.place(relx=.375, rely=.78, relwidth=btn_width, relheight=btn_height)
    
    def finalizar(self):
        self.root.quit()