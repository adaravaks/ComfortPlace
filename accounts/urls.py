from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]
