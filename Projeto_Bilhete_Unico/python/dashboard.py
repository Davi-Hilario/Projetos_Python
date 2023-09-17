from maquina import Maquina
import psutil as ps

from tkinter import *

from datetime import datetime

from math import *
from random import random

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from tkinter import ttk

class Dashboard():

    def __init__(self):
        self.maq_1
        self.maq_2
        self.maq_3
        self.index
        self.cpu_list
        self.memo_list
        self.disk_list
        self.time_list

    def create_graphs(self):
        
        self.cpu_list = []
        self.memo_list = []
        self.disk_list = []
        self.time_list = []

        graphs_pos_y = .5
        graphs_width = .31
        graphs_height = .35

        self.fig_cpu, self.ax_cpu = plt.subplots()
        self.fig_memo, self.ax_memo = plt.subplots()
        self.fig_disk, self.ax_disk = plt.subplots()
        
        self.titulo_cpu = Label(self.container, text="CPU", font='Arial 12 bold',bg='#0072AF',fg='white')
        self.titulo_cpu.place(relx=.07, rely=.45, relwidth=.2, relheight=.05)
        self.graph_cpu = FigureCanvasTkAgg(self.fig_cpu, master=self.container)
        self.graph_cpu.get_tk_widget().place(relx=.01, rely=graphs_pos_y, relheight=graphs_height, relwidth=graphs_width)

        self.titulo_memo = Label(self.container, text="MEMORIA", font='Arial 12 bold',bg='#0072AF',fg='white')
        self.titulo_memo.place(relx=.4, rely=.45, relwidth=.2, relheight=.05)
        self.graph_memo = FigureCanvasTkAgg(self.fig_memo, master=self.container)
        self.graph_memo.get_tk_widget().place(relx=.345, rely=graphs_pos_y, relheight=graphs_height, relwidth=graphs_width)

        self.titulo_disco = Label(self.container, text="DISCO", font='Arial 12 bold',bg='#0072AF',fg='white')
        self.titulo_disco.place(relx=.75, rely=.45, relwidth=.2, relheight=.05)
        self.graph_disk = FigureCanvasTkAgg(self.fig_disk, master=self.container)
        self.graph_disk.get_tk_widget().place(relx=.68, rely=graphs_pos_y, relheight=graphs_height, relwidth=graphs_width)

    def create_list(self):

        self.lista = ttk.Treeview(self.container,height=3,columns=('col1', 'col2', 'col3', 'col4'))
        
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

    def machine_info_page(self, index):
        
        self.container.destroy()
        self.root.geometry("1000x700")

        self.frame()

        self.tituloCaixa = Label(self.container, 
            text=f"Caixa Eletrônico {index}", font='Arial 18 bold', bg='#0072AF', fg='white')
        self.tituloCaixa.place(relx=0, rely=.005, relwidth=1, relheight=.1)

        self.create_list()
        self.create_graphs()

        self.btn_voltar = Button(
            self.container, 
            text="Voltar", 
            font='Arial 10 bold',
            bg='#00809A',
            fg='white'
        )
            
        self.btn_voltar.place(relx=.05, rely=.95, relwidth=.44, relheight=.05)

        self.get_maq(index)

    def get_maq(self, index):
        
        self.maq_1 = Maquina()
        self.maq_2 = Maquina()
        self.maq_3 = Maquina()

        # Pegando CPU --------------------
        self.maq_1.set_cpu(round(ps.cpu_percent(),1))
        cpu1 = self.maq_1.get_cpu()

        self.maq_3.set_cpu(round(abs(cpu1 - (ceil(sqrt(cpu1))) - (floor(cpu1 * 0.05))),1))
        cpu3 = self.maq_3.get_cpu()
        
        self.maq_2.set_cpu(round(cpu1 + (0.1 * cpu1) - (0.05 * cpu3),1))
        cpu2 = self.maq_2.get_cpu()

        # Pegando Memoria --------------------
        self.maq_1.set_memo(round(ps.virtual_memory().percent,1))
        memo1 = self.maq_1.get_memo()

        self.maq_3.set_memo(round(memo1 - (floor(tan(0.5 * tan(memo1)))) - (ceil(sin(sqrt(memo1)))),1))
        memo3 = self.maq_3.get_memo()

        self.maq_2.set_memo(round(memo1 + (0.15 * memo1) + (0.05 * memo3),1))
        memo2 = self.maq_2.get_memo()
        
        # Pegando Disco ----------------------
        self.maq_1.set_disk(round(ps.disk_usage('/').percent,1))
        disco1 = self.maq_1.get_disk()
        
        self.maq_2.set_disk(round(round(disco1 - (0.05 * disco1),1)))
        disco2 = self.maq_2.get_disk()

        self.maq_3.set_disk(round((disco2 * 3),1))
        disco3 = self.maq_3.get_disk()

        horario = datetime.now().time().strftime("%H:%M:%S")
        self.index = index

        self.time_list.append(horario)

        if(self.index == 1):

            self.cpu_list.append(cpu1)
            self.memo_list.append(memo1)
            self.disk_list.append(disco1)

            self.lista.insert("",END, values=(f"{cpu1}%", f"{memo1}%", f"{disco1}%", horario))

        elif(self.index == 2):

            self.cpu_list.append(cpu2)
            self.memo_list.append(memo2)
            self.disk_list.append(disco2)

            self.lista.insert("",END, values=(f"{cpu2}%", f"{memo2}%", f"{disco2}%", horario))

        elif(self.index == 3):

            self.cpu_list.append(cpu3)
            self.memo_list.append(memo3)
            self.disk_list.append(disco3)

            self.lista.insert("",END, values=(f"{cpu3}%", f"{memo3}%", f"{disco3}%", horario))
        
        self.plot_graphs_data()
                
        self.root.after(1000, lambda: self.get_maq(self.index))

    def plot_graphs_data(self):

        self.ax_cpu.clear()
        self.ax_memo.clear()
        self.ax_disk.clear()

        if(len(self.time_list) > 3):
            self.time_list.pop(0)
            self.cpu_list.pop(0)
            self.memo_list.pop(0)
            self.disk_list.pop(0)

        self.ax_cpu.plot(self.time_list,self.cpu_list)
        self.graph_cpu.draw()

        self.ax_memo.plot(self.time_list,self.memo_list)
        self.graph_memo.draw()

        self.ax_disk.plot(self.time_list,self.disk_list)
        self.graph_disk.draw()
