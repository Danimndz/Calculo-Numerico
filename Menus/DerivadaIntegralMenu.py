from tkinter import *
from tkinter import ttk,font,messagebox
import MainMenu as Main
from Integrar_Derivar.Dif_Numerica import DifNumerica
from Integrar_Derivar.Integracion_Puntos import IngeracionPuntos
from Integrar_Derivar.Abierta_compuesta import AbiertaCompuesta
from Integrar_Derivar.TrapecioMetodo import Trapecio
from Integrar_Derivar.SimpsonMethod import Simpson

class DerEintMenu:
    def __init__(self):
        self.polymenu = Tk()
        self.polymenu.geometry('300x300')
        self.polymenu.title('Poly Menu')
        self.polymenu.resizable(width=False, height=False)
        self.difNum_bttn = ttk.Button(self.polymenu,text='Numerical differentiation',command=self.met_difNum)
        self.difNum_bttn.pack()
        self.integracionPuntos_bttn = ttk.Button(self.polymenu,text='Integration by Given Points',command=self.met_intPuntos)
        self.integracionPuntos_bttn.pack()
        self.AbiertaCompuesta_bttn = ttk.Button(self.polymenu,text='Open integration',command=self.met_Abierta)
        self.AbiertaCompuesta_bttn.pack()
        self.Simpson_bttn = ttk.Button(self.polymenu,text='Simpson Method',command=self.met_Simpson)
        self.Simpson_bttn.pack()
        self.Trapecio_bttn = ttk.Button(self.polymenu,text='Trapeze Method',command=self.met_Trapecio)
        self.Trapecio_bttn.pack()
        self.back_mainM = ttk.Button(self.polymenu,text="Return Main Menu",command=self.back_main)
        self.back_mainM.pack(side=RIGHT) 
        self.close = ttk.Button(self.polymenu,text="Exit",command=self.polymenu.destroy)
        self.close.pack(side=LEFT)


    def met_difNum(self):
        self.polymenu.destroy()
        DifNumerica()

    def met_intPuntos(self):
        self.polymenu.destroy()
        IngeracionPuntos()

    def met_Abierta(self):
        self.polymenu.destroy()
        AbiertaCompuesta()

    def met_Simpson(self):
        self.polymenu.destroy()
        Simpson()

    def met_Trapecio(self):
        self.polymenu.destroy()
        Trapecio()

    def back_main(self):
        self.polymenu.destroy()
        Main.MainMenu()
        

        
