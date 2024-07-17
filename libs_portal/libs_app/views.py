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
    return render(request, 'mybooks.html',context={'current_tab': 'mybooks'})

def returns(request):
    return render(request, 'returns.html',context={'current_tab': 'returns'})


def shop(request):
    return HttpResponse("Hello Shopping")

def save_student(request):
    student_name = request.POST['student_name']
    return render(request, 'welcome.html', context={'student_name':student_name})

def readers_tab(request):
    readers = Reader.objects.all()  # Ensure the model name is correct
    return render(request, "readers.html", context={"current_tab": "readers", "readers": readers})

def save_reader(request):
    reader_item = Reader(reference_id=request.POST.get('reader_ref_id'),
                         reader_name=request.POST.get('reader_name'),
                         reader_contact=request.POST.get('reader_contact'),
                         reader_address=request.POST.get('reader_address'),
                         active=True)
    reader_item.save()
    return redirect('readers')