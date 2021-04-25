import requests as r
from datetime import datetime
import time


def print_msg(messages):
    # функция вывода сообщений

    for msg in messages:
        dt = datetime.fromtimestamp(msg['time'])
        dt = dt.strftime('%d.%m %H:%M')
        print(msg['sender'], 'to', msg['recipient'], dt)
        print(msg['message'], '\n')


after = 0

while True:
    result = r.get(
        'http://127.0.0.1:5000/messages',
        params={'after': after}
    )
    msgs = result.json()['messages']
    if len(msgs) > 0:
        print_msg(msgs)
        after = msgs[-1]['time']

    time.sleep(1)
