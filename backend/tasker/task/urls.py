from django.contrib import admin
from django.urls import path
#from task.views import taskList, taskCreate, task
from task.views import TaskList, TaskCreate, TaskDetail

urlpatterns = [
    path('task/list/', TaskList.as_view()),
    path('task/create/', TaskCreate.as_view()),
    path('task/<int:pk>/', TaskDetail.as_view())
]
