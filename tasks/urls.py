from django.urls import path, re_path

from . import views

app_name='tasks'
urlpatterns = [
	path('', views.tasks, name = 'tasks'),
    path('createtask/', views.createtask, name='newtask'),
    path('<int:task_pk>/', views.edittask, name='edittask'),
    path('delete/<int:task_pk>/', views.deletetask, name='deletetask'),
    re_path(r'.*', views.bad, name = 'bad link'),
]