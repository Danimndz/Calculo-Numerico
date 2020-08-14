from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.RootMenu as root

class Muller: 
    def __init__(self):
        self.Muller_ = Tk()
        self.Muller_.geometry('400x400')
        self.Muller_.title("Müller Method")
        self.Muller_.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')
        self.fxtx = ttk.Label(self.Muller_,text="f(x): ",font=fuente)
        self.X0txt =ttk.Label(self.Muller_,text='X0: ',font=fuente)
        self.X1txt =ttk.Label(self.Muller_,text='X1: ',font=fuente)
        self.X2txt =ttk.Label(self.Muller_,text='X2: ',font=fuente)
        self.fx=StringVar()
        self.X0 = DoubleVar()
        self.X1 = DoubleVar()
        self.X2 = DoubleVar()
        self.fxBox = ttk.Entry(self.Muller_,textvariable=self.fx,width=15)
        self.X0Box = ttk.Entry(self.Muller_,textvariable=self.X0,width=15)
        self.X1Box = ttk.Entry(self.Muller_,textvariable=self.X1,width=15)
        self.X2Box = ttk.Entry(self.Muller_,textvariable=self.X2,width=15)
        self.tabinfo = Text(self.Muller_, width=35, height=10)
        self.help_btn = ttk.Button(self.Muller_,text="Help",command=self.help_ )
        self.cal_btn = ttk.Button(self.Muller_,text="Calculate",command=self.mullerMethod_ )
        self.back_mainM = ttk.Button(self.Muller_,text="Return Main Menu",command=self.back_main)
        self.fxtx.pack()
        self.fxBox.pack()
        self.X0txt.pack()
        self.X0Box.pack()
        self.X1txt.pack()
        self.X1Box.pack()
        self.X2txt.pack()
        self.X2Box.pack()   
        self.tabinfo.pack() 
        self.cal_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.Muller_.mainloop()

    def help_(self):
        self.newWindow = Toplevel(self.Muller_)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def mullerMethod_(self):
        try:
            self.tabinfo.delete("1.0", END)
            fxS = self.fxBox.get()
            XCero = float(self.X0Box.get())
            XUno = float(self.X1Box.get())
            XDos = float(self.X2Box.get())
            
            def f(fx,x):
                return fx.eval(x)

            def muller(fx,X0,X1,X2):
                tol = 10**-5
                X3=0
                error = 1
                while abs(error) > tol:
                    A = (((X1-X2)*(f(fx,X0)-f(fx,X2)) -(X0-X2)*(f(fx,X1)-f(fx,X2)))/((X0-X2)*(X1-X2)*(X0-X1)))
                    B = (((X0-X2)**2*(f(fx,X1)-f(fx,X2)) -(X1-X2)**2*(f(fx,X0)-f(fx,X2)))/((X0-X2)*(X1-X2)*(X0-X1)))
                    C = f(fx,X2)
                    
                    if complex(B).real > 0:
                        X3 = (-(2*C)/(B+(((B**2)-4*A*C)**0.5))+X2)
                    else:
                        X3 = (-(2*C)/(B-(((B**2)-4*A*C)**0.5))+X2)
                    X3 = complex(X3)
                    error = abs(X3-X2)/X3
                    X0 = X1
                    X1 = X2
                    X2 = X3
                return X3

            def sacarCoeff(fxC):
                x = symbols('x')
                a = Poly(fxC,x)
                return a.all_coeffs()

            def buildPoly(arr):
                x = symbols('x')
                pln = Poly(arr,x)
                return pln

            def HornerMethod(fx,coeff,X0,X1,X2):
                arrfinal = []
                x = symbols('x')
                grado = degree(Poly(coeff,x),gen=x)
                while grado > 0:
                    nuevoPoly =[]
                    bn = coeff.pop(0)
                    nuevoPoly.append(bn)
                    R0 = muller(fx,X0,X1,X2)
                    while len(coeff) > 0:
                        bn = coeff[0]+(bn*R0)
                        nuevoPoly.append(bn)
                        coeff.pop(0)
                    coeff = nuevoPoly
                    coeff.pop()
                    fx = Poly(coeff,x)
                    grado -=1
                    num = round(R0.real,5) + round(R0.imag,5)*1j
                    if R0.imag == 0: arrfinal.append(round(R0.real,5))
                    else: arrfinal.append(num)
                return arrfinal
            
            Polfx = buildPoly(sacarCoeff(fxS))
            rootArr = HornerMethod(Polfx,sacarCoeff(fxS),XCero,XUno,XDos)
            for i in rootArr:
                self.tabinfo.insert('1.0',str(i)+'\n')
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
        self.Muller_.destroy()
        root.RootMenu()
