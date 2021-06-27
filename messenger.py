from datetime import datetime
from PyQt6 import QtWidgets, QtCore
from gui import chatUI
from gui import loginUI
import requests as r


class MainWindow(QtWidgets.QMainWindow, chatUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.after = 0
        # to run on button click
        self.pushButton.pressed.connect(self.send_msg)

        # to run by timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_msg)
        self.timer.start(1000)

    def show_msg(self, messages):
        for msg in messages:
            dt = datetime.fromtimestamp(msg['time'])
            dt = dt.strftime('%d.%m %H:%M')

            self.textBrowser.append(msg['sender'] + ' ' + 'to' + ' ' + msg['recipient'] + ' ' + dt)
            self.textBrowser.append(msg['message'] + '\n')

    def get_msg(self):
        try:
            result = r.get(
                'http://127.0.0.1:5000/messages',
                params={'after': self.after}
            )
        except:
            return

        msgs = result.json()['messages']
        if len(msgs) > 0:
            self.show_msg(msgs)
            self.after = msgs[-1]['time']

    def send_msg(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()

        try:
            result = r.post(
                'http://127.0.0.1:5000/send',
                json={'sender': name, 'message': text, 'recipient': 'Terminal'}
            )
        except:
            self.textBrowser.append('Сервер недоступен!')
            self.textBrowser.append('')
            return

        if result.status_code != 200:
            self.textBrowser.append('Недостаточно данных!')
            self.textBrowser.append('')
            return
        self.textEdit.clear()


class LoginForm(QtWidgets.QMainWindow, loginUI.Ui_MainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.log_in)
        self.mainwindow = mainwindow

    def log_in(self):
        login = self.lineEdit_2.text()
        password = self.lineEdit.text()

        try:
            result = r.post(
                'http://127.0.0.1:5000/login',
                json={'login': login, 'password': password}
            )
        except:
            self.label_2.setStyleSheet("color: #FF8C00;")
            self.label_2.setText('Server do not respond.')
            self.plainTextEdit.clear()
            self.plainTextEdit_2.clear()
            return

        if result.status_code != 200:
            print(f'Login - {login}\nPassword - {password}\nStatus Code - {result.status_code}')
            self.label_2.setStyleSheet("color: #FF4500;")
            self.label_2.setText('Invalid login or password.')
        else:
            self.label_2.clear()
            self.close()

            self.mainwindow.show()
            # TODO: закрепить username справа сверху mainwindow
            # TODO: Добавить окно регистрации
            # TODO: добавить чаты в каждый аккаунт с возможностью сохранения.
            app.exec()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MainWindow()
    login = LoginForm(window)

    login.show()
    app.exec()
