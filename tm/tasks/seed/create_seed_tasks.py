import random
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group, Permission

from tasks.models import TasksModel

titles = [
    'Проверить почту',
    'Подготовить отчёт',
    'Провести собрание',
    'Связаться с клиентом'
]


def create_user_groups():
    group_1, _ = Group.objects.get_or_create(name='employee')
    group_1.permissions.set(
        Permission.objects.filter(codename__endswith='tasksmodel')
    )

    group_1.save()

    group_2, _ = Group.objects.get_or_create(name='admin')
    group_2.permissions.set(
        Permission.objects.filter(codename__in=[
            'view_tasksmodel',
            'change_tasksmodel',
        ])
    )

    group_2.save()


def create_base_users():
    password = make_password('password1')

    user_model = get_user_model()

    admin_group = Group.objects.get(name='admin')
    employee_group = Group.objects.get(name='employee')

    # super_user = User.objects.create_user(
    #     'admin',
    #     password=password,
    # )
    #
    # super_user.is_superuser = True
    # super_user.is_staff = True
    #
    # super_user.save()

    admin = user_model.objects.create(
        username='max_demax',
        first_name='Максим',
        last_name='Демах',
        password=password,
    )

    admin.groups.add(admin_group)

    employee_1 = user_model.objects.create_user(
        username='egrazor',
        first_name='Егор',
        last_name='Зенкин',
        password=password,
    )

    employee_1.groups.add(employee_group)

    employee_2 = user_model.objects.create_user(
        username='zarina',
        first_name='Зарина',
        last_name='Каримова',
        password=password,
    )

    employee_2.groups.add(employee_group)

    employee_3 = user_model.objects.create_user(
        username='zenderg',
        first_name='Данила',
        last_name='Кузин',
        password=password,
    )

    employee_3.groups.add(employee_group)

    employee_4 = user_model.objects.create_user(
        username='zenderg',
        first_name='Данила',
        last_name='Кузин',
        password=password,
    )

    employee_4.groups.add(employee_group)

    employee_5 = user_model.objects.create_user(
        username='ivan',
        first_name='Иван',
        last_name='Ерёменко',
        password=password,
    )

    employee_5.groups.add(employee_group)


def create_seed_tasks():
    for employee in User.objects.filter(
            groups__name='employee'
    ):
        TasksModel.objects.create(
            title=random.choice(titles),
            deadline=datetime.now() + timedelta(days=random.choice(range(10))),
            executor_id=employee.id
        )
