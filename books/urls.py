from django.urls import path
from .views import *

app_name = 'books'


urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('create/', BooksCreateView.as_view(), name='add'),
    path('update/', BooksUpdateView.as_view(), name='update'),
    path('delete/', BooksDeleteView.as_view(), name='delete'),
]