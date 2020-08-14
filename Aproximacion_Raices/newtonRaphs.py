from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.RootMenu as root
class NewtonRaphson:
    def __init__(self):
        self.newtonRaphson = Tk()
        self.newtonRaphson.geometry('500x630')
        self.newtonRaphson.title("Newton Raphson Method")
        self.newtonRaphson.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')
        self.fxtx = ttk.Label(self.newtonRaphson,text="f(x): ",font=fuente)
        self.pntitxt =ttk.Label(self.newtonRaphson,text='Pi: ',font=fuente)
        self.tolerance =ttk.Label(self.newtonRaphson,text='tolerance: ',font=fuente)
        self.numIttxt =ttk.Label(self.newtonRaphson,text='number of iterations: ',font=fuente)
        self.fx=StringVar()
        self.pi = StringVar()
        self.nIter = StringVar()
        self.presission = StringVar()
        self.fxBox = ttk.Entry(self.newtonRaphson,textvariable=self.fx,width=30)
        self.piBox = ttk.Entry(self.newtonRaphson,textvariable=self.pi,width=30)
        self.tolBox = ttk.Entry(self.newtonRaphson,textvariable=self.presission,width=30)
        self.ItBox = ttk.Entry(self.newtonRaphson,textvariable=self.nIter,width=30)
        self.tabinfo = Text(self.newtonRaphson, width=37, height=25)
        self.cal_btn = ttk.Button(self.newtonRaphson,text="Calculate",command=self.newtonRaphson_ )
        self.help_btn = ttk.Button(self.newtonRaphson,text="Help",command=self.help_ )
        self.back_mainM = ttk.Button(self.newtonRaphson,text="Return Root Menu",command=self.back_main)
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
        self.newtonRaphson.mainloop()

    def help_(self):
        self.newWindow = Toplevel(self.newtonRaphson)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def newtonRaphson_(self):
        try:
            tab = PrettyTable()
            self.tabinfo.delete("1.0", END)
            tab.field_names=(["iteraciones", "p"])
            def f(x):
                return eval(self.fxBox.get())

            def derivadaEval(fx,Po):
                x = symbols('x')
                derivada = diff(fx)
                derivadaEval = derivada.evalf(subs={x:Po})
                return derivadaEval

            def Pn(Po,fx):
                return Po - (f(Po)/derivadaEval(fx,Po))
            pn=0
            def neWRaph(pn):
                i=0
                fx = self.fxBox.get()
                tol = eval(self.tolBox.get())    
                Po = eval(self.piBox.get())
                numIt = int(self.ItBox.get())
                while i <= numIt:
                    pn = Pn(Po,fx)
                    if abs(pn-Po) < tol:
                        return pn
                    i+=1
                    Po=pn
                    tab.add_row([i,pn])
                print('Error')
            neWRaph(pn)
            txt = "\nRaiz: "+str(neWRaph(pn))
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
        self.newtonRaphson.destroy()
        root.RootMenu()