# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 402)

        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        MainWindow.setMinimumSize(QtCore.QSize(301, 402))
        MainWindow.setMaximumSize(QtCore.QSize(301, 402))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 301, 401))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(95, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(24, 272, 251, 41))
        self.pushButton.setMinimumSize(QtCore.QSize(251, 41))
        self.pushButton.setMaximumSize(QtCore.QSize(251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 225, 141, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 189, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(70, 130, 180, 1);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;\n"
"\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(70, 130, 180, 1);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;\n"
"\n"
"")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(32769)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Log In"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Username"))
