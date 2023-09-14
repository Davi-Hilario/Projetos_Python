from data import Functions
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from urllib.request import urlopen

root = Tk() # criando a janela

class App(Functions):

    def __init__(self):
        self.root = root
        self.config()
        self.frame()
        self.label()
        self.logo()
        self.buttons()
        self.root.mainloop() # loop para que a janela continue aberta após execução do código

    # Configurações da tela
    def config(self):
        self.root.title("Análise de Hardware") # titulo da tela   
        self.root.configure(background='#004480') # cor de fundo
        self.root.geometry('700x500') # tamanho da tela (horizontal x vertical)
        self.root.resizable(True, True) # definindo se a tela é ajustável nos eixos x e y
        self.root.maxsize(width=900, height=700) # tamanho máximo que a tela pode chegar
        self.root.minsize(width=500, height=300) # tamanho minimo que a tela pode chegar

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

    def createList(self, component):
        
        col1 = col2 = col3 = ''
        labelBotao = ''

        if(component == 'CPU'):
            col1 = 'CPU 1'
            col2 = 'CPU 2'
            col3 = 'CPU 3'
            labelBotao = 'Analisar CPU'
            comando = self.getCpu

        elif(component == 'MEMO'):
            col1 = 'MEMORIA 1'
            col2 = 'MEMORIA 2'
            col3 = 'MEMORIA 3'
            labelBotao = 'Analisar Memória'
            comando = self.getMemo

        elif(component == 'DISCO'):
            col1 = 'DISCO 1'
            col2 = 'DISCO 2'
            col3 = 'DISCO 3'
            labelBotao = 'Analisar Disco'
            comando = self.getDisk

        self.container.destroy()

        self.frame()

        self.lista = ttk.Treeview(
            self.container,
            height=3,
            columns=('col1', 'col2', 'col3', 'col4')
        )
        
        self.lista.heading('#0', text='')
        self.lista.column("#0", width=1)

        self.lista.heading('#1', text=col1) 
        self.lista.column("#1", width=50)

        self.lista.heading('#2', text=col2) 
        self.lista.column("#2", width=50)

        self.lista.heading('#3', text=col3) 
        self.lista.column("#3", width=50)

        self.lista.heading('#4', text='HORÁRIO')  
        self.lista.column("#4", width=120)

        self.lista.place(relx=0.02, rely=.05, relwidth=.9, relheight=.7)

        self.scroll = Scrollbar(self.container, orient='vertical')
        self.lista.configure(yscroll=self.scroll.set)
        self.scroll.place(relx=0.92, rely=0.05, relwidth=.05, relheight=.7)

        self.btnVoltar = Button(
            self.container, 
            command=App,
            text="Voltar", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
            
        self.btnVoltar.place(relx=.05, rely=.8, relwidth=.44, relheight=.1)

        self.btnAnalisar = Button(
            self.container, 
            command=comando,
            text=labelBotao, 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
            
        self.btnAnalisar.place(relx=.5, rely=.8, relwidth=.44, relheight=.1)

    def logo(self):
        
        url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5SreHVKgbi9PHq3HZ8DUKKJHQu0IBAfXtkA&usqp=CAU"

        open = urlopen(url)

        data = open.read()

        open.close()

        image = ImageTk.PhotoImage(data=data)

        self.logo = Label(self.container, image=image, bg='#0072AF')
        self.logo.image = image

        self.logo.place(relx=.44, rely=.25, relheight=.2, relwidth=.15)

    def buttons(self):

        btnWidth = .4
        btnHeight = .1
        btnPosX = .3

        # Monitorar Todos os Dados
        self.btnGraph = Button(
            self.container, 
            command=lambda: self.createList('DISCO'),
            text="Comparação de Performance", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
            
        self.btnGraph.place(relx=btnPosX, rely=.5, relwidth=btnWidth, relheight=btnHeight)
        
        # Monitoriar CPU
        self.btnCpu = Button(
            self.container, 
            command=lambda: self.createList('CPU'),
            text="Monitorar CPU", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btnCpu.place(relx=btnPosX, rely=.61, relwidth=btnWidth, relheight=btnHeight)
    
        # Monitorar Memória
        self.btnMemo = Button(
            self.container, 
            command=lambda: self.createList('MEMO'),
            text="Monitorar Memória", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btnMemo.place(relx=btnPosX, rely=.72, relwidth=btnWidth, relheight=btnHeight)

        # Monitorar Disco 
        self.btnDisk = Button(
            self.container,
            command=lambda: self.createList('DISCO'), 
            text="Monitorar Disco", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btnDisk.place(relx=btnPosX, rely=.83, relwidth=btnWidth, relheight=btnHeight)
