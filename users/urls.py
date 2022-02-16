from django.urls import path
from .views import StaffSigUpView

urlpatterns = [
    path('login/', StaffSigUpView.as_view(), name='login'),
]