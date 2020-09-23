<h2>Django_business_logic</h2>
<hr>

***Проект про то, как и где хранить бизнес-логику***
***в Django***

Для запуска проекта сделать следующее:

1. Создать виртуальное окружение:
    
    `python3 -m venv venv`
    
2. Настроить БД:

    `'ENGINE': 'django.db.backends.postgresql_psycopg2', `
    `'NAME': 'db_name',`<br>
    `'USER': 'user_name',`<br>
    `'PASSWORD': 'password',`<br>
    `'HOST': '127.0.0.1',`<br>
    `'PORT': '5432',`

3. Создать переменные окружения, данные в *settings.py*

4. Выполнить миграции: 
    
    `python manage.py makemigrations`
    
    `python manage.py migrate`
    
5. Запускаем проект: 
    
    `python manage.py runserver`
    
    
