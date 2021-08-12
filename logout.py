from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_MainWindow


class Ui_dialog(object):
    def main(self):
        from main_menu import Ui_Main
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()

    def out(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(275, 100)
        dialog.setStyleSheet("background-color: rgb(255, 161, 148);")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 250, 20))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 61, 20))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.out)
        self.pushButton.clicked.connect(lambda :dialog.close())

        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 50, 61, 20))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.main)
        self.pushButton_2.clicked.connect(lambda :dialog.close())

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Warning"))
        self.label.setText(_translate("dialog", "Are you sure you want to log out?"))
        self.pushButton.setText(_translate("dialog", "Yes"))
        self.pushButton_2.setText(_translate("dialog", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
