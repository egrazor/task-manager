from django.forms import ModelForm

from tasks.models import TasksModel


class TaskForm(ModelForm):
    class Meta:
        model = TasksModel
        fields = ['title', 'description', 'executor']
