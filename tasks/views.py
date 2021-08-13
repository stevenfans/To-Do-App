from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import Task
from tasks.forms import taskForm 


def index(request):
    tasks = Task.objects.all()

    form = taskForm()

    if request.method =='POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}

    return render(request, 'tasks/list.html',context)

def updateTask(request,pk):

    task = Task.objects.get(id=pk)

    form = taskForm(instance=task)

    if request.method == 'POST': 
        form = taskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'tasks/update_task.html',context)

def deleteTask(request,pk):

    item = Task.objects.get(id=pk)

    if request.method == 'POST': 
        item.delete()
        return redirect('/') 
        
    context = {'item':item}

    return render(request,'tasks/delete_task.html',context)