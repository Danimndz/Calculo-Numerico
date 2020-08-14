from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.DerivadaIntegralMenu as dev

class IngeracionPuntos:
    def __init__(self):
        self.integracionpuntos_ = Tk()
        self.integracionpuntos_.geometry('300x400')
        self.integracionpuntos_.title("Integration by Given Points")
        self.integracionpuntos_.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')

        self.n_txt = ttk.Label(self.integracionpuntos_,text='N:',font=fuente)
        self.ene = StringVar()
        self.n_box = ttk.Entry(self.integracionpuntos_,textvariable=self.ene,width=5)

        self.txt = ttk.Label(self.integracionpuntos_,text='Leave a space for each given point')
        self.xPoints_text = ttk.Label(self.integracionpuntos_,text='X:',font=fuente)
        self.xPoints = StringVar()
        self.xPoints_box = ttk.Entry(self.integracionpuntos_,textvariable=self.xPoints,width=20)

        self.fxPoints_txt = ttk.Label(self.integracionpuntos_,text='f(x):',font=fuente)
        self.fxPoints = StringVar()
        self.fxPoints_box = ttk.Entry(self.integracionpuntos_,textvariable=self.fxPoints,width=35)

        self.display_txt = Text(self.integracionpuntos_,width=30,height=10)
        self.derivate_btn = ttk.Button(self.integracionpuntos_,text='Find Integrate ',command=self.intPnts_)
        self.help_btn = ttk.Button(self.integracionpuntos_,text="Help",command=self.help_ )
        self.back_mainM = ttk.Button(self.integracionpuntos_,text="Return Integrate Menu",command=self.back_main)
        self.n_txt.pack()
        self.n_box.pack()
        self.txt.pack()
        self.xPoints_text.pack()
        self.xPoints_box.pack()
        self.fxPoints_txt.pack()
        self.fxPoints_box.pack()
        self.display_txt.pack()
        self.derivate_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.integracionpuntos_.mainloop()

    def help_(self):
        self.newWindow = Toplevel(self.integracionpuntos_)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()
    
    def intPnts_(self):
        try:
            self.display_txt.delete("1.0", END)
            n = int(self.n_box.get())
            X =[float(i) for i in self.xPoints_box.get().split(' ')]
            fx = [float(i) for i in self.fxPoints_box.get().split(' ')]
            def cerradasTrapecio(X_,fx_):
                n = 1
                b = X_[len(X_)-1]
                a= X_[0]
                h = (b-a)/n
                return (h/2)*(fx_[0]+fx_[len(fx_)-1])

            def reglaSimpson(X_,fx_):
                n = 2
                b = X_[len(X_)-1]
                a= X_[0]
                h = (b-a)/n
                return (h/3)*(fx_[0]+4*fx_[1]+fx_[2])

            def tresOctavosSimpson(X_,fx_):
                n = 3
                b = X_[len(X_)-1]
                a= X_[0]
                h = (b-a)/n
                return ((3*h)/8)*(fx_[0]+3*fx_[1]+3*fx_[2]+fx_[3])

            def n4(X_,fx_):
                n = 4
                b = X_[len(X_)-1]
                a= X_[0]
                h = (b-a)/n
                return ((2*h)/45)*(7*fx_[0]+32*fx_[1]+12*fx_[2]+32*fx_[3]+7*fx_[4])

            def abiertaPmendio(X_,fx_):
                n = 0
                b = X_[len(X_)-1]
                a= X_[0]
                h = (b-a)/(n+2)
                return 2*h*fx_[0]

            if n == 0: txt = 'Abierta Punto Medio: ' + str(abiertaPmendio(X,fx))
            elif n == 1: txt = 'Cerrada Trapecio: '+ str(cerradasTrapecio(X,fx))
            elif n == 2: txt = 'Simpson: ' + str(reglaSimpson(X,fx))
            elif n ==3: txt = 'Tres Octavos: ' + str(tresOctavosSimpson(X,fx)) + '\n' + 'N4: ',str(n4(X,fx))
            elif n ==4: txt = 'N4: ',str(n4(X,fx))
            
            self.display_txt.insert('1.0',txt)
            
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
        self.integracionpuntos_.destroy()
        dev.DerEintMenu()





# def m():
#     IngeracionPuntos()
#     return 0

# if __name__ == '__main__':
#     m()

    
