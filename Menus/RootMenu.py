from tkinter import *
from tkinter import ttk,font
import MainMenu as Main
from Aproximacion_Raices.biseccion import Bisection
from Aproximacion_Raices.FixedPoint import FixedPoint
from Aproximacion_Raices.newtonRaphs import NewtonRaphson
from Aproximacion_Raices.secante import Secant
from Aproximacion_Raices.PosicionFalsa import FalsePosition
from Aproximacion_Raices.HornerMethod import HornerMethod
from Aproximacion_Raices.MullerMethod import Muller
class RootMenu:
    def __init__(self):
        self.rootMenu = Tk()
        self.rootMenu.geometry('300x300')
        self.rootMenu.title("Root Menu")
        self.rootMenu.resizable(width=False, height=False)
        self.bi_bttn = ttk.Button(self.rootMenu,text="Bisection Method",command=self.met_bi)
        self.bi_bttn.pack()
        self.pnto_bttn = ttk.Button(self.rootMenu,text="Fixed Point Method",command=self.met_pntf)
        self.pnto_bttn.pack() 
        self.nwR_bttn = ttk.Button(self.rootMenu,text="Newton Raphson Method",command=self.met_nwR)
        self.nwR_bttn.pack()
        self.sec_bttn = ttk.Button(self.rootMenu,text="Secant Method",command=self.met_sec)
        self.sec_bttn.pack() 
        self.poF_bttn = ttk.Button(self.rootMenu,text="False Position Method",command=self.met_poF)
        self.poF_bttn.pack() 
        self.horner_bttn = ttk.Button(self.rootMenu,text="Horner Method",command =self.met_horner)
        self.horner_bttn.pack()
        self.muller_bttn = ttk.Button(self.rootMenu,text="Müller Method",command=self.met_mull)
        self.muller_bttn.pack()
        self.back_mainM = ttk.Button(self.rootMenu,text="Return Main Menu",command=self.back_main)
        self.back_mainM.pack(side=RIGHT) 
        self.close = ttk.Button(self.rootMenu,text="Exit",command=self.rootMenu.destroy)
        self.close.pack(side=LEFT)

    def met_bi(self):
        self.rootMenu.destroy()
        Bisection()

    def met_pntf(self):
        self.rootMenu.destroy()
        FixedPoint()

    def met_nwR(self):
        self.rootMenu.destroy()
        NewtonRaphson()
        
    def met_sec(self):
        self.rootMenu.destroy()
        Secant()

    def met_poF(self):
        self.rootMenu.destroy()
        FalsePosition()

    def met_horner(self):
        self.rootMenu.destroy()
        HornerMethod()
        
    def met_mull(self):
        self.rootMenu.destroy()
        Muller()
    
    def back_main(self):
        self.rootMenu.destroy()
        Main.MainMenu()