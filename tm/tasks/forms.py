from datetime import datetime

from django.forms import ModelForm, DateTimeField

from tasks.models import TasksModel


class TaskCreateForm(ModelForm):
    class Meta:
        model = TasksModel
        fields = ['title', 'description', 'deadline',  'executor']

    deadline = DateTimeField(initial=datetime.now)
