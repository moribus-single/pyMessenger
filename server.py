from flask import Flask, request, abort
from datetime import datetime  # библиотеки для работы
from time import time  # со временем


def unique_users(obj):
    # подчет уникальных пользователей

    names = [elem['sender'] for elem in obj]
    names = set(names)

    return len(names)


def sum_msgs(obj):
    # подсчет кол-ва сообщений

    msgs = [elem['message'] for elem in obj]

    return len(msgs)


app = Flask(__name__)
db = [
    {
        'sender': 'Пшеничный',
        'recipient': 'Terminal',
        'message': 'По воле великого меня, да заработает сервер!',
        'time': 0.1
    },
    {
        'sender': 'Данил',
        'recipient': 'Terminal',
        'message': 'Иди стихи пиши, старый',
        'time': 0.2
    }
]


@app.route("/")
def hello():
    return "Hello, Messenger!"


@app.route("/stat")
def status():
    return {
        'status': True,
        'name': 'RMessenger',
        'unique-users': unique_users(db),
        'amount-of-messages': sum_msgs(db),
        'time': datetime.fromtimestamp(time())
    }


@app.route("/send", methods=['POST'])
def send_msg():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    if 'sender' not in data or 'message' not in data or 'recipient' not in data:
        return abort(400)

    sender = data['sender']
    recipient = data['recipient']
    message = data['message']

    if not isinstance(sender, str) or not isinstance(message, str) or not isinstance(recipient, str):
        return abort(400)
    if sender == '' or message == '' or recipient == '':
        print('ABORT')
        return abort(400)

    db.append({
        'sender': sender,  # отправитель
        'recipient': recipient,  # получатель
        'message': message,  # сообщение
        'time': time()  # время
    })

    if message == '/help':
        bot_msg = '/time - узнать время\n'
        db.append({
            'sender': 'bot4help',  # отправитель
            'recipient': sender,  # получатель
            'message': bot_msg,  # сообщение
            'time': time()  # время
        })

    if message == '/time':
        dt = datetime.fromtimestamp(time())
        bot_msg = 'Время на сервере  -  ' + dt.strftime('%d.%m %H:%M')
        db.append({
            'sender': 'bot4help',  # отправитель
            'recipient': sender,  # получатель
            'message': bot_msg,  # сообщение
            'time': time()  # время
        })

    return {'ok': True}


@app.route("/messages")
def get_msg():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    messages = []
    for msg in db:
        if msg['time'] > after:
            messages.append(msg)
    return {'messages': messages[:50]}


app.run()
