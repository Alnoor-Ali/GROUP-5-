from PyQt5 import QtCore, QtGui, QtWidgets
from invalid import Ui_Invalid
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor(buffered=True)

class Ui_MainWindow(object):
    def menu(self):
        from main_menu import Ui_Main
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()
    def invalid(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Invalid()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Appointments")
        MainWindow.resize(335, 210)
        MainWindow.setStyleSheet("background-color: rgb(255, 179, 87);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 130, 101, 21))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.log)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 161, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 90, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def log(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        query = f"SELECT * FROM `user` WHERE `username` = '{username}' AND `password` = '{password}'"
        mycursor.execute(query)

        row = mycursor.fetchone()

        if username == '' or password == '':
            self.invalid()
        elif row != None:
            self.menu()
            MainWindow.close()
        else:
            self.invalid()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Appointments", "Log In"))
        self.pushButton.setText(_translate("Appointments", "Log in"))
        self.label_6.setText(_translate("Appointments", "USERNAME:"))
        self.label_7.setText(_translate("Appointments", "PASSWORD:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
