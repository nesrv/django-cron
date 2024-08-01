from celery import shared_task
# from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
from django_cron.celery import app



COUNTER = 0

@shared_task
def first_task():
    global COUNTER
    COUNTER +=1
    print(f'first-task {COUNTER}')

@shared_task
def second_task():
    global COUNTER
    COUNTER +=1
    print(f'second-task {COUNTER}')


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


# @app.task()
# def write_file(email):
#     send(email)
#     return True

