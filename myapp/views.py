from django.http import HttpResponse, JsonResponse
from myapp.models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def hello(request):
    #return HttpResponse("Hola Mundo")
    greeting = 'Welcome to Django Course :D :D'
    return render(request, 'index.html', {
        'greeting' : greeting
    })

def about(request):
    #return HttpResponse("Sobre nosotros")
    enterprise = 'ADISA'
    return render(request, 'about.html', {
        'enterprise': enterprise
    })

def greetings(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def suma(request, numero):
    return HttpResponse(numero + 2)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    #return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    #return HttpResponse('task: %s' % task.name)
    
    tasks = Task.objects.all()

    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):

    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()
    })

    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=5)
        return redirect('tasks')
    
def create_project(request):

    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    
    else:
        Project.objects.create(name=request.POST["name"])

        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)

    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })