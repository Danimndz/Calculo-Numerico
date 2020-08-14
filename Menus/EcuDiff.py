from tkinter import *
from tkinter import ttk,font,messagebox
import MainMenu as Main
from Ecuaciones_Diferenciales.TaylorOrdenN import TaylorN
from Ecuaciones_Diferenciales.EulerRK import eulerRk
from Ecuaciones_Diferenciales.HeunRk import Heun
from Ecuaciones_Diferenciales.Pmedio import Pmedio
from Ecuaciones_Diferenciales.orden4rk import Orden4


class EqDif:
    def __init__(self):
        self.eqdif = Tk()
        self.eqdif.geometry('300x300')
        self.eqdif.title('Differential equations Menu')
        self.eqdif.resizable(width=False, height=False)
        self.taylorOn_bttn = ttk.Button(self.eqdif,text='taylor Orden N',command=self.met_tayOn)
        self.taylorOn_bttn.pack()
        self.euler_btn = ttk.Button(self.eqdif,text='Euler',command=self.met_euler)
        self.euler_btn.pack()
        self.heun_btn = ttk.Button(self.eqdif,text='Heun method',command=self.met_heun)
        self.heun_btn.pack()
        self.pmedio_btn = ttk.Button(self.eqdif,text='Pmedio method',command=self.pmedio_)
        self.pmedio_btn.pack()
        self.O4_btn = ttk.Button(self.eqdif,text='Runke 4th Order',command=self.o4_)
        self.O4_btn.pack()
        self.back_mainM = ttk.Button(self.eqdif,text="Return Main Menu",command=self.back_main)
        self.back_mainM.pack(side=RIGHT) 
        self.close = ttk.Button(self.eqdif,text="Exit",command=self.eqdif.destroy)
        self.close.pack(side=LEFT)


    def met_tayOn(self):
        self.eqdif.destroy()
        TaylorN()


    
    def met_euler(self):
        self.eqdif.destroy()
        eulerRk()


    def met_heun(self):
        self.eqdif.destroy()
        Heun()
    
    def pmedio_(self):
        self.eqdif.destroy()
        Pmedio()
    
    def o4_(self):
        self.eqdif.destroy()
        Orden4()

    


    def back_main(self):
        self.eqdif.destroy()
        Main.MainMenu()



