from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.PolyMenu as pol

class Hermite:
    def __init__(self):
        self.hermite_ = Tk()
        self.hermite_.geometry('400x450')
        self.hermite_.title("Hermite Method")
        self.hermite_.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')
        self.txt = ttk.Label(self.hermite_,text='Leave a space for each given point')
        self.xPoints_text = ttk.Label(self.hermite_,text='X:',font=fuente)
        self.xPoints = StringVar()
        self.xPoints_box = ttk.Entry(self.hermite_,textvariable=self.xPoints,width=20)

        self.fxPoints_txt = ttk.Label(self.hermite_,text='f(x):',font=fuente)
        self.fxPoints = StringVar()
        self.fxPoints_box = ttk.Entry(self.hermite_,textvariable=self.fxPoints,width=30)

        self.fxpPoints_text = ttk.Label(self.hermite_,text='f´(x):',font=fuente)
        self.fxpPoints = StringVar()
        self.fxpPoints_box = ttk.Entry(self.hermite_,textvariable=self.fxpPoints,width=30)

        self.fx_txt = ttk.Label(self.hermite_,text='function:',font=fuente)
        self.fx_ = StringVar()
        self.fx_box = ttk.Entry(self.hermite_,textvariable=self.fx_,width=20)

        self.evalPoint_txt = ttk.Label(self.hermite_,text='Point to evaluate:')
        self.evalPoint = StringVar()
        self.evalPoint_box = ttk.Entry(self.hermite_,textvariable=self.evalPoint,width=5)

        self.display_txt = Text(self.hermite_,width=45,height=10)
        self.constructPoly_btn = ttk.Button(self.hermite_,text='Construct Poly',command=self.difDivMethod_)
        self.help_btn = ttk.Button(self.hermite_,text="Help",command=self.help_ )
        self.back_mainM = ttk.Button(self.hermite_,text="Return Poly Menu",command=self.back_main)
        self.txt.pack()
        self.xPoints_text.pack()
        self.xPoints_box.pack()
        self.fxPoints_txt.pack()
        self.fxPoints_box.pack()
        self.fxpPoints_text.pack()
        self.fxpPoints_box.pack()
        self.evalPoint_txt.pack()
        self.evalPoint_box.pack()
        self.fx_txt.pack()
        self.fx_box.pack()
        self.display_txt.pack()
        self.constructPoly_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.hermite_.mainloop()


    def help_(self):
        self.newWindow = Toplevel(self.hermite_)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def difDivMethod_(self):
        try:
            self.display_txt.delete("1.0", END)
            x = symbols('x')
            X =[float(i) for i in self.xPoints_box.get().split(' ')]
            fdx = [float(i) for i in self.fxPoints_box.get().split(' ')]
            fdxP = [float(i) for i in self.fxpPoints_box.get().split(' ')]

            def Lin(exis):
                x = symbols('x')
                j = 0
                arrPolys = []
                firstED = 0
                firstEN = 0
                while j < len(exis):
                    Num = 0
                    Denm = 0
                    multArrN=[]
                    multArrD=[]
                    Xk = exis.pop(j)
                    for i in exis:
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
                    arrPolys.append(res)
                    exis.insert(j,Xk)
                    j+=1
                return arrPolys
            def LinP(PolysP):
                arrP = [diff(poly) for poly in PolysP]
                return arrP
            def Linsqr(Polys2):
                arrP2 = [expand(poly**2 )for poly in Polys2]
                return arrP2
            def Hi(xis,LinDer,LinalC):
                x = symbols('x')
                HcG = []
                for i in range(len(xis)):
                    HcG.append(expand(((1-(2*(x-xis[i])*round(LinDer[i].evalf(subs={x:xis[i]}),7)))*LinalC[i])))
                return HcG

            def Hgorrito(xis,LinalC):
                x = symbols('x')
                Hgorro =[]
                for i in range(len(xis)):
                    Hgorro.append(expand(((x-xis[i])*LinalC[i])))
                return Hgorro

            def H(HsinG,HconG,xis,fxis,fxisP):
                x = symbols('x')
                poly = 0
                for i in range(len(xis)):
                    poly+= (fxis[i]*HsinG[i]) + (fxisP[i]*HconG[i])
                return poly

            def error(fx_,polieval,peval):
                fxeval = fx.evalf(subs={x:peval})
                err = abs(fxeval-polieval)
                return err

            LDeriv = LinP(Lin(X))
            LalCuadr = Linsqr(Lin(X))
            HsinGorro = Hi(X,LDeriv,LalCuadr)
            HconGorro = Hgorrito(X,LalCuadr)
            
            ache = H(HsinGorro,HconGorro,X,fdx,fdxP)
            if not self.evalPoint.get():
                    self.display_txt.insert('1.0','fx= '+ str(ache))
            else:
                fx = eval(self.fx_box.get())
                numE = float(self.evalPoint_box.get())
                polyEval = ache.evalf(subs={x:numE})
                txt = 'f({})'.format(numE) + '= ' + str(polyEval)
                E = error(fx,polyEval,numE)
                self.display_txt.insert('1.0','fx= '+ str(ache)+'\n'+txt + '\n'+ 'Error: '+ str(E))
                
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
        self.hermite_.destroy()
        pol.PolyMenu()


# def m():

#     Hermite()
#     return 0

# if __name__ == '__main__':
#     m()

    