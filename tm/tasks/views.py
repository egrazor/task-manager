from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Hello, world')


def task_info(request, task_id):
    return HttpResponse(f'This is info about {task_id}')
