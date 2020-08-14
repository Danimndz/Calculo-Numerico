from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.DerivadaIntegralMenu as dev

class DifNumerica:
    def __init__(self):
        self.difnumerica_ = Tk()
        self.difnumerica_.geometry('400x500')
        self.difnumerica_.title("Numerical differentiation")
        self.difnumerica_.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')

        self.txt = ttk.Label(self.difnumerica_,text='Leave a space for each given point')
        self.xPoints_text = ttk.Label(self.difnumerica_,text='X:',font=fuente)
        self.xPoints = StringVar()
        self.xPoints_box = ttk.Entry(self.difnumerica_,textvariable=self.xPoints,width=20)

        self.fxPoints_txt = ttk.Label(self.difnumerica_,text='f(x):',font=fuente)
        self.fxPoints = StringVar()
        self.fxPoints_box = ttk.Entry(self.difnumerica_,textvariable=self.fxPoints,width=35)

        self.display_txt = Text(self.difnumerica_,width=45,height=20)
        self.derivate_btn = ttk.Button(self.difnumerica_,text='Find Derivate',command=self.difNumMethod_)
        self.help_btn = ttk.Button(self.difnumerica_,text="Help",command=self.help_ )
        self.back_mainM = ttk.Button(self.difnumerica_,text="Return Derivate Menu",command=self.back_main)
        self.txt.pack()
        self.xPoints_text.pack()
        self.xPoints_box.pack()
        self.fxPoints_txt.pack()
        self.fxPoints_box.pack()
        self.display_txt.pack()
        self.derivate_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.difnumerica_.mainloop()

    def help_(self):
        self.newWindow = Toplevel(self.difnumerica_)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()
    
    def difNumMethod_(self): 
        try:
            self.display_txt.delete("1.0", END)
            X =[float(i) for i in self.xPoints_box.get().split(' ')]
            fx = [float(i) for i in self.fxPoints_box.get().split(' ')]
            h = X[1]-X[0]

            def TformulaUno(fex,ha,index): 
                fxP = (1/(2*ha))*(-3*fex[index]+4*fex[index+1]-fex[index+2])
                return fxP

            def TformulaDos(fex,ha,index):
                fxP = (1/(2*ha))*(fex[index+1]-fex[index-1])
                return fxP

            def CformulaUno(fex,ha,index):
                fxP = (1/(12*ha))*((-25*fex[index])+(48*fex[index+1])-(36*fex[index+2])+(16*fex[index+3])-(3*fex[index+4]))
                return fxP

            def CformulaDos(fex,ha,index):
                fxP = (1/(12*ha))*((fex[index+2])-(8*fex[index-1])+(8*fex[index+1])-(fex[index+2]))
                return fxP

            def dif_num(Xis,Pfx,Dh):
                res = []
                ache = -Dh
                for i in range(len(Xis)):
                    if len(Xis)-1 >= 5:
                        if i-1 < 0:
                            res.append(CformulaUno(Pfx,Dh,i))
                        elif i-2 >=0 and i+2 <=len(Xis)-1:
                            res.append(CformulaDos(Pfx,Dh,i))
                        else:
                            aux = Pfx[::-1]
                            res.append(CformulaUno(aux,ache,0))    
                    elif len(Xis)-1 <= 3:
                        if i-1 <0:
                            res.append(TformulaUno(Pfx,Dh,i))
                        elif i-1 >=0 and i+1 <=len(Xis)-1:
                            res.append(TformulaDos(Pfx,Dh,i))
                        else:
                            aux = Pfx[::-1]
                            res.append(TformulaUno(aux,ache,0))
                return res

            tab = PrettyTable()
            field_names = ['x','fx','f´x']
            tab.add_column(field_names[0],X)
            tab.add_column(field_names[1],fx)
            tab.add_column(field_names[2],dif_num(X,fx,h))
            self.display_txt.insert('1.0',tab)
            
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
        self.difnumerica_.destroy()
        dev.DerEintMenu()





def m():
    DifNumerica()
    return 0

if __name__ == '__main__':
    m()

    