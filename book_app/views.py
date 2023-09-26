from django.shortcuts import render
from .models import Book
from django_ratelimit.decorators import ratelimit

from django.http import HttpRequest

def get_client_ip(request, view):
    if not isinstance(request, HttpRequest):
        return "unknown"

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', "unknown")
    return ip

# Create your views here.
@ratelimit(key=get_client_ip, rate='5/m', method='GET', block=True)
def index(request):
    books = Book.objects.all()
    context = {'books': books}

    return render(request, 'index.html', context=context)
