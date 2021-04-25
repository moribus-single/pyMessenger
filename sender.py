import requests as r

name = input('Введите имя: ')

while True:

    result = r.post(
        'http://127.0.0.1:5000/send',
        json={'sender': name, 'message': input(), 'recipient': 'Terminal'}
    )


#print(result.json())
