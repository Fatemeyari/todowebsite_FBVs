from django.shortcuts import render

from django.shortcuts import get_object_or_404 , redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Todo
from users.models import User
from .forms import CreateTaskForm
@login_required(login_url='login_view')
@never_cache
def todo_list(request):
    """ Show all Todo tasks for the current user, with pagination. """
    user = request.user
    all_plans = Todo.objects.filter(user=user)
    todos_paginator = Paginator(all_plans, 5)
    page_number = request.GET.get('page', 1)
    try:
        todos = todos_paginator.get_page(page_number)
    except PageNotAnInteger:
        todos = todos_paginator.get_page(1)
    except EmptyPage:
        todos = todos_paginator.get_page(todos_paginator.num_pages)
    return render(
        request,
        'todo_list.html',
        {
            'todos': todos,
            'username': user
        })


@login_required(login_url='login_view')
@never_cache
def todo_create(request):
    """ Create a new Todo task for the current user. """
    if request.method=='POST':
        form=CreateTaskForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            if title:
                plan=Todo.objects.create(user=request.user,title=title)
            return redirect('todo_list')
        return redirect('.')
    else:
        form=CreateTaskForm()
    return render(request, 'todo_list.html', {'form':form})



@login_required(login_url='login_view')
@never_cache
def is_done(request,pk):
    """ Toggle the 'done' status of a Todo task. """
    plan=get_object_or_404(Todo,pk=pk , user=request.user)
    if plan.done:
        plan.done=False
    else:
        plan.done=True
    plan.save()
    return redirect('todo_list')




@login_required(login_url='login_view')
@never_cache
def todo_delete(request,pk):
    """ Delete a Todo task for the current user. """
    user=request.user
    plan=get_object_or_404(Todo,pk=pk , user=user)
    plan.delete()
    return redirect('todo_list')
