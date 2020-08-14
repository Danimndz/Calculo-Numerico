from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from PIL import Image,ImageTk
from sympy import *
import math
import Menus.DerivadaIntegralMenu as dev
path = 'C:/Users/wachu/Documents/IIA/Semestre 5/Calculo Numerico/Proyecto/Integrar_Derivar/integralSymbol.png'
class AbiertaCompuesta:
    def __init__(self):
        self.abiertacompuesta_ = Tk()
        self.abiertacompuesta_.geometry('400x350')
        self.abiertacompuesta_.title("Open Integrate")
        self.abiertacompuesta_.resizable(width=False, height=False)
        self.abiertacompuesta_.config(background='white')
        fuente = font.Font(weight='normal')
        self.imag = ImageTk.PhotoImage(Image.open(path))
        self.img = Label(self.abiertacompuesta_,image = self.imag)

        self.b_ = StringVar()
        self.b_box = ttk.Entry(self.abiertacompuesta_,textvariable=self.b_,width=5)

        self.a_ = StringVar()
        self.a_box = ttk.Entry(self.abiertacompuesta_,textvariable=self.a_,width=5)

        self.equal_txt = ttk.Label(self.abiertacompuesta_,text='=',font=fuente)
        self.equal_txt.config(background='white')
        self.fx_ = StringVar()
        self.fx_box = ttk.Entry(self.abiertacompuesta_,textvariable=self.fx_,width=15)
        self.result_txt = Text(self.abiertacompuesta_,width=15,height=1)

        self.n_txt = ttk.Label(self.abiertacompuesta_,text='N:',font=fuente)
        self.n_txt.config(background='white')
        self.n_ = StringVar()
        self.n_box = ttk.Entry(self.abiertacompuesta_,textvariable=self.n_,width=5)

        self.int_btn = ttk.Button(self.abiertacompuesta_,text='Calculate',command=self.abiertaCompuesta)
        self.help_btn = ttk.Button(self.abiertacompuesta_,text="Help",command=self.help_ )
        self.back_mainM = ttk.Button(self.abiertacompuesta_,text="Return Integrate Menu",command=self.back_main)
        self.n_txt.pack()
        self.n_box.pack()
        self.img.place(x=30, y=100)
        self.a_box.place(x=30, y=250)
        self.b_box.place(x=60, y=80)
        self.fx_box.place(x=95,y=170)
        self.equal_txt.place(x=200,y=170)
        self.result_txt.place(x=220,y=170)
        self.int_btn.place(x=150,y=250)
        self.help_btn.place(x=5,y=300)
        self.back_mainM.place(x=270,y=300)
        self.abiertacompuesta_.mainloop()


    def help_(self):
        self.newWindow = Toplevel(self.abiertacompuesta_)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def abiertaCompuesta(self):
        try:
            self.result_txt.delete("1.0", END)
            x = symbols('x')
            n = int(self.n_box.get())
            fx = self.fx_box.get()
            a = float(self.a_box.get())
            b = float(self.b_box.get())
            

            def f(x):
                return eval(fx)

            def abiertaCompuesta_(a_,b_,n_):
                suma = 0
                h = (b_-a_)/(n_+2)
                Xi = [a+(i*h) for i in range(1,n_+2)]
                for i in range(int(n/2)+1):
                    suma+=f(Xi[2*i])
                return (2*h)*suma
            
            inter = round(abiertaCompuesta_(a,b,n),5)
            self.result_txt.insert('1.0',str(inter))
        except SyntaxError:
            errorMessage = "Wrong or non-existence value, please try again"
            self.result_txt.insert('1.0',errorMessage)
        except ValueError:
            errorMessage = "Wrong or non-existence value, please try again"
            self.result_txt.insert('1.0',errorMessage)
        except NameError:
            errorMessage = "Value not define, please try again"
            self.result_txt.insert('1.0',errorMessage)
        except ZeroDivisionError:
            errorMessage = "Zero division, pleas try again"
            self.result_txt.insert('1.0',errorMessage)

    def back_main(self):
        self.abiertacompuesta_.destroy()
        dev.DerEintMenu()


# def m():
#     AbiertaCompuesta()
#     return 0

# if __name__ == '__main__':
#     m()

    