from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect


# Create your views here.
from .models import *

def home(request):
    return render(request, 'home.html',context={'current_tab': 'home'})

def readers(request):
    return render(request, 'readers.html',context={'current_tab': 'readers'})

def books(request):
    return render(request, 'books.html',context={'current_tab': 'books'})

def mybooks(request):
    user_books = BorrowedBook.objects.filter(user=request.user)  # Adjust this query based on your actual model structure

    return render(request, 'mybooks.html', {'user_books': user_books})

def returns(request):
    return render(request, 'returns.html',context={'current_tab': 'returns'})


def shop(request):
    return HttpResponse("Hello Shopping")

def save_student(request):
    student_name = request.POST['student_name']
    return render(request, 'welcome.html', context={'student_name':student_name})

def readers_tab(request):
    if request.method == "GET":
        readers = Reader.objects.all()  # Query all readers using the Reader model
        return render(request, "readers.html", context={"current_tab": "readers", "readers": readers})
    elif request.method == "POST":
        query = request.POST.get('query')  
        readers = Reader.objects.raw(f"SELECT * FROM libs_app_reader WHERE reader_name LIKE '%{query}%'")
        return render(request, "readers.html", context={"current_tab": "readers", "readers": readers, "query": query})

def save_reader(request):
    reader_item = Reader(reference_id=request.POST.get('reader_ref_id'),
                         reader_name=request.POST.get('reader_name'),
                         reader_contact=request.POST.get('reader_contact'),
                         reader_address=request.POST.get('reader_address'),
                         active=True)
    reader_item.save()
    return redirect('readers')



def books_tab(request):
    query = request.GET.get('query')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    
    return render(request, "books.html", context={"current_tab": "books", "books": books, "query": query})

def save_reader(request):
    if request.method == "POST":
        reader_item = Reader(reference_id=request.POST.get('reader_ref_id'),
                             reader_name=request.POST.get('reader_name'),
                             reader_contact=request.POST.get('reader_contact'),
                             reader_address=request.POST.get('reader_address'),
                             active=True)
        reader_item.save()
        return redirect('readers')  # Redirect to the readers page after saving
    else:
        return render(request, "add_reader.html")  # Display the form to add a reader

def save_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        genre = request.POST['genre']
        published_year = request.POST['published_year']
        copies_available = request.POST.get('copies_available', 1)

        book = Book(title=title, author=author, isbn=isbn, genre=genre, published_year=published_year, copies_available=copies_available)
        book.save()
        return redirect('books')  # Redirect to the books page after saving
    else:
        return render(request, "add_book.html")  # Display the form to add a book
    
    