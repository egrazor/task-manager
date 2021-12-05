from django.db import models
from django.conf import settings


class TaskStatuses(models.TextChoices):
    OPEN = 'OPEN'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    CHECKED = 'CHECKED'


class TasksModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(
        choices=TaskStatuses.choices,
        default=TaskStatuses.OPEN,
        max_length=20,
    )

    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Task(id={self.id}, title={self.title[:10]})'
