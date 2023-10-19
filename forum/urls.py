from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('theme/<int:theme_id>', views.theme, name='theme'),
    path('new-theme', views.new_theme, name='new-theme'),
]
