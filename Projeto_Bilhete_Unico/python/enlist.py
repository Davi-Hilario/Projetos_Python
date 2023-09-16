from maquina import Maquina
import psutil as ps

from tkinter import *

from datetime import datetime

from math import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Enlist():

    def __init__(self):
        self.maq_1
        self.maq_2
        self.maq_3
        self.index

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

        horario = datetime.now()
        self.index = index

        if(self.index == 1):
            self.insertData(cpu1, memo1, disco1, horario)
        elif(self.index == 2):
            self.insertData(cpu2, memo2, disco2, horario)
        elif(self.index == 3):
            self.insertData(cpu3, memo3, disco3, horario)
        
    def insertData(self, cpu, memoria, disco, tempo):

        self.values_cpu.append(cpu)
        self.values_memo.append(memoria)
        self.values_disk.append(disco)
        self.values_tempo.append(tempo)

        self.graphs()
    
        self.lista.insert("",END, values=(f"{cpu}%", f"{memoria}%", f"{disco}%", tempo))

        self.plot(self.values_cpu, self.values_memo, self.values_disk, self.values_tempo) 

        self.root.after(1000, lambda: self.get_maq(self.index))
    
    def graphs(self):

        graphs_pos_y = .5
        graphs_width = .31
        graphs_height = .35

        self.fig_cpu, self.ax_cpu = plt.subplots()
        self.fig_memo, self.ax_memo = plt.subplots()
        self.fig_disk, self.ax_disk = plt.subplots()
        
        self.titulo_cpu = Label(
            self.container, 
            text="CPU", 
            font='Arial 12 bold',
            bg='#0072AF',
            fg='white'
            )
        self.titulo_cpu.place(relx=.07, rely=.45, relwidth=.2, relheight=.05)
        self.graph_cpu = FigureCanvasTkAgg(self.fig_cpu, master=self.container)
        self.graph_cpu.get_tk_widget().place(relx=.01, rely=graphs_pos_y, relheight=graphs_height, relwidth=graphs_width)

        self.titulo_memo = Label(
            self.container, 
            text="MEMORIA", 
            font='Arial 12 bold',
            bg='#0072AF',
            fg='white'
            )
        self.titulo_memo.place(relx=.4, rely=.45, relwidth=.2, relheight=.05)
        self.graph_memo = FigureCanvasTkAgg(self.fig_memo, master=self.container)
        self.graph_memo.get_tk_widget().place(relx=.345, rely=graphs_pos_y, relheight=graphs_height, relwidth=graphs_width)

        self.titulo_disco = Label(
            self.container, 
            text="DISCO", 
            font='Arial 12 bold',
            bg='#0072AF',
            fg='white'
            )
        self.titulo_disco.place(relx=.75, rely=.45, relwidth=.2, relheight=.05)
        self.graph_disk = FigureCanvasTkAgg(self.fig_disk, master=self.container)
        self.graph_disk.get_tk_widget().place(relx=.68, rely=graphs_pos_y, relheight=graphs_height, relwidth=graphs_width)

    def plot(self, cpu, memoria, disco, tempo):
        self.ax_cpu.clear()
        self.ax_cpu.scatter(tempo, cpu)
        self.graph_cpu.draw()

        self.ax_memo.clear()
        self.ax_memo.scatter(tempo, memoria)
        self.graph_memo.draw()

        self.ax_disk.clear()
        self.ax_disk.scatter(tempo, disco)
        self.graph_disk.draw()
