from django.http import HttpRequest
from django.shortcuts import render, redirect
# flake8: noqa
from todo_list.forms import TodoForm
from todo_list.models import Todo


# Create your views here.

def todo_index(request):
    todo_list = Todo.objects.filter(is_finished=False)
    context = {'todo_list': todo_list}
    return render(
        request=request,
        template_name='todo_index.html',
        context=context
    )


def create_todo(request: HttpRequest):
    context = {}

    if request.method == 'GET':
        form = TodoForm()
        context['form'] = form
        return render(
            request=request,
            template_name='create_todo.html',
            context=context
        )

    form = TodoForm(request.POST)
    if form.is_valid():
        title = form.data['title']
        finish_date = form.data['finish_date']
        is_active = True if form.data.get('is_active') else False
        is_finished = True if form.data.get('is_finished') else False

        context['title'] = title
        context['finish_date'] = finish_date
        context['is_active'] = is_active
        context['is_finished'] = is_finished

        todo_task = Todo.objects.create(
            title=title,
            owner='Sunshine',
            finish_date=finish_date,
            is_active=is_active,
            is_finished=is_finished
        )

        return render(
            request=request,
            template_name='todo_result.html',
            context=context
        )

    else:
        context['form'] = form
        return render(
            request=request,
            template_name='create_todo.html',
            context=context
        )


def task_details(request: HttpRequest, task_id):
    task = Todo.objects.get(id=task_id)

    if request.method == 'GET':
        initial_data = {
            'title': task.title,
            'finish_date': task.finish_date,
            'is_active': task.is_active,
            'is_finished': task.is_finished
        }

        form = TodoForm(initial=initial_data)

        context = {'form': form}

        return render(
            request,
            template_name='task.html',
            context=context
        )

    form = TodoForm(request.POST)
    context = {}

    if form.is_valid():
        title = form.data['title']
        finish_date = form.data['finish_date']
        is_active = True if form.data.get('is_active') else False
        is_finished = True if form.data.get('is_finished') else False

        task.title = title
        task.finish_date = finish_date
        task.is_active = is_active
        task.is_finished = is_finished

        task.save()

        return redirect('todo_index')

    else:
        context[form] = form
        return render(
            request=request,
            template_name='task.html',
            context=context
        )
