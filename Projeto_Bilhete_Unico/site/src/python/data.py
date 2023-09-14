import psutil as ps
from tkinter import *
from math import *
import connection as con

from datetime import datetime

class Functions():

    def getCpu(self):

        cpu1 = round(ps.cpu_percent(),1)
        cpu3 = round(abs(cpu1 - (ceil(sqrt(cpu1))) - (floor(cpu1 * 0.05))),1)
        cpu2 = round(cpu1 + (0.1 * cpu1) - (0.05 * cpu3),1)

        horario = datetime.now()

        self.lista.insert("",END, values=(cpu1, cpu2, cpu3, horario))

        self.root.after(1000, self.getCpu)

    def getDisk(self):
        
        disco1 = disco2 = round(ps.disk_usage('/').percent,1)
        disco2 = round(disco2 - (0.05 * disco1),1)
        disco3 = round((disco2 * 3),1)

        horario = datetime.now()
        
        self.lista.insert("",END, values=(disco1, disco2, disco3, horario))

        self.root.after(1000, self.getDisk)

    def getMemo(self):
        
        memo1 = round(ps.virtual_memory().percent,1)
        memo3 = round(memo1 - (floor(tan(0.5 * tan(memo1)))) - (ceil(sin(sqrt(memo1)))),1)
        memo2 = round(memo1 + (0.15 * memo1) + (0.05 * memo3),1)

        horario = datetime.now()
        
        self.lista.insert("",END, values=(memo1, memo2, memo3, horario))

        self.root.after(1000, self.getMemo)

