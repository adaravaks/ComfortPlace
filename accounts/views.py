from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return HttpResponse('Registration page')


class LoginUser(LoginView):
    pass


def logout(request):
    return HttpResponse('Logout page')


def profile(request):
    return HttpResponse('Profile page')