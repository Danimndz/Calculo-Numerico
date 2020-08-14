from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.RootMenu as root
xarr =[]
class HornerMethod: 
    def __init__(self):
        self.HornerMethod_ = Tk()
        self.HornerMethod_.geometry('400x400')
        self.HornerMethod_.title("Horner Method")
        self.HornerMethod_.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')
        self.fxtx = ttk.Label(self.HornerMethod_,text="f(x): ",font=fuente)
        self.pnt0txt =ttk.Label(self.HornerMethod_,text='P0: ',font=fuente)
        self.fx=StringVar()
        self.p0 = StringVar()
        self.fxBox = ttk.Entry(self.HornerMethod_,textvariable=self.fx,width=30)
        self.p0Box = ttk.Entry(self.HornerMethod_,textvariable=self.p0,width=30)
        self.tabinfo = Text(self.HornerMethod_, width=35, height=10)
        self.help_btn = ttk.Button(self.HornerMethod_,text="Help",command=self.help_ )
        self.cal_btn = ttk.Button(self.HornerMethod_,text="Calculate",command=self.hornerMethod_ )
        self.back_mainM = ttk.Button(self.HornerMethod_,text="Return Root Menu",command=self.back_main)
        self.fxtx.pack()
        self.fxBox.pack()
        self.pnt0txt.pack()
        self.p0Box.pack()   
        self.tabinfo.pack() 
        self.cal_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.HornerMethod_.mainloop()

    def help_(self):
        self.newWindow = Toplevel(self.HornerMethod_)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def hornerMethod_(self):
        try:
            self.tabinfo.delete("1.0", END)
            fx_ = self.fxBox.get()
            P0 = float(self.p0Box.get())

            def f(fx,Po):
                return fx.eval(Po)

            def derivadaEval(fx,Po):
                derivada = fx.diff()
                derivadaEval = derivada.eval(Po)
                return derivadaEval

            def Pn(Po,fx):
                return Po - (f(fx,Po)/derivadaEval(fx,Po))
            
            def newtonRaphs(Po,fx):
                numIt = 10000
                tol = 10**-5
                i = 0
                while i <=numIt:
                    pn = Pn(Po,fx)
                    if abs(pn-Po) < tol:
                        return pn
                    i+=1
                    Po = pn
                    if i >=numIt:
                        return -1

            def sacarCoeff(fx):
                x = symbols('x')
                a = Poly(fx,x)
                return a.all_coeffs()

            def buildPoly(arr):
                x = symbols('x')
                pln = Poly(arr,x)
                return pln

            def HornerMethod(fx,coeff,Po):
                x = symbols('x')
                grado = degree(Poly(coeff,x),gen=x)
                while grado > 2:
                    nuevoPoly =[]
                    bn = coeff.pop(0)
                    nuevoPoly.append(bn)
                    X0 = newtonRaphs(Po,fx)
                    if X0 == -1: return
                    else:
                        while len(coeff) > 0:
                            bn = coeff[0]+(bn*X0)
                            nuevoPoly.append(bn)
                            coeff.pop(0)
                        coeff = nuevoPoly
                        coeff.pop()
                        fx = Poly(coeff,x)
                        grado -=1
                        self.tabinfo.insert('1.0',str(X0)+'\n')
                return fx
            
            def chicharronera(fx):
                Poln = str(fx).split('(')
                Poln = str(Poln).split(',')
                Poln = str(Poln[1]).split('"')
                finalPoln = str(Poln[1])
                abc = sacarCoeff(finalPoln)
                A = abc[0]
                B = abc[1]
                C = abc[2]
                try:
                    R1 = (-B + (math.sqrt(B**2-(4*A*C))))/(2*A)
                    R2 = (-B - (math.sqrt(B**2-(4*A*C))))/(2*A)
                    st = str(R1) + '\n' + str(R2)
                    return st
                except ValueError:
                    return 'Math Error, for complex numbers use müller method'
            
            Polfx = buildPoly(sacarCoeff(fx_))
            txt = str(chicharronera(HornerMethod(Polfx,sacarCoeff(fx_),P0))) + '\n'
            self.tabinfo.insert('1.0',txt)
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
        self.HornerMethod_.destroy()
        root.RootMenu()
