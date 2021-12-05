from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:task_id>/', views.task_info, name='task-info')
]
