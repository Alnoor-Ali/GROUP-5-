from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from pet_add import Ui_Pet_ADD
from PU2 import Ui_PU2
from PD2 import  Ui_PD2
from notfound import Ui_Error1
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor()

class Ui_Pets(object):
    def Main_menu(self):
        from main_menu import Ui_Main
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()

    def add_pet(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Pet_ADD()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def update_pet(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_PU2()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def delete_pet(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_PD2()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def notfound(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Error1()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def setupUi(self, Pets):
        Pets.setObjectName("Appointments")
        Pets.resize(1600, 900)
        Pets.setStyleSheet("background-color: rgb(255, 179, 71);")
        self.centralwidget = QtWidgets.QWidget(Pets)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1300, 20, 600, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "color: rgb(255, 249, 215);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fill_table)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1300, 90, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 161, 148);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.update_pet)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1450, 90, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 133, 122);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.delete_pet)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1150, 90, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 238, 210);\n"
                                        "background-color: rgb(174, 255, 170);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.add_pet)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(253, 255, 230);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.search_customer)

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 238, 210);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(138, 118, 107);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.Main_menu)
        self.pushButton_9.clicked.connect(lambda: Pets.close())

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 1560, 850))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 90, 351, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        Pets.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Pets)
        self.statusbar.setObjectName("statusbar")
        Pets.setStatusBar(self.statusbar)

        self.retranslateUi(Pets)
        QtCore.QMetaObject.connectSlotsByName(Pets)

        self.fill_table()

    def update(self):
        self.fill_table()

    def search_customer(self):
        search = self.lineEdit.text()
        self.lineEdit.clear()
        if search == '':
            self.notfound()
        else:
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Pet ID"))
            self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Pet Name"))
            self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Type of Animal"))
            self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Breed"))
            self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Gender"))
            self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem("Birthday"))
            self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem("Customer"))

            query = f"SELECT * FROM `pet` WHERE `customer_name` = '{search}'"
            mycursor.execute(query)

            result = mycursor.fetchall()

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            db.commit()

            try:
                self.tableWidget.setRowCount(row_number + 1)
            except:
                if result == None:
                    self.tableWidget.setRowCount(0)
                self.notfound()
                print("Empty")
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)

    def fill_table(self):
        self.pushButton.disconnect()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Pet ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Pet Name"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Type of Animal"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Breed"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Gender"))
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem("Birthday"))
        self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem("Customer"))

        mycursor.execute("SELECT * FROM `pet` ORDER BY `pet_name`")

        result = mycursor.fetchall()
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.commit()

        try:
            self.tableWidget.setRowCount(row_number + 1)
        except:
            self.tableWidget.setRowCount(0)
            print("Empty")
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        self.pushButton.clicked.connect(self.fill_table)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Appointments", "Appointments"))
        self.label.setToolTip(_translate("Appointments", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setWhatsThis(_translate("Appointments", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("Appointments", "Pets Data"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_6.setText(_translate("Appointments", "Update"))
        self.pushButton_5.setText(_translate("Appointments", "Delete"))
        self.pushButton_4.setText(_translate("Appointments", "Add"))
        self.pushButton_7.setText(_translate("Appointments", "Search "))
        self.pushButton_9.setText(_translate("Appointments", "Back to Main Menu"))
        self.label_2.setText(_translate("Appointment", "SEARCH CUSTOMER:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Pets()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
