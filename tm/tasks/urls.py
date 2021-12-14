from django.urls import path

from tasks import views


app_name = 'tasks'

urlpatterns = [
    path('', views.render_tasks_list, name='all'),
    path('open/', views.render_tasks_list, name='open'),
    path('in_progress/', views.render_tasks_list, name='in_progress'),
    path('completed/', views.render_tasks_list, name='completed'),
    path('checked/', views.render_tasks_list, name='checked'),
    path('new/', views.render_task_form, name='new'),
    path('<int:task_id>', views.render_task_detail, name='detail'),
]
