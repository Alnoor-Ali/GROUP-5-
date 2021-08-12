from PyQt5 import QtCore, QtGui, QtWidgets


def back(self):
    from customer import Ui_Customer
    self.window = QtWidgets.QMainWindow()
    self.ui = Ui_Customer()
    self.ui.setupUi(self.window)
    self.window.show()
class Ui_Error2(object):
    def setupUi(self, Error2):
        Error2.setObjectName("Error2")
        Error2.resize(300, 150)
        Error2.setStyleSheet("background-color: rgb(255, 161, 148);\n"
"background-color: rgb(199, 199, 199);")
        self.pushButton_2 = QtWidgets.QPushButton(Error2)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 75, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(Error2.close)

        
        self.label_2 = QtWidgets.QLabel(Error2)
        self.label_2.setGeometry(QtCore.QRect(55, 45, 300, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Error2)
        QtCore.QMetaObject.connectSlotsByName(Error2)

    def retranslateUi(self, Error2):
        _translate = QtCore.QCoreApplication.translate
        Error2.setWindowTitle(_translate("Error2", "Invalid"))
        self.pushButton_2.setText(_translate("Error2", "OK"))
        self.label_2.setText(_translate("Error2", "Customer ID already exist!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error2 = QtWidgets.QDialog()
    ui = Ui_Error2()
    ui.setupUi(Error2)
    Error2.show()
    sys.exit(app.exec_())
