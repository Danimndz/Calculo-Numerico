from tkinter import *
from tkinter import ttk,font,messagebox
import MainMenu as Main
from Build_Polys.Dif_div import DifDivididas
from Build_Polys.lagrangePoly import Lagrange
from Build_Polys.Hermite import Hermite

class PolyMenu:
    def __init__(self):
        self.polymenu = Tk()
        self.polymenu.geometry('300x300')
        self.polymenu.title('Poly Menu')
        self.polymenu.resizable(width=False, height=False)
        self.difDiv_bttn = ttk.Button(self.polymenu,text='Divided Differences',command=self.met_difdiv)
        self.difDiv_bttn.pack()
        self.lagrange_bttn = ttk.Button(self.polymenu,text='Lagrange Polynomial',command=self.met_lagrange)
        self.lagrange_bttn.pack()
        self.hermite_bttn = ttk.Button(self.polymenu,text='Hermite method',command=self.met_hermite)
        self.hermite_bttn.pack()
        self.back_mainM = ttk.Button(self.polymenu,text="Return Main Menu",command=self.back_main)
        self.back_mainM.pack(side=RIGHT) 
        self.close = ttk.Button(self.polymenu,text="Exit",command=self.polymenu.destroy)
        self.close.pack(side=LEFT)


    def met_difdiv(self):
        self.polymenu.destroy()
        DifDivididas()
    
    def met_lagrange(self):
        self.polymenu.destroy()
        Lagrange()

    def met_hermite(self):
        self.polymenu.destroy()
        Hermite()

    def back_main(self):
        self.polymenu.destroy()
        Main.MainMenu()



