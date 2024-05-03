from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

books= list()

def show_all_books (request):
    all_books= {
        'books' : books
    }

    return render(request, 'base_layout.html', content_type=all_books )

def index(request):

    # return HttpResponse("hello os")
    return  render(request, 'base_layout.html')