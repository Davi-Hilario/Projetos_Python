from tkinter import *
from connection import Connection

root = Tk()

class App():
    
    def __init__(self):
        self.root = root
        self.screen()
        self.widgets()
        self.root.mainloop()
    
    def screen(self):
        self.root.title("teste")
        self.root.configure(bg='#0097c9', highlightcolor='#03c0ff', highlightthickness=4)
        self.root.geometry('400x450')
        self.root.resizable(False, False)
    
    def widgets(self):

        labelFg = 'white'
        bgColor = inputFg = '#0097c9'

        # ----------- Titulo ----------- #
        self.title = Label(
            self.root,
            text="Login no Sistema", 
            font="Helvetica 30 bold",
            fg='midnightblue',
            bg='#0097c9'
        )
        self.title.place(relx=.075, rely=.1, relheight=.1, relwidth=.85)

        # ----------- Login ----------- #

        self.labelLogin = Label(
            self.root,
            text="Login",
            font="Helvetica 15 bold",
            fg=labelFg,
            bg=bgColor
        )
        self.labelLogin.place(relx=.03, rely=.3,relheight=.05,relwidth=.4)

        self.inputLogin = Entry(self.root, fg=inputFg, justify='center')
        self.inputLogin.place(relx=.15, rely=.38,relheight=.12,relwidth=.7)

        # ----------- Senha ----------- #

        self.labelLogin = Label(
            self.root,
            text="Senha",
            font="Helvetica 15 bold",
            fg=labelFg,
            bg=bgColor
        )
        self.labelLogin.place(relx=.03, rely=.53,relheight=.05,relwidth=.4)

        self.inputLogin = Entry(self.root, fg=inputFg, justify='center')
        self.inputLogin.place(relx=.15, rely=.6,relheight=.12,relwidth=.7)

        # ----------- Botão Entrar ----------- #

        self.btnConfirm = Button(
            self.root, 
            bg='royalblue', 
            fg='white', 
            text='Entrar',
            font='Helvetica 20 bold',
            border=5
        )
        self.btnConfirm.place(relx=.2, rely=.8,relheight=.135,relwidth=.6)