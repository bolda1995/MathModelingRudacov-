from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from cmath import sin, sqrt, pi, exp
class Puason:


    def __init__(self,master,graphics):
        self.leb1 = Label(text="введите начало диапазона", width=25).grid(row=0, column=0, pady=20)
        self.ent1 = Entry(master, width=20)
        self.leb2 = Label(text="ввдите конец дипазона", width=25).grid(row=1, column=0,pady=20)
        self.ent2 = Entry(master, width=20)
        self.leb3 = Label(text="ввидете ламбда", width=25).grid(row=2, column=0,pady=20)
        self.ent3 = Entry(master,width=20)
        self.but3 = Button(master, width=20, text='ввод')
        self.but3['command'] = eval('self.' + graphics)
        self.ent1.grid(row=0, column=1)
        self.ent2.grid(row=1, column=1)
        self.ent3.grid(row=2, column=1)
        self.but3.grid(row=2, column=2)
        self.p = [676.5203681218851
            , -1259.1392167224028
            , 771.32342877765313
            , -176.61502916214059
            , 12.507343278686905
            , -0.13857109526572012
            , 9.9843695780195716e-6
            , 1.5056327351493116e-7
             ]
        self.EPSILON = 1e-07



    def drop_imag(self,z):
        if abs(self.z.imag) <= self.EPSILON:
            self.z = z.real
        return z

    def gamma(self,z):
        self.z = complex(z)
        if self.z.real < 0.5:
            y = pi / (sin(pi * self.z) * self.gamma(1 - self.z))  # Reflection formula
        else:
            z -= 1
            x = 0.99999999999980993
            for (i, self.pval) in enumerate(self.p):
                x += self.pval / (z + i + 1)
            t = z + len(self.p) - 0.5
            y = sqrt(2 * pi) * t ** (self.z + 0.5) * exp(-t) * x
        return self.drop_imag(y)

    def func_dancity(self,x, lam):
        return lam ** x * exp(1) ** (-lam) / self.gamma(x + 1).real

    def func_puason(self,x, lam):
        return sum([self.func_dancity(i, lam) * (x / 50) for i in np.arange(0, x, x / 50)])

    def graphics(self):
        self.a = int(self.ent1.get())
        self.b = int(self.ent2.get())
        self.lam = int(self.ent3.get())
        self.n = 50
        x = [i / self.n for i in range(self.n * self.a, self.n * self.b, self.b - self.a)]
        y = [self.func_puason(i, self.lam) for i in x]
        z = [self.func_dancity(i, self.lam) for i in x]
        plt.plot(x, y)
        plt.plot(x, z)
        plt.show()



def main():
    root = Tk()
    first_block = Puason(root, 'graphics')
    root.mainloop()
if __name__ == '__main__':
    main()
