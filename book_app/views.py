from django.shortcuts import render
from .models import Book
from django_ratelimit.decorators import ratelimit

# Create your views here.
@ratelimit(key='ip', rate='5/m', block=True)
def index(request):
    books = Book.objects.all()
    context = {'books': books}

    return render(request, 'index.html', context=context)
