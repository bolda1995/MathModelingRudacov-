import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QGridLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from lab3 import *

class MainWindow(QMainWindow,QWidget):
    def __init__(self):

        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1300, 600))
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com")
        self.init_table()
        self.init_but()


        self.firstbutton.setGeometry(615, 50, 70, 25)

    def init_table(self):

        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)
        self.tableWidget = QTableWidget()
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)

        self.table = QTableWidget(self)  # Создаём таблицу
        self.table.setColumnCount(10)  # Устанавливаем три колонки
        self.table.setRowCount(10)
        self.table.setHorizontalHeaderLabels(["" for i in range(10)])
        for i in range(10):
            self.table.horizontalHeaderItem(i).setToolTip("0")
        for i in range(10):
            self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)
            self.table.resizeColumnsToContents()

        grid_layout.addWidget(self.table, 0, 0)

    def result(self):
        matrix = []
        text = [i for i in self.line.text().split()]
        for i in range(int(text[0])):
            a = []
            for j in range(int(text[0])):
                a.append(int(self.table.item(i,j).text()))
            matrix.append(a)
        length = len(matrix)
        prob = FindProb(matrix, length)
        prob.solve_probiliti()
        t = ""
        for i in prob.calc_stabilization_times():
            t += str(i)+" "
        self.line1.setText(t)

    def init_but(self):
        self.line = QLineEdit(self)
        self.line.setGeometry(870, 10, 50, 30)
        passwordLabel = QLabel('введите размерность матрицы размерность матрицы', self)
        passwordLabel.setGeometry(640, 5, 220, 30)
        self.firstbutton = QPushButton('ввод', self)
        self.firstbutton.clicked.connect(self.result)
        self.firstbutton.setGeometry(870, 30, 50, 30)
        self.line1 = QLineEdit(self)
        self.line1.setGeometry(650, 80, 500, 30)



















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
