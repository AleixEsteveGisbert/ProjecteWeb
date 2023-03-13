from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from Wallapop.models import UserInfo


class Register(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(Register, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            userInfo = UserInfo.objects.create(user=user)
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuari'}))
    password = forms.CharField(label="Contraseña", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contrasenya'}))