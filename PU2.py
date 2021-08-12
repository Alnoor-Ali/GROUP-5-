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

class Ui_PU2(object):
    def notfound(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Error1()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def setupUi(self, Pet):
        Pet.setObjectName("Pet")
        Pet.resize(327, 307)
        Pet.setStyleSheet("background-color: rgb(255, 179, 71);")
        self.pushButton_4 = QtWidgets.QPushButton(Pet)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 270, 75, 23))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: Pet.close())

        self.pushButton_3 = QtWidgets.QPushButton(Pet)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 270, 75, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.proceed)
        self.pushButton_3.clicked.connect(lambda :Pet.close())


        self.lineEdit_4 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 140, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.dateEdit = QtWidgets.QDateEdit(Pet)
        self.dateEdit.setGeometry(QtCore.QRect(150, 230, 161, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")

        self.label_6 = QtWidgets.QLabel(Pet)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Pet)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_5 = QtWidgets.QLabel(Pet)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEdit_2 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_8 = QtWidgets.QLabel(Pet)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.lineEdit_5 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 170, 161, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 200, 161, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.label_9 = QtWidgets.QLabel(Pet)
        self.label_9.setGeometry(QtCore.QRect(20, 200, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Pet)
        self.label_10.setGeometry(QtCore.QRect(20, 230, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(Pet)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.comboBox = QtWidgets.QComboBox(Pet)
        self.comboBox.setGeometry(QtCore.QRect(150, 50, 161, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")

        self.lineEdit = QtWidgets.QLineEdit(Pet)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 121, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.label_12 = QtWidgets.QLabel(Pet)
        self.label_12.setGeometry(QtCore.QRect(20, 110, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.lineEdit_3 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 110, 161, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton_5 = QtWidgets.QPushButton(Pet)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 20, 31, 23))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.search_customer)

        self.comboBox.currentIndexChanged.connect(self.update)
        self.true()

        self.retranslateUi(Pet)
        QtCore.QMetaObject.connectSlotsByName(Pet)

    def update(self):
        try:
            self.check_pet_ID()
            self.check_pet_name()
            self.check_type()
            self.check_breed()
            self.check_gender()
            self.check_date()
        except:
            pass

    def true(self):
        self.comboBox.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        self.lineEdit_6.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.dateEdit.setDisabled(True)

    def false(self):
        self.comboBox.setDisabled(False)
        self.lineEdit_2.setDisabled(False)
        self.lineEdit_4.setDisabled(False)
        self.lineEdit_5.setDisabled(False)
        self.lineEdit_6.setDisabled(False)
        self.pushButton_3.setDisabled(False)
        self.dateEdit.setDisabled(False)

    def clear(self):
        self.lineEdit_5.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_6.clear()

    def search_customer(self):
        self.pushButton_5.disconnect()
        self.comboBox.clear()
        self.search = self.lineEdit.text()
        self.lineEdit_3.clear()
        if self.search == '':
            self.notfound()
            self.true()
            self.clear()

        else:
            query = f"SELECT * FROM `customer` WHERE `customer_name` = '{self.search}'"
            mycursor.execute(query)

            result = mycursor.fetchone()

            if result == None:
                self.notfound()
                self.true()
                self.clear()

            else:
                self.false()
                self.check_pets_list()
                self.update()
        self.pushButton_5.clicked.connect(self.search_customer)


    def check_pet_ID(self):
        self.pet_name = self.comboBox.currentText()
        query = f"SELECT `pet_ID` FROM `pet` WHERE `pet_name` = '{self.pet_name}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_3.setText(status)

    def check_pet_name(self):
        self.pet_name = self.comboBox.currentText()
        self.lineEdit_2.setText(self.pet_name)

    def check_type(self):
        self.pet_name = self.comboBox.currentText()
        query = f"SELECT `type_of_animal` FROM `pet` WHERE `pet_name` = '{self.pet_name}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_4.setText(status)

    def check_breed(self):
        self.pet_name = self.comboBox.currentText()
        query = f"SELECT `breed` FROM `pet` WHERE `pet_name` = '{self.pet_name}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_5.setText(status)

    def check_gender(self):
        self.pet_name = self.comboBox.currentText()
        query = f"SELECT `gender` FROM `pet` WHERE `pet_name` = '{self.pet_name}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_6.setText(status)

    def check_date(self):
        self.pet_name = self.comboBox.currentText()
        query = f"SELECT DATE(`birthday`) FROM `pet` WHERE `pet_name` = '{self.pet_name}'"
        mycursor.execute(query)
        dates = mycursor.fetchone()
        new_date = dates[0]
        self.dateEdit.setDate(new_date)

    def check_pets_list(self):
        query = f"SELECT `pet_name` FROM `pet` WHERE `customer_name` = '{self.search}'"
        mycursor.execute(query)
        records = mycursor.fetchall()

        for row in records:
            content = row[0]
            self.comboBox.addItem(content)

    def proceed(self):
        self.name = self.lineEdit_2.text()
        self.code = self.lineEdit_3.text()
        self.type = self.lineEdit_4.text()
        self.breed = self.lineEdit_5.text()
        self.gender = self.lineEdit_6.text()
        self.date = self.dateEdit.date().toPyDate()

        code = self.code
        name = self.name
        type = self.type
        breed = self.breed
        gender = self.gender
        date = self.date


        query2 = f"UPDATE `pet` SET `pet_ID` = '{code}', `pet_name` = '{name}', `type_of_animal` = '{type}', `breed` = '{breed}', `gender` = '{gender}', `birthday` = '{date}' WHERE `pet_ID` = '{code}'"
        mycursor.execute(query2)
        db.commit()

    def retranslateUi(self, Pet):
        _translate = QtCore.QCoreApplication.translate
        Pet.setWindowTitle(_translate("Pet", "Pet UPDATE"))
        self.pushButton_4.setText(_translate("Pet", "Cancel"))
        self.pushButton_3.setText(_translate("Pet", "OK"))
        self.label_6.setText(_translate("Pet", "Pet List:"))
        self.label_7.setText(_translate("Pet", "Type of Animal:"))
        self.label_5.setText(_translate("Pet", "Breed:"))
        self.label_8.setText(_translate("Pet", "Pet Name:"))
        self.label_9.setText(_translate("Pet", "Gender:"))
        self.label_10.setText(_translate("Pet", "Birthday:"))
        self.label_11.setText(_translate("Pet", "Search Customer:"))
        self.label_12.setText(_translate("Pet", "Pet ID:"))
        self.pushButton_5.setText(_translate("Pet", "Go"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pet = QtWidgets.QDialog()
    ui = Ui_PU2()
    ui.setupUi(Pet)
    Pet.show()
    sys.exit(app.exec_())
