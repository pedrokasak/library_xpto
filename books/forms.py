from django import forms
from books.models import Books


class BooksCreateViewForm(forms.ModelForm):

    model = Books

    fields = ['name', 'is_available', 'description',
              'publishing_company', 'authors']

    widgets = {
        'name': forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o nome do livro', }
        ),
        'authors': forms.Select(
            attrs={'class': 'form-control', }
        ),
        'description': forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira a descrição do livro', }
        ),
        'publishing_company': forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'informe a Editora', }
        ),
    }
