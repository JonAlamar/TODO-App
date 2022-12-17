from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def update(request, task_id):
    task = Todo.objects.get(id=task_id)
    # populate a form instance with data from the data on the database
    # instance=product allows to update the record rather than creating a new record when save method is called
    form = TaskForm(request.POST or None, instance=task)

    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('view_todo')

    # if the request does not have post data, render the page with the form containing the product's info
    return render(request, 'update.html', {'form': form})


def add(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            tasks = Todo.objects.all()
            return render(request, 'index.html', {'tasks': tasks})
        else:
            form = TaskForm()
            return render(request, 'add.html', {'form': form, 'error': 'The data is not valid'})

    else:
        form = TaskForm(request.POST or None)
        return render(request, 'add.html', {'form': form})

def delete(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    # after deleting redirect to view_product page
    return redirect('view_todo')

def search(request):

    search_term = request.GET.get('search') or ''

    print(search_term)
    print("hello")

    tasks = Todo.objects.filter(task_name__icontains=search_term)

    return render(request, 'index.html', {'tasks': tasks})
