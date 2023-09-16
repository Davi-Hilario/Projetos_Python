from maquina import Maquina
import psutil as ps
from tkinter import END
from datetime import datetime
from time import sleep
from math import *

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

        self.lista.insert("",END, values=(f"{cpu}%", f"{memoria}%", f"{disco}%", tempo))
        self.root.after(1000, lambda: self.get_maq(self.index))

        


