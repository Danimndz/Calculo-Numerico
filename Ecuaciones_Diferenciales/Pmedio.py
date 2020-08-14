from tkinter import *
from tkinter import ttk,font
from prettytable import PrettyTable
from PIL import Image,ImageTk
from sympy import *
import numpy 
import math
import Menus.EcuDiff as eq

path2 = 'C:/Users/wachu/Documents/IIA/Semestre 5/Calculo Numerico/Proyecto/Ecuaciones_Diferenciales/mayor.png'
class Pmedio:
    def __init__(self):
        self.pmedio_ = Tk()
        self.pmedio_.geometry('650x450')
        self.pmedio_.title("Pmedio Method")
        self.pmedio_.resizable(width=False, height=False)
        fuente = font.Font(weight='normal')

        self.imag2 = ImageTk.PhotoImage(Image.open(path2))
        self.img2 = ttk.Label(self.pmedio_,image = self.imag2,width=400)

        self.fx=StringVar()
        self.fx_label = ttk.Label(self.pmedio_,text='f(x) =',font=fuente)
        self.fxBox = ttk.Entry(self.pmedio_,textvariable=self.fx,width=30)

        self.a_ = StringVar()
        self.a_box = ttk.Entry(self.pmedio_,textvariable=self.a_,width=5)

        self.b_ = StringVar()
        self.b_box = ttk.Entry(self.pmedio_,textvariable=self.b_,width=5)

        self.y_ = StringVar()
        self.y_label = ttk.Label(self.pmedio_,text='yinicial =',font=fuente)
        self.y_box = ttk.Entry(self.pmedio_,textvariable=self.y_,width=5)

        self.h_ = StringVar()
        self.h_label = ttk.Label(self.pmedio_,text='h =',font=fuente)
        self.h_box = ttk.Entry(self.pmedio_,textvariable=self.h_,width=5)

        self.display_txt = Text(self.pmedio_,width=80,height=10)
        self.taylor_btn = ttk.Button(self.pmedio_,text='wi',command=self.Pmedio_)
        self.help_btn = ttk.Button(self.pmedio_,text="Help",command=self.help_ )
        self.back_mainM = ttk.Button(self.pmedio_,text="Return to D.E Menu",command=self.back_main)
        self.fx_label.place(x=160,y=40)
        self.fxBox.place(x=240,y=40)
        self.a_box.place(x=250,y=80)
        self.img2.place(x=300,y=80)
        self.b_box.place(x=360,y=80)
        self.h_label.place(x=280,y=130)
        self.h_box.place(x=310,y=130)
        self.y_label.place(x=350,y=130)
        self.y_box.place(x=410,y=130)
        self.taylor_btn.place(x=290,y=180)
        self.display_txt.place(x=15,y=215)
        self.help_btn.place(x=5,y=420)
        self.back_mainM.place(x=550,y=420)
        self.pmedio_.mainloop()


    def help_(self):
        self.newWindow = Toplevel(self.pmedio_)
        help = ttk.Label(self.newWindow, text = "Seems you're having trouble typing the functions, let me help:"+"\n * = Multiplication \n / = Divide (fraccion) \n - = Substract \n + = Add \n () = parenthesis to separate expressions \n e = math.e \n If you want to elevate a number to the power of n: \n \tif your n is a number simply type de '**' exmpl: x**2, meaning x squared\n \tif your n is a fraccion or a function use 'pow()' property exmpl: pow(2,x) meaning 2**x \n\t if you want to elevate the 'e' number use: math.exp(powerToElevate) \n Trigonometric Functions: \nCosine:\n\tType: cos(), Computes the cosine of x, cos(x)\n\tType: cospi(), Computes the cos(πx) meaning cos(pi*x)\n\tInvers: Type: acos(), Computes the inverse cosine or arccosine of x\nSin:\n\tType: sin(), Computes the sin of x, sin(x)\n\tType sinpi(), Computes the sin(πx) meaning sin(pi*x)\n\tInvers: Type: asin(), Computes the inverse sine or arcsine of x\nTangent:\n\tType: tan(), Computes the tangent of x, tan(x)\n\tInvers: Type: atan(), Computes the invers of tangent or arctargent of x\nSecant:\n\tType: se(), Computes the secant of x, sec(x)\n\tInvers: Type: asec(), Computes the inverse secant of x\ncosecant:\n\tType csc(), Computes the cosecant of x, csc(x)\n\tInvers: Type: acsc(), Computes the inverse cosecant of x\ncotangent:\n\tType: cot(), Computes the cotangent of x, cot(x)\n\tInvers: Type: acot(), Computes the inverse cotangent of x")                                                   
        help.pack()

    def Pmedio_(self):
        try:
            self.display_txt.delete("1.0", END)
            def f(t,y):
                return eval(fx)

            def euler(a_,b_,h_,y0_):
                w = y0_
                wArr = []
                ti = [round(i,1) for i in numpy.arange(a_,b_+h_,h_)]
                for t_ in ti:
                    tab.add_row([t_,w,f(t_,w),f(t_+(h_/2),w+(h_/2)*f(t_,w))])
                    w = w+h*f(t_+(h_/2),w+(h_/2)*f(t_,w))

            tab = PrettyTable()
            tab.field_names=(['ti','wi','f(ti,wi)','f(ti+h/2,wi+h/2f(ti,wi))'])
            fx = self.fxBox.get()
            t = symbols('t')
            y = symbols('y')
            a = float(self.a_box.get())
            b = float(self.b_box.get())
            h = float(self.h_box.get())
            y0 = float(self.y_box.get())
            euler(a,b,h,y0)
            self.display_txt.insert('1.0',tab)
        except ValueError:
            errorMessage = "Wrong or non-existence value, please try again"
            self.display_txt.insert('1.0',errorMessage)

    def back_main(self):
        self.pmedio_.destroy()
        eq.EqDif()


# def m():

#     Pmedio()
#     return 0

# if __name__ == '__main__':
#     m()