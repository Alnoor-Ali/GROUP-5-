
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Not(object):
    def setupUi(self, empty):
        empty.setObjectName("empty")
        empty.resize(173, 88)
        empty.setStyleSheet("background-color: rgb(255, 161, 148);")
        self.label = QtWidgets.QLabel(empty)
        self.label.setGeometry(QtCore.QRect(15, 20, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(empty)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda :empty.close())

        self.retranslateUi(empty)
        QtCore.QMetaObject.connectSlotsByName(empty)

    def retranslateUi(self, Error1):
        _translate = QtCore.QCoreApplication.translate
        Error1.setWindowTitle(_translate("empty", "Dialog"))
        self.label.setText(_translate("empty", "Fields are empty!"))
        self.pushButton.setText(_translate("empty", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error1 = QtWidgets.QDialog()
    ui = Ui_Not()
    ui.setupUi(Error1)
    Error1.show()
    sys.exit(app.exec_())
