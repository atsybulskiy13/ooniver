from django.urls import path
from my_django.mysite.views import index, main_page, simple_numbers, admin_page, guest_page, check_role, palindrome,\
    check_view, book_booking

urlpatterns = [
    path('hi/', index, name='index'),
    path('', main_page, name='main-page'),
    path('simple_numbers/<int:number>', simple_numbers, name='simple_numbers'),
    path('admin_new/', admin_page, name='admin-page'),
    path('guest/<role>', guest_page, name='guest-page'),
    path('check_role/<role>', check_role, name='check-role'),
    path('palindrome/<word>', palindrome, name='palindrome'),
    path('check_view', check_view, name='check-view'),
    path('book_booking', book_booking, name='book-booking')
]
