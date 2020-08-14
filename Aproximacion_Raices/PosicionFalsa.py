from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.RootMenu as root
class FalsePosition: 
    def __init__(self):
        self.FalsePosition_ = Tk()
        self.FalsePosition_.geometry('500x690')
        self.FalsePosition_.title("FalsePosition Method")
        self.FalsePosition_.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')
        self.fxtx = ttk.Label(self.FalsePosition_,text="f(x): ",font=fuente)
        self.pnt0txt =ttk.Label(self.FalsePosition_,text='P0: ',font=fuente)
        self.pnt1txt =ttk.Label(self.FalsePosition_,text='P1: ',font=fuente)
        self.tolerance =ttk.Label(self.FalsePosition_,text='tolerance: ',font=fuente)
        self.numIttxt =ttk.Label(self.FalsePosition_,text='Number of iterations: ',font=fuente)
        self.fx=StringVar()
        self.p0 = StringVar()
        self.p1 = StringVar()
        self.nIter = StringVar()
        self.presission = StringVar()
        self.fxBox = ttk.Entry(self.FalsePosition_,textvariable=self.fx,width=30)
        self.p0Box = ttk.Entry(self.FalsePosition_,textvariable=self.p0,width=30)
        self.p1Box = ttk.Entry(self.FalsePosition_,textvariable=self.p1,width=30)
        self.tolBox = ttk.Entry(self.FalsePosition_,textvariable=self.presission,width=30)
        self.ItBox = ttk.Entry(self.FalsePosition_,textvariable=self.nIter,width=30)
        self.tabinfo = Text(self.FalsePosition_, width=37, height=25)
        self.help_btn = ttk.Button(self.FalsePosition_,text="Help",command=self.help_ )
        self.cal_btn = ttk.Button(self.FalsePosition_,text="Calculate",command=self.poscionFalsa_ )
        self.back_mainM = ttk.Button(self.FalsePosition_,text="Return Main Menu",command=self.back_main)
        self.fxtx.pack()
        self.fxBox.pack()
        self.pnt0txt.pack()
        self.p0Box.pack()
        self.pnt1txt.pack()
        self.p1Box.pack()
        self.tolerance.pack()
        self.tolBox.pack()
        self.numIttxt.pack()
        self.ItBox.pack()      
        self.tabinfo.pack() 
        self.cal_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.FalsePosition_.mainloop()

    def help_(self):
        self.newWindow = Toplevel(self.FalsePosition_)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def poscionFalsa_(self):
        try:
            tab = PrettyTable()
            self.tabinfo.delete("1.0", END)
            tab.field_names=(["iteraciones", "p"])
            def f(x):
                return eval(self.fxBox.get())
            p=0
            def PosicionFalsa(p):
                i=0
                tol = eval(self.tolBox.get())
                p0 = eval(self.p0Box.get())
                p1 = eval(self.p1Box.get())
                q0 = f(p0)
                q1 = f(p1)
                numIt = int(self.ItBox.get())
                q0 =f(p0)
                q1 = f(p1)
                while i<=numIt:
                    p = p1-q1*(p1-p0)/(q1-q0)
                    if abs(p-p1)<tol:
                        return p
                    i+=1
                    q = f(p)
                    if q*q1<0:
                        p0=p1
                        q0=q1
                    p1=p
                    q1=q
                    tab.add_row([i,p])
                print('Error')
            if f(float(self.p1Box.get())) >0 and f(float(self.p0Box.get())) < 0 or f(float(self.p1Box.get())) <0 and f(float(self.p0Box.get())) > 0:
                PosicionFalsa(p)
                txt = "\nRaiz: "+str(PosicionFalsa(p))
                self.tabinfo.insert('1.0',txt)
                self.tabinfo.insert('1.0',tab)
            else: self.tabinfo.insert('1.0','Intervalo incorrecto,\nno hay cambio de signo\n Ingrese otro porfavor')
        except SyntaxError:
            errorMessage = "Wrong or non-existence value, please try again"
            self.tabinfo.insert('1.0',errorMessage)
        except ValueError:
            errorMessage = "Wrong or non-existence value, please try again"
            self.tabinfo.insert('1.0',errorMessage)
        except NameError:
            errorMessage = "Value not define, please try again"
            self.tabinfo.insert('1.0',errorMessage)
        except ZeroDivisionError:
            errorMessage = "Zero division, pleas try again"
            self.tabinfo.insert('1.0',errorMessage)


    def back_main(self):
        self.FalsePosition_.destroy()
        root.RootMenu()