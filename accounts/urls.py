from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView
from djangoProject import settings
from . import views

urlpatterns = [
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('profile', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
