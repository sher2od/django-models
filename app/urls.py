from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.create_task, name='create_task'),   # Shu nom kerak
    path('list/', views.task_list, name='task_list'),
]

