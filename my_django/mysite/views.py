from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import json
from datetime import datetime
# flake8: noqa
from mysite.utils import get_simple_numbers_in_number, if_palindrom


# Create your views here.


def index(request):
    response = HttpResponse("Hello, Sashka! It's your first view")
    return response


def main_page(request):
    response = HttpResponse(f'Hello, user! You entered at {datetime.now().isoformat()}')
    return response


def simple_numbers(request, number):
    simple_numbers = get_simple_numbers_in_number(number)
    response = HttpResponse(f'All simple numbers in {number}: {simple_numbers}')
    return response


def admin_page(request):
    return HttpResponse(f'<h1>Вы вошли как Админ</h1>')


def guest_page(request, role):
    return HttpResponse(f'<h1>Вы вошли как {role}<h1>')


def check_role(request, role):
    if role == 'admin':
        return redirect('admin-page')
    else:
        return redirect('guest-page', role=role)


def palindrome(request, word):
    if if_palindrom(word):
        return HttpResponse(f'Half word: {word[:len(word) // 2]}')
    else:
        return redirect('main-page')


def check_view(request: HttpRequest):
    if request.method == 'GET':
        page_number = request.GET.get('number')
        return redirect('guest-page', role=page_number)

    return redirect('admin-page')


def book_booking(request: HttpRequest):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='book_booking.html'
        )

    user_data = {
        'book_name': request.POST.get('book_name'),
        'person_name': request.POST.get('person_name'),
        'period': request.POST.get('period')
    }

    with open('user.txt', 'w') as user_file:
        user_file.write(json.dumps(user_data))

    return render(
        request=request,
        template_name='new_template.html',
        context={'user_data': user_data}
    )
