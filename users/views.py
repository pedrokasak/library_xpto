from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login, authenticate
from users.models import Users
from django.views.generic import CreateView
from .forms import *


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'register.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'register.html',
                  {'user_form': user_form})


class StaffSigUpView(CreateView):
    model = Users
    form_class = StaffSignUpForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('administrative:index')


def staff_login(request):
    form = StaffLoginForm(request.POST)
    if form.is_valid():
        u = form.cleaned_data['email']
        p = form.cleaned_data['password']

        user = authenticate(request, username=u, password=p)
        try:
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('administrative:index')

        except Exception as e:
            print(e)
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')
