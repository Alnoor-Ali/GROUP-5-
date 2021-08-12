from PyQt5 import QtCore, QtGui, QtWidgets
from notfound import Ui_Error1
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor()


class Ui_CD2(object):
    def notfound(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Error1()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def setupUi(self, Customer):
        Customer.setObjectName("Customer")
        Customer.resize(329, 225)
        Customer.setStyleSheet("background-color: rgb(255, 179, 71);")
        self.label = QtWidgets.QLabel(Customer)
        self.label.setGeometry(QtCore.QRect(10, 30, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(Customer)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(Customer)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(Customer)
        self.pushButton.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.proceed)
        self.pushButton.clicked.connect(lambda: Customer.close())

        self.pushButton_2 = QtWidgets.QPushButton(Customer)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda :Customer.close())

        self.label_4 = QtWidgets.QLabel(Customer)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.dateEdit = QtWidgets.QDateEdit(Customer)
        self.dateEdit.setGeometry(QtCore.QRect(160, 150, 161, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Customer)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 90, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_4 = QtWidgets.QLineEdit(Customer)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 120, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_3 = QtWidgets.QLineEdit(Customer)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 30, 121, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(Customer)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 30, 31, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.search_customer)

        self.label_5 = QtWidgets.QLabel(Customer)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(Customer)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 60, 161, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Customer)
        QtCore.QMetaObject.connectSlotsByName(Customer)

        self.lineEdit_5.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.dateEdit.setDisabled(True)
        self.pushButton.setDisabled(True)



    def clear(self):
        self.lineEdit_5.clear()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()

    def search_customer(self):
        self.pushButton_3.disconnect()
        self.search = self.lineEdit_3.text()
        self.lineEdit_3.clear()
        if self.search == '':
            self.notfound()
            self.clear()

        else:
            query = f"SELECT * FROM `customer` WHERE `customer_name` = '{self.search}'"
            mycursor.execute(query)

            result = mycursor.fetchone()
            print(result)

            if result == None:
                self.notfound()
                print("not")
                self.clear()
                self.pushButton.setDisabled(True)

            else:
                print("have")
                self.check_name()
                self.check_number()
                self.check_name()
                self.check_ID()
                self.pushButton.setDisabled(False)
        self.pushButton_3.clicked.connect(self.search_customer)

    def check_ID(self):
        query = f"SELECT `customer_ID` FROM `customer` WHERE `customer_name` = '{self.search}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_5.setText(status)

    def check_name(self):
        query = f"SELECT `customer_name` FROM `customer` WHERE `customer_name` = '{self.search}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_2.setText(status)

    def check_number(self):
        query = f"SELECT `contact_number` FROM `customer` WHERE `customer_name` = '{self.search}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = str(status[0])
        self.lineEdit_4.setText(status)

    def check_date(self):
        query = f"SELECT DATE(`birthday`) FROM `customer` WHERE `customer_name` = '{self.search}'"
        mycursor.execute(query)
        dates = mycursor.fetchone()
        new_date = dates[0]
        self.dateEdit.setDate(new_date)

    def proceed(self):
        self.code = self.lineEdit_5.text()

        query2 = f"DELETE FROM `customer` WHERE `customer_ID` = '{self.code}'"
        mycursor.execute(query2)
        db.commit()

    def retranslateUi(self, Customer):
        _translate = QtCore.QCoreApplication.translate
        Customer.setWindowTitle(_translate("Customer", "Customer DELETE"))
        self.label.setText(_translate("Customer", "Search Customer:"))
        self.label_3.setText(_translate("Customer", "Customer Number:"))
        self.label_2.setText(_translate("Customer", "Customer Name:"))
        self.pushButton.setText(_translate("Customer", "OK"))
        self.pushButton_2.setText(_translate("Customer", "Cancel"))
        self.label_4.setText(_translate("Customer", "Customer Birthday:"))
        self.pushButton_3.setText(_translate("Customer", "Go"))
        self.label_5.setText(_translate("Customer", "Customer ID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Customer = QtWidgets.QDialog()
    ui = Ui_CD2()
    ui.setupUi(Customer)
    Customer.show()
    sys.exit(app.exec_())