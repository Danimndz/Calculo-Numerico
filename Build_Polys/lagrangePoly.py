from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.PolyMenu as pol


class Lagrange:
    def __init__(self):
        self.lagrange_ = Tk()
        self.lagrange_.geometry('400x400')
        self.lagrange_.title("Lagrange Method")
        self.lagrange_.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')
        self.txt = ttk.Label(self.lagrange_,text='Leave a space for each given point, if your poly is grade n, you will give n+1 points')
        self.polygrade_txt = ttk.Label(self.lagrange_,text='Grade of Poly:',font=fuente)
        self.polygrade = StringVar()
        self.polygrade_box = ttk.Entry(self.lagrange_,textvariable=self.polygrade,width=30)

        self.fx_txt = ttk.Label(self.lagrange_,text='f(x):',font=fuente)
        self.fx_ = StringVar()
        self.fx_box = ttk.Entry(self.lagrange_,textvariable=self.fx_,width=30)

        self.xPoints_text = ttk.Label(self.lagrange_,text='Points:',font=fuente)
        self.xPoints = StringVar()
        self.xPoints_box = ttk.Entry(self.lagrange_,textvariable=self.xPoints,width=20)

        self.evalPoint_txt = ttk.Label(self.lagrange_,text='Point to evaluate:')
        self.evalPoint = StringVar()
        self.evalPoint_box = ttk.Entry(self.lagrange_,textvariable=self.evalPoint,width=5)

        self.display_txt = Text(self.lagrange_,width=45,height=10)
        self.constructPoly_btn = ttk.Button(self.lagrange_,text='Construct Poly',command=self.difDivMethod_)
        self.help_btn = ttk.Button(self.lagrange_,text="Help",command=self.help_ )
        self.back_mainM = ttk.Button(self.lagrange_,text="Return Poly Menu",command=self.back_main)
        self.txt.pack()
        self.polygrade_txt.pack()
        self.polygrade_box.pack()
        self.fx_txt.pack()
        self.fx_box.pack()
        self.xPoints_text.pack()
        self.xPoints_box.pack()
        self.evalPoint_txt.pack()
        self.evalPoint_box.pack()
        self.display_txt.pack()
        self.constructPoly_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.lagrange_.mainloop()


    def help_(self):
        self.newWindow = Toplevel(self.lagrange_)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def difDivMethod_(self):
        try:
            self.display_txt.delete("1.0", END)
            def f(x):
                return eval(fx)

            x = symbols('x')
            n = int(self.polygrade_box.get())
            fx = self.fx_box.get()
            X =[float(i) for i in self.xPoints_box.get().split(' ')]
            FdX =[f(i) for i in X]

            def toPoly(Xarr,FXarr):
                x = symbols('x')
                j = 0
                z = 0
                sumArr = []
                firstED = 0
                firstEN = 0
                while j < len(Xarr):
                    Num = 0
                    Denm = 0
                    multArrN=[]
                    multArrD=[]
                    Xk = Xarr.pop(j)
                    for i in Xarr:
                        Num = Poly(x-i)
                        Denm = Xk-i
                        multArrN.append(Num)
                        multArrD.append(Denm)
                    firstED = multArrD.pop(0)
                    firstEN = multArrN.pop(0)

                    for num in multArrN:
                        firstEN = firstEN*num
                    for denom in multArrD:
                        firstED = firstED*denom

                    res = firstEN/firstED
                    sumArr.append(res)
                    Xarr.insert(j,Xk)
                    j+=1
                aux = []
                while z < len(sumArr):
                    aux.append(sumArr[z]*FXarr[z])
                    z+=1
                polyF = sum(aux)
                return polyF

            def lagrangeNumber(InX,Fx,numEval):
                o = 0
                ñ = 0
                arr = []
                primer_denom = 0
                primer_enum = 0
                while o < len(InX):
                    numerador=[]
                    denominador=[]
                    numK =InX.pop(o)
                    for i in InX:
                        numer = (numEval-i)
                        deno =(numK-i)
                        numerador.append(numer)
                        denominador.append(deno)
                    primer_denom = denominador.pop(0)
                    primer_enum = numerador.pop(0)

                    for num in numerador:
                        primer_enum = primer_enum*num
                    for denom in denominador:
                        primer_denom = primer_denom*denom

                    n_res = primer_enum/primer_denom
                    arr.append(n_res)
                    InX.insert(o,numK)
                    o+=1
                aux_ = []
                while ñ < len(arr):
                    aux_.append(arr[ñ]*Fx[ñ])
                    ñ+=1
                numerito = sum(aux_)
                return numerito
            
            def error(polieval,numE):
                err = abs(f(numE)-polieval)
                return err
            
            p = toPoly(X,FdX)
            if not self.evalPoint.get():
                    self.display_txt.insert('1.0','fx= '+ str(p))
            else:
                numE = float(self.evalPoint_box.get())
                polyEval = round(p.evalf(subs={x:numE}),5)
                txt = 'f({})'.format(numE) + '= ' + str(polyEval)
                E = error(polyEval,numE)
                self.display_txt.insert('1.0','fx= '+ str(p)+'\n'+txt + '\n'+ 'Error: '+ str(E))
        except SyntaxError:
            errorMessage = "Wrong or non-existence value, please try again"
            self.display_txt.insert('1.0',errorMessage)
        except ValueError:
            errorMessage = "Wrong or non-existence value, please try again"
            self.display_txt.insert('1.0',errorMessage)
        except NameError:
            errorMessage = "Value not define, please try again"
            self.display_txt.insert('1.0',errorMessage)
        except ZeroDivisionError:
            errorMessage = "Zero division, pleas try again"
            self.display_txt.insert('1.0',errorMessage)

        


    def back_main(self):
        self.lagrange_.destroy()
        pol.PolyMenu()


# def m():

#     Lagrange()
#     return 0

# if __name__ == '__main__':
#     m()

    