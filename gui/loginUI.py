# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


import PyQt6
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 402)
        MainWindow.setMinimumSize(PyQt6.QtCore.QSize(301, 402))
        MainWindow.setMaximumSize(PyQt6.QtCore.QSize(301, 402))

        MainWindow.setWindowFlags(PyQt6.QtCore.Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(PyQt6.QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.centralwidget = PyQt6.QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = PyQt6.QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(PyQt6.QtCore.QRect(0, 0, 301, 401))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 255);")
        self.frame.setFrameShape(PyQt6.QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(PyQt6.QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = PyQt6.QtWidgets.QLabel(self.frame)
        self.label.setGeometry(PyQt6.QtCore.QRect(95, 40, 131, 51))
        font = PyQt6.QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = PyQt6.QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(PyQt6.QtCore.QRect(24, 272, 251, 41))
        self.pushButton.setMinimumSize(PyQt6.QtCore.QSize(251, 41))
        self.pushButton.setMaximumSize(PyQt6.QtCore.QSize(251, 41))
        font = PyQt6.QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(PyQt6.QtGui.QCursor(PyQt6.QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(32, 178, 170, 255), stop:0.55 rgba(0, 139, 139, 255), stop:0.98 rgba(0, 128, 129, 255), stop:1 rgba(70, 130, 180, 255));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(32, 178, 170, 200), stop:0.55 rgba(0, 139, 139, 200), stop:0.98 rgba(0, 128, 129, 200), stop:1 rgba(70, 130, 180, 200));\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(32, 178, 170, 255), stop:0.55 rgba(0, 139, 139, 255), stop:0.98 rgba(0, 128, 129, 255), stop:1 rgba(70, 130, 180, 255));\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = PyQt6.QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(PyQt6.QtCore.QRect(80, 225, 141, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = PyQt6.QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(PyQt6.QtCore.QRect(30, 189, 241, 31))
        font = PyQt6.QtGui.QFont()
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
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setEchoMode(PyQt6.QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = PyQt6.QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(PyQt6.QtCore.QRect(30, 130, 241, 31))
        font = PyQt6.QtGui.QFont()
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
        self.lineEdit_2.setMaxLength(12)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = PyQt6.QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(PyQt6.QtCore.QRect(285, 0, 16, 16))
        self.pushButton_2.setCursor(PyQt6.QtGui.QCursor(PyQt6.QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgba(255, 0, 0,255);\n"
"border: 1px solid rgb(193, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 0, 0,200);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 0, 0,255);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = PyQt6.QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(PyQt6.QtCore.QRect(105, 340, 91, 23))
        font = PyQt6.QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(PyQt6.QtGui.QCursor(PyQt6.QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet("border: none;")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        PyQt6.QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = PyQt6.QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sign In"))
        self.pushButton.setText(_translate("MainWindow", "Sign In"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Username"))
        self.pushButton_2.setText(_translate("MainWindow", "X"))
        self.pushButton_3.setText(_translate("MainWindow", "Create account"))
