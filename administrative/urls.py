from django.urls import path
from .views import index

app_name = 'administrative'

urlpatterns = [
    path('index/',index,name='index')
]