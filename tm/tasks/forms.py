from django.forms import ModelForm

from tasks.models import TasksModel


class TaskCreateForm(ModelForm):
    class Meta:
        model = TasksModel
        fields = ['title', 'description', 'executor']
