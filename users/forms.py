from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users
from django.contrib.auth import authenticate

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class StaffLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError("Staff: Login ou senha invalidos")
            if not user.is_staff:
                raise forms.ValidationError("Usuário não é membro da equipe.")
        return super().clean()

class StaffSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ("email",)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user