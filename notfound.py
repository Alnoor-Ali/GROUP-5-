from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error1(object):
    def setupUi(self, Error1):
        Error1.setObjectName("Error1")
        Error1.resize(300, 150)
        Error1.setStyleSheet("background-color: rgb(255, 161, 148);")
        self.label = QtWidgets.QLabel(Error1)
        self.label.setGeometry(QtCore.QRect(40, 45, 300, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Error1)
        self.pushButton.setGeometry(QtCore.QRect(110, 75, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: Error1.close())

        self.retranslateUi(Error1)
        QtCore.QMetaObject.connectSlotsByName(Error1)

    def retranslateUi(self, Error1):
        _translate = QtCore.QCoreApplication.translate
        Error1.setWindowTitle(_translate("Error1", "!"))
        self.label.setText(_translate("Error1", "Customer name not found!"))
        self.pushButton.setText(_translate("Error1", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error1 = QtWidgets.QDialog()
    ui = Ui_Error1()
    ui.setupUi(Error1)
    Error1.show()
    sys.exit(app.exec_())
