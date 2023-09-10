from tkinter import * # importando a biblioteca do tkinter
from tkinter import ttk

root = Tk() # criando a janela

class App():

    def __init__(self):
        self.root = root
        self.config()
        self.frame()
        self.label()
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

    def createList(self):

        self.container.destroy()

        self.frame()

        self.lista = ttk.Treeview(
            self.container,
            height=3,
            columns=('col1', 'col2', 'col3', 'col4')
        )
        
        self.lista.heading('#0', text='')
        self.lista.column("#0", width=1)

        self.lista.heading('#1', text='CPU 1') 
        self.lista.column("#1", width=50)

        self.lista.heading('#2', text='CPU 2') 
        self.lista.column("#2", width=50)

        self.lista.heading('#3', text='CPU 3') 
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
            
        self.btnVoltar.place(relx=.3, rely=.8, relwidth=.4, relheight=.1)

        self.ler

    def buttons(self):

        btnWidth = .4
        btnHeight = .1
        btnPosX = .3

        # Monitorar Todos os Dados
        self.btnGraph = Button(
            self.container, 
            command=self.createList,
            text="Comparação de Performance", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
            
        self.btnGraph.place(relx=btnPosX, rely=.3, relwidth=btnWidth, relheight=btnHeight)
        
        # Monitoriar CPU
        self.btnCpu = Button(
            self.container, 
            text="Monitorar CPU", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btnCpu.place(relx=btnPosX, rely=.41, relwidth=btnWidth, relheight=btnHeight)
    
        # Monitorar Memória
        self.btnMemo = Button(
            self.container, 
            text="Monitorar Memória", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btnMemo.place(relx=btnPosX, rely=.52, relwidth=btnWidth, relheight=btnHeight)

        # Monitorar Disco 
        self.btnDisk = Button(
            self.container, 
            text="Monitorar Disco", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
        self.btnDisk.place(relx=btnPosX, rely=.63, relwidth=btnWidth, relheight=btnHeight)

App()

