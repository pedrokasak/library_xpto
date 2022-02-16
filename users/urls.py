from django.urls import path
from .views import register, staff_login, logout

app_name ='users'

urlpatterns = [
    path('', staff_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]