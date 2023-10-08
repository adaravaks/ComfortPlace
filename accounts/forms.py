from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, TextInput, Textarea, FileInput, PasswordInput, CharField, EmailInput, EmailField


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Имя пользователя', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    email = EmailField(label='Адрес электронной почты', widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Адрес электронной почты'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = CharField(label='Пароль ещё раз', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль ещё раз'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'}),

            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес электронной почты'}),

            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'}),

            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль ещё раз'})
        }


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Имя пользователя', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))