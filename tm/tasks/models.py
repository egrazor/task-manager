from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class TasksModel(models.Model):

    class TaskStatuses(models.TextChoices):
        OPEN = 'OPEN'
        IN_PROGRESS = 'IN_PROGRESS'
        COMPLETED = 'COMPLETED'
        CHECKED = 'CHECKED'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='задача')
    description = models.TextField(verbose_name='описание')
    deadline = models.DateTimeField(verbose_name='срок устранения (до)')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='дата создания')
    status = models.CharField(
        choices=TaskStatuses.choices,
        default=TaskStatuses.OPEN,
        max_length=20,
        verbose_name='статус',
    )

    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='executor_task',
        verbose_name='исполнитель',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author_task',
        verbose_name='автор',
        null=True,
    )

    def __str__(self):
        return f'Task(id={self.id}, title={self.title[:10]})'
