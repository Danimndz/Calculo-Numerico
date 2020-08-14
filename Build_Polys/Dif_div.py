from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from sympy import *
import math
import Menus.PolyMenu as pol
class DifDivididas:
    def __init__(self):
        self.difdivididas = Tk()
        self.difdivididas.geometry('400x400')
        self.difdivididas.title("Divided Differences Method")
        self.difdivididas.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')
        self.txt = ttk.Label(self.difdivididas,text='Leave a space for each given point')
        self.fxeval_txt = ttk.Label(self.difdivididas,text='Evaluated points(f(x)):',font=fuente)
        self.fxeval = StringVar()
        self.fxeval_box = ttk.Entry(self.difdivididas,textvariable=self.fxeval,width=30)
        self.xPoints_text = ttk.Label(self.difdivididas,text='Points:',font=fuente)
        self.xPoints = StringVar()
        self.xPoints_box = ttk.Entry(self.difdivididas,textvariable=self.xPoints,width=20)
        self.evalPoint_txt = ttk.Label(self.difdivididas,text='Point to evaluate:')
        self.evalPoint = StringVar()
        self.evalPoint_box = ttk.Entry(self.difdivididas,textvariable=self.evalPoint,width=5)
        self.display_txt = Text(self.difdivididas,width=45,height=10)
        self.constructPoly_btn = ttk.Button(self.difdivididas,text='Construct Poly',command=self.difDivMethod_)
        self.help_btn = ttk.Button(self.difdivididas,text="Help",command=self.help_ )
        self.back_mainM = ttk.Button(self.difdivididas,text="Return Poly Menu",command=self.back_main)
        self.txt.pack()
        self.xPoints_text.pack()
        self.xPoints_box.pack()
        self.fxeval_txt.pack()
        self.fxeval_box.pack()
        self.evalPoint_txt.pack()
        self.evalPoint_box.pack()
        self.display_txt.pack()
        self.constructPoly_btn.pack()
        self.help_btn.pack(side=LEFT)
        self.back_mainM.pack(side=RIGHT)
        self.difdivididas.mainloop()


    def help_(self):
        self.newWindow = Toplevel(self.difdivididas)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def difDivMethod_(self):
        try:
            self.display_txt.delete("1.0", END)
            x = symbols('x')
            X =[float(i) for i in self.xPoints_box.get().split(' ')]
            fx = [float(i) for i in self.fxeval_box.get().split(' ')]
            def diferencias_div(arrX,arrFX):
                x = symbols('x')
                res = []
                res.append(arrFX[0])
                n = 1
                while len(arrFX)>1:
                    for i in range(len(arrFX)):
                        if i+1 < len(arrFX):
                            An = round(((arrFX[i+1]-arrFX[i])/(arrX[i+n]-arrX[i])),5)
                            arrFX.pop(i)
                            arrFX.insert(i,An)
                        else:
                            arrFX.pop(i)
                    res.append(arrFX[0])
                    n+=1
                first = res.pop(0)
                z=0
                while z <len(res):
                    exis = 1
                    for k in range(z+1):
                        exis*=expand((x-arrX[k]))
                    pol = expand(res[z]*exis)
                    res.pop(z)
                    res.insert(z,pol)
                    z+=1
                
                res.insert(0,first)
                ans = 0
                for i in res:
                    ans+=i
                return expand(ans)

            p = diferencias_div(X,fx)
            if not self.evalPoint.get():
                self.display_txt.insert('1.0','fx= '+ str(p))
            else:
                po = float(self.evalPoint_box.get())
                txt = 'f({})'.format(po) + '= ' + str(round(p.evalf(subs={x:po}),5))
                self.display_txt.insert('1.0','fx= '+ str(p)+'\n'+txt)
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
        self.difdivididas.destroy()
        pol.PolyMenu()


# def m():

#     DifDivididas()
#     return 0

# if __name__ == '__main__':
#     m()

    




