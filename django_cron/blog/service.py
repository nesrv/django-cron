import json
from django.core.files import File
import datetime
from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Сообщение',
        'n4tanan@yandex.ru',
        [user_email],
        fail_silently=False,
    )



# def send(user_email):
#     f = open(f'./emails.txt', 'a')
#     testfile = File(f)
#     testfile.write(str(datetime.datetime.now()) + "  " + user_email + '\n')
#     testfile.close()
#     f.close()


# def save_categories(data):
#     with open(f'./categories.json', 'a') as file:
#         json.dump(data, file)
