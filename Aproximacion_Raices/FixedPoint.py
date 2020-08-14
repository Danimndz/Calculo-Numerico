from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.RootMenu as root
class FixedPoint:
    def __init__(self):
        self.fixedPoint = Tk()
        self.fixedPoint.geometry('500x630')
        self.fixedPoint.title("Fixed Point Method")
        self.fixedPoint.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')
        self.fxtx = ttk.Label(self.fixedPoint,text="g(x): ",font=fuente)
        self.pntitxt =ttk.Label(self.fixedPoint,text='Pi: ',font=fuente)
        self.tolerance =ttk.Label(self.fixedPoint,text='tolerance: ',font=fuente)
        self.numIttxt =ttk.Label(self.fixedPoint,text='number of iterations: ',font=fuente)
        self.fx=StringVar()
        self.pi = StringVar()
        self.nIter = StringVar()
        self.presission = StringVar()
        self.fxBox = ttk.Entry(self.fixedPoint,textvariable=self.fx,width=30)
        self.piBox = ttk.Entry(self.fixedPoint,textvariable=self.pi,width=30)
        self.tolBox = ttk.Entry(self.fixedPoint,textvariable=self.presission,width=30)
        self.ItBox = ttk.Entry(self.fixedPoint,textvariable=self.nIter,width=30)
        self.cal_btn = ttk.Button(self.fixedPoint,text="Calculate",command=self.fixedPoint_ )
        self.help_btn = ttk.Button(self.fixedPoint,text="Help",command=self.help_ )
        self.tabinfo = Text(self.fixedPoint, width=37, height=25)
        self.back_mainM = ttk.Button(self.fixedPoint,text="Return Root Menu",command=self.back_main)
        self.fxtx.pack()
        self.fxBox.pack()
        self.pntitxt.pack()
        self.pntitxt.pack()
        self.piBox.pack()
        self.tolerance.pack()
        self.tolBox.pack()
        self.numIttxt.pack()
        self.ItBox.pack()
        self.tabinfo.pack()
        self.cal_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.fixedPoint.mainloop()

    def help_(self):
        self.newWindow = Toplevel(self.fixedPoint)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def fixedPoint_(self):
        try:
            tab = PrettyTable()
            self.tabinfo.delete("1.0", END)
            p=0
            tab.field_names=(["iteraciones", "p"])
            def g(x):
                return eval(self.fxBox.get())
            def puntoFijo(p):
                i=0
                tol = eval(self.tolBox.get())
                pi = eval(self.piBox.get())
                numIt = int(self.ItBox.get())
                while i <=numIt:
                    p = g(pi)
                    if abs(p-pi) < tol:
                        return p
                    i+=1
                    pi = p
                    tab.add_row([i,p])
                print("Error")
            puntoFijo(p)
            txt = "\nRaiz: "+str(puntoFijo(p))
            self.tabinfo.insert('1.0',txt)
            self.tabinfo.insert('1.0',tab)
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
        self.fixedPoint.destroy()
        root.RootMenu()