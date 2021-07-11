from datetime import datetime
from PyQt6 import QtWidgets, QtCore
from gui import chatUI
from gui import loginUI
from gui import registrationUI
import requests as r


class MainWindow(QtWidgets.QMainWindow, chatUI.Ui_MainWindow):
    def __init__(self, user_login):
        super().__init__()
        self.setupUi(self)
        self.user_login = user_login
        self.label.setText(user_login)  # Логин слева сверху
        self.after = 0
        # to run on button click
        self.pushButton.pressed.connect(self.send_msg)
        self.pushButton_2.pressed.connect(self.close_window)

        # to run by timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_msg)
        self.timer.start(1000)

    def show_msg(self, messages):
        for msg in messages:
            dt = datetime.fromtimestamp(msg['time'])
            dt = dt.strftime('%d.%m %H:%M')

            self.textBrowser.append(msg['sender'] + ' ' + dt + ':')
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
        name = self.user_login
        text = self.textEdit.toPlainText()
        print(f'Login - {self.user_login}\nMessage - {text}\n')

        try:
            result = r.post(
                'http://127.0.0.1:5000/send',
                json={'sender': name, 'message': text}
            )
        except:
            self.textBrowser.append('Сервер недоступен!\n')
            return

        if result.status_code != 200:
            print(f'Status code - {result.status_code}')
            self.textBrowser.append('Недостаточно данных!\n')
            return

        self.textEdit.clear()

    def close_window(self):
        self.close()


class LoginForm(QtWidgets.QMainWindow, loginUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.log_in)
        self.pushButton_2.pressed.connect(self.close_window)
        self.pushButton_3.pressed.connect(self.sign_up)

        self.register_window = RegistrationForm(self)

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
            self.label_2.setStyleSheet("color: #FF4500;")
            self.label_2.setText('Invalid login or password.')
        else:
            self.label_2.clear()
            self.close()

            self.main_window = MainWindow(login)
            self.main_window.show()
            # TODO: убрать пробелы с краев сообщений ( strip() )
            # TODO: привести в порядок отображение сообщений в main_window
            # TODO: добавить чаты в каждый аккаунт с возможностью сохранения.
            app.exec()

    def sign_up(self):
        self.close()
        self.register_window.show()
        app.exec()

    def close_window(self):
        self.close()


class RegistrationForm(QtWidgets.QMainWindow, registrationUI.Ui_MainWindow):
    def __init__(self, login_form):
        super().__init__()
        self.setupUi(self)
        self.login_form = login_form
        self.pushButton.pressed.connect(self.sign_up)
        self.pushButton_2.pressed.connect(self.close_window)

    def clear_fields(self):
        self.lineEdit.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_6.clear()

    def sign_up(self):
        first_name = self.lineEdit_2.text()
        second_name = self.lineEdit.text()
        country = self.lineEdit_5.text()
        birthday = self.dateEdit.text()
        login = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        password2 = self.lineEdit_6.text()

        if password != password2:
            self.label_2.setText('Passwords do not match')
            return

        else:

            try:
                result = r.post(
                    'http://127.0.0.1:5000/registration',
                    json={
                        'first_name': first_name,
                        'second_name': second_name,
                        'country': country,
                        'birthday': birthday,
                        'login': login,
                        'password': password
                    }
                )
            except:
                print(f'STATUS CODE: {r.status_codes}')
                return

        self.clear_fields()

        if result.status_code != 400:
            self.close()
            self.login_form.show()
            app.exec()

    def close_window(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    login = LoginForm()
    # register = RegistrationForm(login)

    login.show()
    app.exec()
