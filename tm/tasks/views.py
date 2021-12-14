from datetime import datetime

from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from tasks.forms import TaskCreateForm
from tasks.models import TasksModel


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

    if request.method != 'POST':
        form = TaskCreateForm()
    else:
        form = TaskCreateForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)

            # TODO: remove when resolve authorization
            if isinstance(request.user, AnonymousUser):
                author = User.objects.filter(groups__name='leader').first()
            else:
                author = request.user

            task.author = author
            task.status = TasksModel.TaskStatuses.OPEN
            task.created_at = datetime.now()

            task.save()

            return redirect('tasks:all')

    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def render_task_detail(request, task_id):
    template = loader.get_template('tasks/get.html')
    task = TasksModel.objects.get(id=task_id)
    context = {
        'task': task,
    }
    return HttpResponse(template.render(context, request))
