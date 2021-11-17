import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QGridLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from distribution import *
from event_model import *
from step_model import *

class MainWindow(QMainWindow,QWidget):
    def __init__(self):

        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1300, 600))
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com")
        self.init_but()



    def init_but(self):
        self.line = QLineEdit(self)
        self.line.setGeometry(330, 10, 50, 30)
        passwordLabel = QLabel('ввидите диапазон генератора через запитую', self)
        passwordLabel.setGeometry(0, 5, 350, 30)
        self.firstbutton = QPushButton('ввод', self)
        self.firstbutton.setGeometry(10, 300, 50, 30)
        self.firstbutton.clicked.connect(self.result)


        Label = QLabel('ввидите mu', self)
        Label.setGeometry(0, 25, 350, 30)
        self.line1 = QLineEdit(self)
        self.line1.setGeometry(90,30, 50, 30)

        Label1 = QLabel('ввидите sigma', self)
        Label1.setGeometry(0, 55, 350, 30)
        self.line2 = QLineEdit(self)
        self.line2.setGeometry(120, 60, 50, 30)

        Label3 = QLabel('ввидите k', self)
        Label3.setGeometry(0, 95, 350, 30)
        self.line3 = QLineEdit(self)
        self.line3.setGeometry(80, 95, 50, 30)

        Label4 = QLabel('ввидите lambda', self)
        Label4.setGeometry(0, 130, 350, 30)
        self.line4 = QLineEdit(self)
        self.line4.setGeometry(130, 130, 50, 30)

        Label5 = QLabel('ввидите количество задач', self)
        Label5.setGeometry(0, 170, 350, 30)
        self.line5 = QLineEdit(self)
        self.line5.setGeometry(190, 170, 50, 30)

        Label6 = QLabel('ввидите процент повторений', self)
        Label6.setGeometry(0, 210, 350, 30)
        self.line6 = QLineEdit(self)
        self.line6.setGeometry(210, 210, 50, 30)

        Label7 = QLabel('ввидите шаг', self)
        Label7.setGeometry(0, 250, 350, 30)
        self.line7 = QLineEdit(self)
        self.line7.setGeometry(100, 250, 50, 30)



        Label8 = QLabel('событие модели', self)
        Label8.setGeometry(0, 350, 350, 30)
        self.output1 = QLineEdit(self)
        self.output1.setGeometry(120, 350, 500, 30)

        Label9 = QLabel('шаг модели', self)
        Label9.setGeometry(0, 390, 350, 30)
        self.output2 = QLineEdit(self)
        self.output2.setGeometry(120, 390, 500, 30)


    def result(self):

        a,b = [float(i) for i in self.line.text().split(',')]
        generator = EvenDistribution(a, b)
        mu = int(self.line1.text())
        sigma = float(self.line2.text())
        k = int(self.line3.text())
        lambd = int(self.line4.text())
        processor = PoissonDistribution(k, lambd)

        total_tasks = int(self.line5.text())
        repeat_percentage = int(self.line6.text())
        step = float(self.line7.text())
        """
        a, b = 1, 10
        generator = EvenDistribution(a, b)

        mu, sigma = 4, 0.2
        processor = NormalDistribution(mu, sigma)
        k = 1
        lambd = 4
        processor = PoissonDistribution(k, lambd);

        total_tasks = 1000
        repeat_percentage = 0
        step = 0.01"""
        out1 = event_model(generator, processor, total_tasks, repeat_percentage)
        out2 = step_model(generator, processor, total_tasks, repeat_percentage, step)
        self.output1.setText(str(out1))
        self.output2.setText(str(out2))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
