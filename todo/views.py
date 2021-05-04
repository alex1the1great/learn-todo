from django.shortcuts import render, redirect, get_object_or_404

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_add(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    return render(request, 'todo/todo_add.html', {'form': form})


def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo_list')