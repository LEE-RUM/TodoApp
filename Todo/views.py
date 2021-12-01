from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Todo
from django.contrib import messages



def index(request):
    tasks = Todo.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)


def add_todo(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'index.html', context)

def update_todo(request, id):
    task = Todo.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'update.html', {'form': form})


def delete_todo(request, id):
    task = Todo.objects.get(id=id)

    if request.method == 'POST':
        messages.success(request, task.task_name + " has been removed.")
        task.delete()
        return redirect('index')

    return render(request, 'delete.html', {'task': task})


def complete_todo(request, id):
    task = Todo.objects.get(id=id)
    task.completed = True
    task.save()
    messages.success(request, task.task_name + " has been completed.")

    return redirect('index')