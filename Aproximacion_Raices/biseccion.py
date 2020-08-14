from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.RootMenu as root
class Bisection:
    def __init__(self):
        self.bisection = Tk()
        self.bisection.geometry('500x630')
        self.bisection.title("Bisection Method")
        self.bisection.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')
        self.fxtx = ttk.Label(self.bisection,text="f(x): ",font=fuente)
        self.pnt0txt =ttk.Label(self.bisection,text='P0: ',font=fuente)
        self.pnt1txt =ttk.Label(self.bisection,text='P1: ',font=fuente)
        self.tolerance =ttk.Label(self.bisection,text='tolerance: ',font=fuente)
        self.fx=StringVar()
        self.p0 = StringVar()
        self.p1 = StringVar()
        self.presission = StringVar()
        self.fxBox = ttk.Entry(self.bisection,textvariable=self.fx,width=30)
        self.p0Box = ttk.Entry(self.bisection,textvariable=self.p0,width=30)
        self.p1Box = ttk.Entry(self.bisection,textvariable=self.p1,width=30)
        self.tolBox = ttk.Entry(self.bisection,textvariable=self.presission,width=30)
        self.cal_btn = ttk.Button(self.bisection,text="Calculate",command=self.bisection_ )
        self.help_btn = ttk.Button(self.bisection,text="Help",command=self.help_ )
        self.tabinfo = Text(self.bisection, width=37, height=25)
        self.back_mainM = ttk.Button(self.bisection,text="Return Root Menu",command=self.back_main)
        self.fxtx.pack()
        self.fxBox.pack()
        self.pnt0txt.pack()
        self.p0Box.pack()
        self.pnt1txt.pack()
        self.p1Box.pack()
        self.tolerance.pack()
        self.tolBox.pack()
        self.tabinfo.pack()
        self.cal_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.bisection.mainloop()

    def help_(self):
        self.newWindow = Toplevel(self.bisection)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n pi = math.pi \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def bisection_(self):
        try:
            def f(x):
                return eval(self.fxBox.get())
            self.tabinfo.delete("1.0", END)
            if f(float(self.p0Box.get())) >0 and f(float(self.p1Box.get())) < 0 or f(float(self.p0Box.get())) <0 and f(float(self.p1Box.get())) > 0:
                tab = PrettyTable()
                tab.field_names=(["iteraciones", "p"])

                a = eval(self.p0Box.get())
                b =eval(self.p1Box.get())
                tol = eval(self.tolBox.get())
                fa =f(a)
                i=0
                while abs(b-a) > tol:
                    pm = (b+a)/2
                    i+=1
                    if fa*f(pm) < 0:
                        b = pm
                    else: a = pm
                    tab.add_row([i,pm])
                txt = "Raiz: "+ str(pm)
                self.tabinfo.insert('1.0',txt)
                self.tabinfo.insert('1.0',tab)
            else: self.tabinfo.insert('1.0','Intervalo incorrecto,\nno hay cambio de signo\nIngrese otro porfavor')
        except ValueError:
            errorMessage = "Wrong or non-existence value, please try again"
            self.tabinfo.insert('1.0',errorMessage)
        except SyntaxError:
            errorMessage = "Wrong or non-existence value, please try again"
            self.tabinfo.insert('1.0',errorMessage)
        except NameError:
            errorMessage = "Value not define, please try again"
            self.tabinfo.insert('1.0',errorMessage)
        except ZeroDivisionError:
            errorMessage = "Zero division, pleas try again"
            self.tabinfo.insert('1.0',errorMessage)

        
        
    def back_main(self):
        self.bisection.destroy()
        root.RootMenu()
