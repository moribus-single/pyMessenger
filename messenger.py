from datetime import datetime
from PyQt6 import QtWidgets, QtCore
import clientui
import requests as r


class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
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


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec()
