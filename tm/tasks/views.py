from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets

from tasks.forms import TaskForm
from tasks.models import TasksModel
from tasks.serializers import TasksSerializer, CreateTaskSerializer, UpdateTaskSerializer


def render_tasks_list(request):
    template = loader.get_template('tasks/list.html')
    tasks = TasksModel.objects.all()
    context = {
        'tasks': tasks
    }
    return HttpResponse(template.render(context, request))


def render_task_form(request):
    template = loader.get_template('tasks/form.html')
    engineers = User.objects.filter(groups__name='engineer')
    context = {
        'engineers': engineers,
        'form': TaskForm,
    }
    return HttpResponse(template.render(context, request))


class TasksViewSet(viewsets.ModelViewSet):
    queryset = TasksModel.objects.all()
    serializer_class = TasksSerializer

    def perform_create(self, serializer):
        serializer.save(
            status=TasksModel.TaskStatuses.OPEN,
            author=self.request.user,
            created_at=datetime.now(),
        )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTaskSerializer
        elif self.request.method in ['UPDATE', 'PATCH']:
            return UpdateTaskSerializer
        else:
            return self.serializer_class
