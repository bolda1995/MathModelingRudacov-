import tkinter
from tkinter import *
import tkinter as tk
import random
class Table:
    def __init__(self, master,table):
        self.leb1 = Label(text="ввидите 10 числел от 0 до 9",width=27).grid(row=0,column=0,pady=20)
        self.ent1 = Entry(master, width=20)

        self.leb2 = Label(text="ввидите 10 числел от 10 до 99",width=27).grid(row=2,column=0,pady=20)
        self.ent2 = Entry(master, width=20)

        self.leb3 = Label(text="ввидите 10 числел от 100 до 999",width=27).grid(row=3, column=0, pady=20)
        self.ent3 = Entry(master, width=20)
        self.but3 = Button(master,width=20, text='ввод')
        self.but3['command'] = eval('self.' + table)
        self.ent1.grid(row=0,column=1)
        self.ent2.grid(row=2,column=1)
        self.ent3.grid(row=3, column=1)

        self.but3.grid(row=3, column=2)
        self.leb4 = Label().grid(row=4, column=0, pady=40)
        self.a1 = [random.randint(0, 10) for i in range(10)]
        self.a2 = [random.randint(10, 99) for i in range(10)]
        self.a3 = [random.randint(100, 999) for i in range(10)]
        self.a4 = [0 for i in range(10)]
        self.a5 = [0 for i in range(10)] 
        self.a6 = [0 for i in range(10)]
        for i in range(0, 10):
            self.b1 = Entry(width=27,justify='center')
            self.b1.grid(row=5+i, column=0)
            self.b1.delete(0, 'end')
            self.b1.insert(0, self.a1[i])

            self.b2 = Entry(width=27,justify='center')
            self.b2.grid(row=5+i, column=1)
            self.b2.delete(0, 'end')
            self.b2.insert(0, self.a2[i])
            self.b3 = Entry(width=27, justify='center')
            self.b3.grid(row=5 + i, column=2)
            self.b3.delete(0, 'end')
            self.b3.insert(0, self.a3[i])

            self.b4 = Entry(width=27, justify='center')
            self.b4.grid(row=5 + i, column=3)
            self.b4.delete(0, 'end')
            self.b4.insert(0, self.a4[i])

            self.b5 = Entry(width=27, justify='center')
            self.b5.grid(row=5 + i, column=4)
            self.b5.delete(0, 'end')
            self.b5.insert(0, self.a5[i])

            self.b6 = Entry(width=27, justify='center')
            self.b6.grid(row=5 + i, column=5)
            self.b6.delete(0, 'end')
            self.b6.insert(0, self.a6[i])

        self.leb5 = Label().grid(row=17, column=0, pady=40)

        self.a1 = [i / 9 for i in self.a1]

        self.t = 4  # максимальное длина интервала
        self.array_inter = [0 for i in range(self.t + 1)]
        self.j = -1  # попадание в единуцу массива
        self.s = 0
        self.r = 0
        for i in range(len(self.a1)):
            if 0.1 <= self.a1[i] <= 0.9 or i == len(self.a1) - 1:
                self.array_inter[(min(self.r, self.t))] += 1
                self.s += 1
                self.r = 0
            else:
                self.r += 1
        self.p = 0.9 - 0.1

        self.V = 0
        for i in range(0, self.t):
            self.pi = self.p * (1 - self.p) ** i
            self.V += pow(self.array_inter[i], 2) / self.pi
        self.V += pow(self.array_inter[self.t], 2) / (1 - self.p) ** self.t
        self.V = self.V / self.s
        self.V = self.V - self.s



        self.end1 = Entry(width=27, justify='center')
        self.end1.grid(row=18, column=0)
        self.end1.delete(0, 'end')
        self.end1.insert(0, self.V)

        self.a2 = [(i - 10) / 89 for i in self.a2]
        print(self.a2)
        self.t1 = 4  # максимальное длина интервала
        self.array_inter1 = [0 for i in range(self.t1 + 1)]

        self.s1 = 0
        self.r1 = 0
        for i in range(len(self.a2)):
            if 0.1 <= self.a2[i] <= 0.9 or i == len(self.a2) - 1:
                self.array_inter1[(min(self.r1, self.t1))] += 1
                self.s1 += 1
                self.r1 = 0
            else:
                self.r1 += 1
        self.p1 = 0.9 - 0.1

        self.V1 = 0
        for i in range(0, self.t1):
            self.pi1 = self.p1 * (1 - self.p1) ** i
            self.V1 += pow(self.array_inter1[i], 2) / self.pi1
        self.V1 += pow(self.array_inter1[self.t1], 2) / (1 - self.p1) ** self.t1
        self.V1 = self.V1 / self.s1
        self.V1 = self.V1 - self.s1



        self.end2 = Entry(width=27, justify='center')
        self.end2.grid(row=18, column=1)
        self.end2.delete(0, 'end')
        self.end2.insert(0, self.V1)

        self.a3 = [(i - 100) / 899 for i in self.a3]
        print(self.a3)
        self.t2 = 4  # максимальное длина интервала
        self.array_inter2 = [0 for i in range(self.t2 + 1)]

        self.s2 = 0
        self.r2 = 0
        for i in range(len(self.a3)):
            if 0.1 <= self.a3[i] <= 0.9 or i == len(self.a3) - 1:
                self.array_inter2[(min(self.r2, self.t2))] += 1
                self.s2 += 1
                self.r2 = 0
            else:
                self.r2 += 1
        self.p2 = 0.9 - 0.1

        self.V2 = 0
        for i in range(0, self.t1):
            self.pi2 = self.p2 * (1 - self.p2) ** i
            self.V2 += pow(self.array_inter2[i], 2) / self.pi2
        self.V2 += pow(self.array_inter2[self.t2], 2) / (1 - self.p2) ** self.t2
        self.V2 = self.V2 / self.s2
        self.V2 = self.V2 - self.s2



        self.end3 = Entry(width=27, justify='center')
        self.end3.grid(row=18, column=2)
        self.end3.delete(0, 'end')
        self.end3.insert(0, self.V2)

        self.end4 = Entry(width=27, justify='center')
        self.end4.grid(row=18, column=3)
        self.end4.delete(0, 'end')
        self.end4.insert(0, 0)

        self.end5 = Entry(width=27, justify='center')
        self.end5.grid(row=18, column=4)
        self.end5.delete(0, 'end')
        self.end5.insert(0, 0)

        self.end6 = Entry(width=27, justify='center')
        self.end6.grid(row=18, column=5)
        self.end6.delete(0, 'end')
        self.end6.insert(0, 0)


    def table(self):
        self.s1 = self.ent1.get()
        self.s1 = [int(i) for i in self.s1.split()]
        self.s2 = self.ent2.get()
        self.s2 = [int(i) for i in self.s2.split()]
        self.s3 = self.ent3.get()
        self.s3 = [int(i) for i in self.s3.split()]



        for i in range(0, 10):
            self.b4 = Entry(width=27, justify='center')
            self.b4.grid(row=5 + i, column=3)
            self.b4.delete(0, 'end')
            self.b4.insert(0, self.s1[i])

            self.b5 = Entry(width=27, justify='center')
            self.b5.grid(row=5 + i, column=4)
            self.b5.delete(0, 'end')
            self.b5.insert(0, self.s2[i])

            self.b6 = Entry(width=27, justify='center')
            self.b6.grid(row=5 + i, column=5)
            self.b6.delete(0, 'end')
            self.b6.insert(0, self.s3[i])

        self.s1 = [i / 9 for i in self.s1]
        self.t = 4  # максимальное длина интервала
        self.array_inter = [0 for i in range(self.t + 1)]
        self.j = -1  # попадание в единуцу массива
        self.s = 0
        self.r = 0
        for i in range(len(self.a1)):
            if 0.1 <= self.s1[i] <= 0.9 or i == len(self.a1) - 1:
                self.array_inter[(min(self.r, self.t))] += 1
                self.s += 1
                self.r = 0
            else:
                self.r += 1
        self.p = 0.9 - 0.1

        self.V = 0
        for i in range(0, self.t):
            self.pi = self.p * (1 - self.p) ** i
            self.V += pow(self.array_inter[i], 2) / self.pi
        self.V += pow(self.array_inter[self.t], 2) / (1 - self.p) ** self.t
        self.V = self.V / self.s
        self.V = self.V - self.s

        self.end4 = Entry(width=27, justify='center')
        self.end4.grid(row=18, column=3)
        self.end4.delete(0, 'end')
        self.end4.insert(0, self.V)

        self.s2 = [(i - 10) / 89 for i in self.s2]
        self.t1 = 4  # максимальное длина интервала
        self.array_inter1 = [0 for i in range(self.t1 + 1)]
        self.j1 = -1  # попадание в единуцу массива
        self.s_1 = 0
        self.r1 = 0
        for i in range(len(self.a1)):
            if 0.1 <= self.s2[i] <= 0.9 or i == len(self.s2) - 1:
                self.array_inter1[(min(self.r1, self.t1))] += 1
                self.s_1 += 1
                self.r1 = 0
            else:
                self.r1 += 1
        self.p1 = 0.9 - 0.1

        self.V1 = 0
        for i in range(0, self.t1):
            self.pi1 = self.p1 * (1 - self.p1) ** i
            self.V1 += pow(self.array_inter1[i], 2) / self.pi1
        self.V1 += pow(self.array_inter1[self.t1], 2) / (1 - self.p1) ** self.t1
        self.V1 = self.V1 / self.s_1
        self.V1 = self.V1 - self.s_1

        self.end5 = Entry(width=27, justify='center')
        self.end5.grid(row=18, column=4)
        self.end5.delete(0, 'end')
        self.end5.insert(0, self.V1)

        self.s3 = [(i - 100) / 899 for i in self.s3]
        print(self.s3)
        self.t3 = 4  # максимальное длина интервала
        self.array_inter2 = [0 for i in range(self.t3 + 1)]
        self.s_2 = 0
        self.r2 = 0
        for i in range(len(self.s3)):
            if 0.1 <= self.s3[i] <= 0.9 or i == len(self.s3) - 1:
                self.array_inter2[(min(self.r2, self.t3))] += 1
                self.s_2 += 1
                self.r2 = 0
            else:
                self.r2 += 1
        self.p2 = 0.9 - 0.1

        self.V2 = 0
        for i in range(0, self.t3):
            self.pi2 = self.p2 * (1 - self.p2) ** i
            self.V2 += pow(self.array_inter2[i], 2) / self.pi2
        self.V2 += pow(self.array_inter2[self.t3], 2) / (1 - self.p2) ** self.t3
        self.V2 = self.V2 / self.s_2
        self.V2 = self.V2 - self.s_2

        self.end6 = Entry(width=27, justify='center')
        self.end6.grid(row=18, column=5)
        self.end6.delete(0, 'end')
        self.end6.insert(0, self.V2)








def main():
    root = Tk()
    first_block = Table(root,'table')


    root.mainloop()

if __name__ == '__main__':
    main()
