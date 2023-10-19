from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('theme/<int:theme_id>', views.theme, name='theme'),
    path('new-theme', views.new_theme, name='new-theme'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
