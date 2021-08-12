from PyQt5 import QtCore, QtGui, QtWidgets
from appointment import Ui_Appointment
from customer import Ui_Customer
from pets import Ui_Pets
from logout import Ui_dialog


class Ui_Main(object):
    def logout(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_dialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def appointment(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Appointment()
        self.ui.setupUi(self.window)
        self.window.show()

    def customer(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Customer()
        self.ui.setupUi(self.window)
        self.window.show()

    def pets(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Pets()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Appointments")
        MainWindow.resize(675, 382)
        MainWindow.setStyleSheet("background-color: rgb(255, 179, 71);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 175, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.appointment)
        self.pushButton.clicked.connect(lambda :MainWindow.close())

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 150, 175, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 221, 158);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.customer)
        self.pushButton_2.clicked.connect(lambda: MainWindow.close())

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 220, 175, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pets)
        self.pushButton_3.clicked.connect(lambda: MainWindow.close())

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(525, 330, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 223, 158);\n"
                                        "font: 75 8pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.logout)
        self.pushButton_4.clicked.connect(lambda :MainWindow.close())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 90, 275, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 170, 275, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 230, 180, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Appointments", "Appointments"))
        self.pushButton.setText(_translate("Appointments", "Appointments"))
        self.pushButton_2.setText(_translate("Appointments", "Customers"))
        self.pushButton_3.setText(_translate("Appointments", "Pets"))
        self.pushButton_4.setText(_translate("Appointments", "LOG OUT"))
        self.label.setText(_translate("Appointments", "FurryFood "))
        self.label_2.setText(_translate("Appointments", " Database"))
        self.label_3.setText(_translate("Appointments", "-Main Menu-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
