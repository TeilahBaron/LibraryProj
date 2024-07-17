from django import forms
from .models import MyBooks

class MyBooksForm(forms.ModelForm):
    class Meta:
        model = MyBooks
        fields = ['reader', 'book', 'borrowed_date', 'returned_date']
