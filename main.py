from datetime import datetime  # библиотеки для работы
from time import time  # со временем

db = []  # база данных сообщений


def send_msg(sender, recipient, message):
    # функция отправки сообщений

    db.append({
        'sender': sender,  # отправитель
        'recipient': recipient,  # получатель
        'message': message,  # сообщение
        'time': time()  # время
    })


def print_msg(messages):
    # функция вывода базы данных

    for msg in messages:
        current_time = datetime.fromtimestamp(msg['time'])
        print(msg['sender'], 'to', msg['recipient'], current_time)
        print(msg['message'], '\n')


def get_msg(after):
    # функция вывода новых сообщений
    messages = []

    for msg in db:
        if msg['time'] > after:
            messages.append(msg)

    return messages[:50]


send_msg('Danil', 'Gordey', 'go progatt lox')

result = get_msg(0)
print_msg(result)
last_time = result[-1]['time']
print('LAST TIME --> ', last_time, sep=' ')

send_msg('Gordey', 'Danil', '.!.')
send_msg('Danil', 'Gordey', 'go ept')

result = get_msg(last_time)
print_msg(result)
last_time = result[-1]['time']
print('LAST TIME --> ', last_time, sep=' ')

