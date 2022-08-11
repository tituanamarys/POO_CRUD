from asyncio import new_event_loop
from http.client import HTTPResponse
from turtle import title
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tasks
from .forms import TaskForm

def inicio (request):
    return render(request,'inicio.html')
def about (request):
    return render(request,'about.html')
def list_tasks (request):
    tasks=Tasks.objects.all()
    return render(request,'task/index.html',{'tasks':tasks})
# Create your views here.
# def list_tasks(request):
#     tasks=Tasks.objects.all()
#     #print(tasks)
#     return render(request,'list_tasks.html',{"tasks": tasks})
#funcion para guardar datos
# def create_tasks(request):
#     #print(request.POST)
#     task=Tasks(name=request.POST['name'],description=request.POST['description'])
#     task.save()
def create_tasks(request):
    #print(request.POST)
    form=TaskForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_tasks') 
    return render(request,'task/create.html',{'form':form})

def delete_tasks(request,task_id):
    task=Tasks.objects.get(id=task_id)
    task.delete();
    return redirect('list_tasks')


#funcion para guardar datos
def update_tasks(request,task_id):
    task=Tasks.objects.get(id=task_id)
    form=TaskForm(request.POST or None, request.FILES or None, instance=task)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('list_tasks')
    return render(request,'task/edit.html',{'form':form})