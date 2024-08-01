# Demo project Celery + Django

## first

```sh
pip install django celery redis
django-admin startproject django_cron
sudo apt install redis-server
python manage.py startapp blog
```

### Linux

```sh
sudo apt install python3.11-venv
python3 -m venv venv
source venv/bin/activate
pip install django celery redis
pip freeze > requirements.txt
sudo apt install redis-server
django-admin startproject django_cron

python manage.py startapp blog

pip install -r requirements.txt 
python3 manage.py runserver
```


### Windows

```sh
python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt 
python manage.py runserver
python manage.py makemigrations
```


```sh
docker run -p 127.0.0.1:16379:6379 --name redis-celery -d redis
```


### Redis for Linux

```sh
sudo service redis-server start
sudo service redis-server restart

```


### Celery for Linux

```sh
celery -A django_cron worker -B -l INFO
celery -A django_cron worker -l INFO
celery -A send_email worker -l info
```

### Celery for windows
```sh
celery -A django_cron worker -l INFO
celery -A send_email worker -l info
```


```sh
git remote rm origin
git remote add origin https://github.com/nesrv/celery_django.git


git reset venv
```




```sh
ssh -T git@github.com
```