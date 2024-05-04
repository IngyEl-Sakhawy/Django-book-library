from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


books= list()
num = 1

def books_list (request):
    all_books= {
        'books' : books
    }

    print("hello from list",books)

    return render(request, 'books_list.html', context=all_books)


def books_add (request):
    return render(request, 'books_add.html')

def book_added(request):
    if request.method == 'POST':
        global num
        
        book_name = request.POST.get('book_name')
        book_author = request.POST.get('book_author')
        book_description = request.POST.get('book_description')

        new_book = {
            'id' : num,
            'name': book_name,
            'author': book_author,
            'description': book_description
        }

        books.append(new_book)
        print(books)
        num+=1
        
        return redirect('books:books-list')
    else:
        return redirect('books:books-add')
    

def _get_book(book_id):
    for book in books:
        print(f"Checking book ID: {book['id']}")
        if book['id'] == book_id:
            print("Found matching book!")
            return book
    print("No book found with the specified ID")
    return None

def books_detail(request, *args, **kwargs):
    book_id = kwargs.get('book_id')
    print("typpppppe",book_id)
    book_object = _get_book(book_id)
    print(book_object)
    if book_object:
        my_context = {
            'book_id': book_object.get('id'),
            'book_name': book_object.get('name'),
            'book_author': book_object.get('author'),
            'book_description': book_object.get('description') 
        }
        print(my_context)
        return render(request, 'books_detail.html', context=my_context)
    else:
        return HttpResponse("Book not found")
    
def books_delete(request, **kwrgs):
    book_id = kwrgs.get('book_id')
    book_object = _get_book(book_id)
    if book_object:
        books.remove(book_object)
    return redirect("books:books-list")

def books_updated(request, **kwrgs):
    if request.method == 'POST':
        
        book_id = kwrgs.get('book_id')
        # book_id = request.POST.get('book_id')
        book_name = request.POST.get('book_name')
        book_author = request.POST.get('book_author')
        book_description = request.POST.get('book_description')

        book_object = _get_book(book_id)
        if book_object:
            books.remove(book_object)

        new_book = {
            'id' : book_id,
            'name': book_name,
            'author': book_author,
            'description': book_description
        }

        books.append(new_book)
        print(books)
        
        
        return redirect('books:books-list')  

def books_update(request, **kwrgs):
    book_id = kwrgs.get('book_id')
    book_object = _get_book(book_id)
    print(book_object)
    if book_object:
        my_context = {
            'book_id': book_object.get('id'),
            'book_name': book_object.get('name'),
            'book_author': book_object.get('author'),
            'book_description': book_object.get('description') 
        }
        print(my_context)
        return render(request, 'books_edit.html', context=my_context)
    