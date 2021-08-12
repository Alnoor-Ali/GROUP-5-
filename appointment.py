from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlQueryModel
from appointment_add import Ui_Appointment_ADD
from AU import Ui_Appointment_UPDATE
from AD import Ui_Appointment_DELETE
from notfound import Ui_Error1
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor()

class Ui_Appointment(object):
    def Main_menu(self):
        from main_menu import Ui_Main
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()

    def add_appointment(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Appointment_ADD()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def update_appointment(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Appointment_UPDATE()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def delete_appointment(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Appointment_DELETE()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def notfound(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Error1()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def setupUi(self, Appointment):
        Appointment.setObjectName("Appointment")
        Appointment.resize(1600, 900)
        Appointment.setStyleSheet("background-color: rgb(255, 179, 71);")
        self.centralwidget = QtWidgets.QWidget(Appointment)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fill_table)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1150, 90, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 238, 210);\n"
                                        "background-color: rgb(174, 255, 170);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.add_appointment)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1300, 90, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 161, 148);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.update_appointment)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1450, 90, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 133, 122);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.delete_appointment)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(253, 255, 230);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.search_customer)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 238, 210);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(138, 118, 107);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.Main_menu)
        self.pushButton_8.clicked.connect(lambda: Appointment.close())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1050, 10, 900, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "color: rgb(255, 249, 215);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 1560, 850))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")

        self.table = QSqlQueryModel()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton.setObjectName("pushButton")

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

        Appointment.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Appointment)
        self.statusbar.setObjectName("statusbar")
        Appointment.setStatusBar(self.statusbar)

        self.retranslateUi(Appointment)
        QtCore.QMetaObject.connectSlotsByName(Appointment)

        self.fill_table()

    def search_customer(self):
        search = self.lineEdit.text()
        self.lineEdit.clear()
        if search == '':
            self.notfound()
        else:
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Appointment ID"))
            self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Appointment Date"))
            self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Appointment Status"))
            self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Customer"))

            query = f"SELECT * FROM `appointment` WHERE `customer_name` = '{search}'"
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
                print("Empty")
                self.notfound()
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def fill_table(self):
        self.pushButton.disconnect()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Appointment ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Appointment Date"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Appointment Status"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Customer"))

        mycursor.execute("SELECT * FROM `appointment` ORDER BY `appointment_ID`")

        result = mycursor.fetchall()
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.commit()

        try:
            self.tableWidget.setRowCount(row_number + 1)
        except:
            print("Empty")
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.pushButton.clicked.connect(self.fill_table)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Appointment", "Appointment"))
        self.pushButton.setText(_translate("Appointment", "Refresh"))
        self.pushButton_4.setText(_translate("Appointment", "Add"))
        self.pushButton_6.setText(_translate("Appointment", "Update"))
        self.pushButton_5.setText(_translate("Appointment", "Delete"))
        self.pushButton_7.setText(_translate("Appointment", "Search "))
        self.pushButton_8.setText(_translate("Appointment", "Back to Main Menu"))
        self.label.setToolTip(_translate("Appointment", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setWhatsThis(_translate("Appointment", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("Appointment", "Appointments Data"))
        self.pushButton.setText(_translate("Appointment", "Refresh"))
        self.label_2.setText(_translate("Appointment", "SEARCH CUSTOMER:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Appointment()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
