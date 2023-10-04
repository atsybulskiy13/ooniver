# from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from my_django.mysite.utils import get_simple_numbers_in_number


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
