# Дата и время
from datetime import datetime
from time import time

# Фреймворк Flask
from flask import Flask, request, abort

# функции
from utils import unique_users, bot_command_check

# Валидация данных
import validation
from pydantic import ValidationError


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

app = Flask(__name__)


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
        'time': datetime.fromtimestamp(time())
    }


@app.route("/send", methods=['POST'])
def send_msg():
    json = request.json

    try:
        data = validation.Message.parse_obj(json)
    except ValidationError:
        abort(400)
        return {'ok': False}

    sender = data.sender
    message = data.message

    db.append({
        'sender': sender,  # отправитель
        'message': message,  # сообщение
        'time': time()  # время
    })

    # Проверка сообщения на команду.
    bot_command_check(message, sender, db)

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
    json = request.json
    try:
        data = validation.AccountLogIn.parse_obj(json)
    except ValidationError:
        abort(400)
        return {'ok': False}

    for acc in acc_db:
        if acc['login'] == data.login:
            if acc['password'] == data.password:
                return {'ok': True}

    abort(400)
    return {'ok': False}


@app.route("/registration", methods=['POST'])
def sign_up():
    json = request.json

    try:
        data = validation.AccountDb.parse_obj(json)
    except ValidationError:
        abort(400)
        return {'ok': False}

    if data.login in [dictionary['login'] for dictionary in acc_db]:
        abort(406)

    else:
        acc_db.append({
            'first_name': data.first_name,
            'second_name': data.second_name,
            'country': data.country,
            'birthday': data.birthday,
            'login': data.login,
            'password': data.password
        })
        return {'ok': True}

    abort(400)
    return {'ok': False}


if __name__ == "__main__":
    app.run()
