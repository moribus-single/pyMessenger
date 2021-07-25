from flask import Flask, request, abort
from datetime import datetime  # библиотеки для работы
from time import time  # со временем


def unique_users(obj):
    # подчет уникальных пользователей

    names = [elem['login'] for elem in acc_db]
    names = set(names)

    return len(names)


def sum_msgs(obj):
    # подсчет кол-ва сообщений

    msgs = [elem['message'] for elem in obj]

    return len(msgs)


def bot_command_check(msg: str, sender: str):
    if msg == '/help':
        bot_msg = '/time - узнать время'
        db.append({
            'sender': 'bot4help',  # отправитель
            'recipient': sender,  # получатель
            'message': bot_msg,  # сообщение
            'time': time()  # время
        })

    if msg == '/time':
        dt = datetime.fromtimestamp(time())
        bot_msg = 'Время на сервере  -  ' + dt.strftime('%d.%m %H:%M')
        db.append({
            'sender': 'bot4help',  # отправитель
            'recipient': sender,  # получатель
            'message': bot_msg,  # сообщение
            'time': time()  # время
        })


app = Flask(__name__)

db = [
    {
        'sender': 'admin',
        'message': 'Я запустил мессенджер))0)',
        'time': 0.1
    }
]

acc_db = [
    {
        'login': 'danil01',
        'password': '12321qwqw'
    }
]


@app.route("/")
def hello():
    return "Hello, Messenger!"


@app.route("/admin")
def accounts():
    return {'info': acc_db}


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
    if 'sender' not in data or 'message' not in data:
        return abort(400)

    sender = data['sender']
    message = data['message']

    if not isinstance(sender, str) or not isinstance(message, str):
        return abort(400)
    if sender == '' or message == '':
        return abort(400)

    db.append({
        'sender': sender,  # отправитель
        'message': message,  # сообщение
        'time': time()  # время
    })

    # Проверка сообщения на команду.
    bot_command_check(message, sender)

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


@app.route("/login", methods=['POST'])
def login():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    if 'login' not in data or 'password' not in data:
        return abort(400)

    if not isinstance(data['login'], str) or not isinstance(data['password'], str):
        return abort(400)
    if data['login'] == '' or data['password'] == '':
        return abort(400)

    for acc in acc_db:
        if acc['login'] == data['login']:
            if acc['password'] == data['password']:
                return {'ok': True}

    abort(400)
    return {'ok': False}


@app.route("/registration", methods=['POST'])
def sign_up():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    if 'first_name' not in data or 'second_name' not in data or 'country' not in data or \
            'birthday' not in data or 'login' not in data or 'password' not in data:
        return abort(400)

    first_name = data['first_name']
    second_name = data['second_name']
    country = data['country']
    birthday = data['birthday']
    login = data['login']
    password = data['password']

    if not isinstance(data['first_name'], str) or \
            not isinstance(data['second_name'], str) or \
            not isinstance(data['country'], str) or \
            not isinstance(data['birthday'], str) or \
            not isinstance(data['login'], str) or \
            not isinstance(data['password'], str):
        return abort(400)

    if first_name == '' or \
            second_name == '' or \
            country == '' or \
            birthday == '' or \
            login == '' or \
            password == '':
        return abort(400)

    if login in [dictionary['login'] for dictionary in acc_db]:
        return abort(406)

    else:
        acc_db.append({
            'first_name': first_name,
            'second_name': second_name,
            'country': country,
            'birthday': birthday,
            'login': login,
            'password': password
        })

        return {'ok': True}

    abort(400)
    return {'ok': False}


if __name__ == "__main__":
    app.run()
