from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, TextInput, Textarea, FileInput, PasswordInput, CharField, EmailInput, EmailField


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Имя пользователя', widget=TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}))
    email = EmailField(label='Адрес электронной почты', widget=EmailInput(attrs={'class': 'form-input', 'placeholder': 'Адрес электронной почты'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))
    password2 = CharField(label='Пароль ещё раз', widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль ещё раз'}))


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Имя пользователя', widget=TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))