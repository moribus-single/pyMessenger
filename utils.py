from time import time
from datetime import datetime


def clean_msg(text: str) -> str:
    """cleaning from excess gaps, new lines and tabs."""
    tmp = list(text.strip())
    flag = True

    while flag:
        for i in range(len(tmp)):

            if tmp[i] == ' ' and tmp[i + 1] == ' ' or tmp[i] == '\n' and tmp[i + 1] == '\n' or tmp[i] == '\t':
                tmp.pop(i)
                break

            if i == len(tmp) - 1:
                flag = False

    return "".join(tmp)


def unique_users(db: list) -> int:
    """Подчет уникальных пользователей"""
    names = [elem['login'] for elem in db]
    names = set(names)

    return len(names)


def bot_command_check(msg: str, sender: str, db: list) -> None:
    """Проверка сообщения на команду"""
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
