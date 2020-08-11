from tkinter import *
from tkinter import ttk,font
import Menus.RootMenu as RootMenu
import Menus.PolyMenu as PolyMenu
import Menus.DerivadaIntegralMenu  as DerivadaIntegralMenu
import Menus.EcuDiff as EqDif
class MainMenu:
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.geometry('300x300')
        self.mainWindow.title("Main Menu")
        self.introLabel = ttk.Label(self.mainWindow,text="  Welcome to UpNums \n where you can use varius numeric methods \n simply click on the method you want to use", justify=CENTER)
        self.introLabel.pack(side =TOP)
        self.mainWindow.resizable(width=False, height=False)
        self.btn = ttk.Button(self.mainWindow,text="Finding Roots...",command=self.Calcular_raices)
        self.btn.pack()
        self.polybtn = ttk.Button(self.mainWindow,text='Build Polys',command=self.Polynoms)
        self.polybtn.pack()
        self.IntDeriv = ttk.Button(self.mainWindow,text='Integrate and Derivate',command=self.IntyDer)
        self.IntDeriv.pack()
        self.DifEq = ttk.Button(self.mainWindow,text='Differential equations',command=self.EcDif)
        self.DifEq.pack()
        self.close = ttk.Button(self.mainWindow,text="Exit",command=self.mainWindow.destroy)
        self.close.pack(side=BOTTOM)
        self.mainWindow.mainloop()


    def Calcular_raices(self):
        self.newWindow = Toplevel(self.mainWindow)
        self.newWindow.withdraw()
        self.mainWindow.destroy()
        RootMenu.RootMenu()
        
    def Polynoms(self):
        self.newWindow = Toplevel(self.mainWindow)
        self.newWindow.withdraw()
        self.mainWindow.destroy()
        PolyMenu.PolyMenu()
        
    def IntyDer(self):
        self.newWindow = Toplevel(self.mainWindow)
        self.newWindow.withdraw()
        self.mainWindow.destroy()
        DerivadaIntegralMenu.DerEintMenu()
    
    def EcDif(self):
        self.newWindow = Toplevel(self.mainWindow)
        self.newWindow.withdraw()
        EqDif.EqDif()
        self.mainWindow.destroy()
    

        

        
