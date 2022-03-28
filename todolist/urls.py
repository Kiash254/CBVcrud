
from django.urls import path
from .views import TaskUpdate, Tasklist, TaskDetail
app_name='todolist'

urlpatterns=[
    path('',Tasklist.as_view(),name='task-list'),   
    path('task-create/',TaskDetail.as_view(),name='task-create'),
     path('task/<int:pk>/',TaskDetail.as_view(),name='detailview'),
     path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
]