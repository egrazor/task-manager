import random
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group, Permission

from tasks.models import TasksModel

tasks = [
    {
        'title': 'Реализовать новый функционал в модуле Документы',
        'description': 'Добавить возможность комментирования документов'
    },
    {
        'title': 'Исправить баги в модуле Документы',
        'description': 'Превью документа некорректно отображается на планшетах'
    },
    {
        'title': 'Исправить баги в модуле Пользователи',
        'description': 'Ошибка сервера при попытке обновить аватарку пользователя'
    },
]


def create_user_groups():
    group_1, _ = Group.objects.get_or_create(name='engineer')
    group_1.permissions.set(
        Permission.objects.filter(codename__in=[
            'view_tasksmodel',
            'change_tasksmodel',
        ])
    )

    group_1.save()

    group_2, _ = Group.objects.get_or_create(name='tester')
    group_2.permissions.set(
        Permission.objects.filter(codename__in=[
            'view_tasksmodel',
            'change_tasksmodel',
        ])
    )

    group_2.save()

    group_3, _ = Group.objects.get_or_create(name='leader')
    group_3.permissions.set(
        Permission.objects.filter(codename__in=[
            'create_taskmodel',
            'view_tasksmodel',
            'change_tasksmodel',
            'delete_taskmodel',
        ])
    )

    group_2.save()


def create_base_users():
    password = make_password('password1')

    user_model = get_user_model()
    leader_group = Group.objects.get(name='leader')
    engineer_group = Group.objects.get(name='engineer')
    tester_group = Group.objects.get(name='tester')
    
    # super_user = User.objects.create_user(
    #     'admin',
    #     password=password,
    # )
    #
    # super_user.is_superuser = True
    # super_user.is_staff = True
    #
    # super_user.save()

    leader = user_model.objects.create(
        username='kutuzov',
        first_name='Михаил',
        last_name='Кутузов',
        password=password,
    )

    leader.groups.add(leader_group)

    engineer_1 = user_model.objects.create_user(
        username='bagrat',
        first_name='Петр',
        last_name='Багратион',
        password=password,
    )

    engineer_1.groups.add(engineer_group)

    engineer_2 = user_model.objects.create_user(
        username='leo',
        first_name='Леонтий',
        last_name='Беннигсен',
        password=password,
    )

    engineer_2.groups.add(engineer_group)

    engineer_3 = user_model.objects.create_user(
        username='dan',
        first_name='Данила',
        last_name='Поперечный',
        password=password,
    )

    engineer_3.groups.add(engineer_group)

    tester_1 = user_model.objects.create_user(
        username='nikolas',
        first_name='Николай',
        last_name='Ростов',
        password=password,
    )

    tester_1.groups.add(tester_group)

    tester_2 = user_model.objects.create_user(
        username='natali',
        first_name='Наталья',
        last_name='Ростова',
        password=password,
    )

    tester_2.groups.add(tester_group)


def create_seed_tasks():
    leader = User.objects.filter(groups__name='leader').first()
    engineers = User.objects.filter(
        groups__name='engineer'
    )

    for task in tasks:
        TasksModel.objects.create(
            title=task['title'],
            description=task['description'],
            deadline=datetime.now() + timedelta(days=random.choice(range(10))),
            executor=random.choice(engineers),
            author=leader,
            created_at=datetime.now()
        )
