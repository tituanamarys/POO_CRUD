from turtle import title
from django.shortcuts import render,redirect

import tasks
from .models import Tasks

# Create your views here.
def list_tasks(request):
    tasks=Tasks.objects.all()
    #print(tasks)
    return render(request,'list_tasks.html',{"tasks": tasks})
#funcion para guardar datos
def create_tasks(request):
    #print(request.POST)
    task=Tasks(name=request.POST['name'],description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_tasks(request,task_id):
    task=Tasks.objects.get(id=task_id)
    task.delete();
    return redirect('/tasks/')