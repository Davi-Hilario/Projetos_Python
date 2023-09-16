# Importando Bibliotecas
from enlist import Enlist

from tkinter import *
from tkinter import ttk

from PIL import ImageTk
from urllib.request import urlopen

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#Iniciando aplicação
root = Tk()

class App(Enlist):

    def __init__(self):
        self.root = root
        self.config()
        self.frame()
        self.label()
        self.logo()
        self.buttons()
        self.root.mainloop()

    # Configurações da tela
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

    def createList(self, index):

        self.container.destroy()
        self.root.geometry("1000x700")

        self.frame()

        self.tituloCaixa = Label(
            self.container, 
            text=f"Caixa Eletrônico {index}", 
            font='Arial 18 bold',
            bg='#0072AF',
            fg='white'
            )
        self.tituloCaixa.place(relx=0, rely=.005, relwidth=1, relheight=.1)

        self.lista = ttk.Treeview(
            self.container,
            height=3,
            columns=('col1', 'col2', 'col3', 'col4')
        )
        
        self.lista.heading('#0', text='')
        self.lista.column("#0", width=1)

        self.lista.heading('#1', text="CPU") 
        self.lista.column("#1", width=50)

        self.lista.heading('#2', text="MEMORIA") 
        self.lista.column("#2", width=50)

        self.lista.heading('#3', text="DISCO") 
        self.lista.column("#3", width=50)

        self.lista.heading('#4', text='HORÁRIO')  
        self.lista.column("#4", width=120)

        self.lista.place(relx=.01, rely=.1, relwidth=.98, relheight=.35)

        self.scroll = Scrollbar(self.container, orient='vertical')
        self.lista.configure(yscroll=self.scroll.set)
        self.scroll.place(relx=.96, rely=.1, relwidth=.03, relheight=.35)

        self.btnVoltar = Button(
            self.container, 
            command=App,
            text="Voltar", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
            
        self.btnVoltar.place(relx=.05, rely=.95, relwidth=.44, relheight=.05)

        self.graphs()

        self.get_maq(index)

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

        # Monitorar Todos os Dados
        # self.btnReadAll = Button(
        #     self.container, 
        #     command=lambda: self.createAllDataList(),
        #     text="Ler Todos os Dados", 
        #     font='Arial 10 bold',
        #     bg='#00809A',
        #     fg='white'
        # )
            
        # self.btnReadAll.place(relx=btnPosX, rely=.5, relwidth=btn_width, relheight=btn_height)
        
        # Primeira Máquina
        self.btn_maq_1 = Button(
            self.container, 
            command=lambda: self.createList(1),
            text="Caixa 1", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btn_maq_1.place(relx=.12, rely=btn_pos_y, relwidth=btn_width, relheight=btn_height)
    
        # Segunda Máquina
        self.btn_maq_2 = Button(
            self.container, 
            command=lambda: self.createList(2),
            text="Caixa 2", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btn_maq_2.place(relx=.375, rely=btn_pos_y, relwidth=btn_width, relheight=btn_height)

        # Terceira Máquina
        self.btn_maq_3 = Button(
            self.container,
            command=lambda: self.createList(3), 
            text="Caixa 3", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btn_maq_3.place(relx=.63, rely=btn_pos_y, relwidth=btn_width, relheight=btn_height)
        