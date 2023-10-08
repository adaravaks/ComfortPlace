from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView

from accounts.forms import RegisterUserForm
from accounts.tokens import account_activation_token


def activateEmail(request, user, to_email):
    mail_subject = 'Подтверждение электронной почты'
    message = render_to_string('accounts/email-verification-message.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Ах ты ёбаный {user}, быстро пиздуй на свой {to_email} и подтверждай свою поганую регистрацию.', extra_tags='alert-success alert')
    else:
        messages.error(request, f'Хуй тебе, а не письмо на {to_email}', extra_tags='alert-danger alert')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        activateEmail(self.request, user, form.cleaned_data.get('email'))
        return redirect('login')  # TODO: continue from there


class LoginUser(LoginView):
    template_name = 'accounts/login.html'


def logout(request):
    return HttpResponse('Logout page')


def profile(request):
    return HttpResponse('Profile page')