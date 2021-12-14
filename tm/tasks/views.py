from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets

from tasks.forms import TaskCreateForm
from tasks.models import TasksModel
from tasks.serializers import TasksSerializer, CreateTaskSerializer, UpdateTaskSerializer


def render_tasks_list(request):
    template = loader.get_template('tasks/list.html')
    last_word = request.path.split('/')[-2]
    if last_word == 'tasks':
        tasks = TasksModel.objects.all()
        title = 'Все задачи'
    else:
        tasks = TasksModel.objects.filter(status=last_word.upper())
        title = f'Задачи в статусе {TasksModel.TaskStatusesRu[last_word.upper()]}'

    context = {
        'title': title,
        'tasks': tasks
    }
    return HttpResponse(template.render(context, request))


def render_task_form(request):
    template = loader.get_template('tasks/form.html')
    context = {
        'form': TaskCreateForm,
    }
    return HttpResponse(template.render(context, request))


def render_task_detail(request, task_id):
    template = loader.get_template('tasks/get.html')
    task = TasksModel.objects.get(id=task_id)
    context = {
        'task': task,
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
