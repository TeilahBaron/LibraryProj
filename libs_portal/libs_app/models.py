from django.db import models

# Create your models here.

class Reader(models.Model):
    reference_id = models.CharField(max_length=200)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.reader_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    published_year = models.IntegerField()
    copies_available = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class MyBooks(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    returned_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.reader.reader_name} - {self.book.title}"
    # libs_app/models.py

from django.db import models
from django.contrib.auth.models import User

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
