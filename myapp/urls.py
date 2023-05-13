from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="hello"),
    path('about/', views.about, name="about"),
    path('greetings/<str:username>', views.greetings, name="greetings"),
    path('suma/<int:numero>', views.suma, name="suma"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name = 'project_detail'),
    path('tasks/', views.tasks, name="tasks"),
    path('create-new-task/', views.create_task, name="create-task"),
    path('create-project/', views.create_project, name="create-project")
]