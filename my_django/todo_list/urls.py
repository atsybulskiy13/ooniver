from django.urls import path

from todo_list.views import todo_index, create_todo, task_details


urlpatterns = [
    path('', todo_index, name='todo_index'),
    path('create-todo/', create_todo, name='create-todo'),
    path('task/<str:task_id>', task_details, name='task-details')
]
