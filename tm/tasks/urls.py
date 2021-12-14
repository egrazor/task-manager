from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.render_tasks_list),
    path('new/', views.render_task_form),
]
