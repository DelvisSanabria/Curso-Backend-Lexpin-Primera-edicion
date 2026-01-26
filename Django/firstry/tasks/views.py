from django.http import HttpResponse
from .models import Task
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
  return HttpResponse("<h1>Hola estamos respondiendo desde Django</h1>")

def task_list(request):
  # Obtener todas las tareas de la base de datos
  all_task = Task.objects.all()

  #Creamos un diccionario para enviar las tareas al template
  context = {
    'tasks': all_task,
    'page_title': 'Lista de todas las Tareas',
  }

  #Renderizamos la plantilla task_list.html con el contexto
  return render(request, 'tasks/task_list.html', context)
  
  
def create_task(request):
  #De la request obtenemos los datos del formulario
  if request.method == 'POST':
    #Obtener los datos del formulario
    title = request.POST.get('title')
    description = request.POST.get('description')
    
    #Crear una nueva tarea en la base de datos
    Task.objects.create(title=title, description=description)
    
    #al finalizar vamos a mandar al usuario a la lista de tareas
    return redirect('task_list')
  else: 
    return render(request, 'tasks/create_task.html')