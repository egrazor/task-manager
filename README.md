# task-manager

Требования:
- python 3.9 и выше

Инструкция по развертыванию приложения:
1. Создать виртуальную среду: `task-manager/ > python3.9 venv -m venv`
2. Активировать виртуальную среду: `source task-manager/venv/bin/activate`
3. Перейти в каталог с приложением: `cd tm`
3. Установить зависимости: `python3 install -r requirements.txt`
5. Применить миграции БД: `python3 manage.py migrate`
6. (опционально) Заполнить БД тестовыми данными: `python3 manage.py seed` 
7. Запуск сервера: `python3 manage.py runserver`

Чтобы воспользоваться админ-панелью, создайте суперпользователя:
`python manage.py createsuperuser`

Далее, в админ-панели, можете создать всех членов команды
