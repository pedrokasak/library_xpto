from rest_framework import viewsets

from ..api.serializers import BooksSerializer
from ..models import Books


class BooksCreateViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer