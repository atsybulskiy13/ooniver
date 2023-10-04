from django.urls import path
from my_django.mysite.views import index, main_page, simple_numbers

urlpatterns = [
    path('hi/', index, name='index'),
    path('', main_page, name='main_page'),
    path('simple_numbers/<int:number>', simple_numbers, name='simple_numbers')
]
