from django.db import models
from django.db.models import CASCADE, SET_NULL
from django.urls import reverse


class Post(models.Model):
    text = models.TextField('Пост', max_length=3000)
    post_picture = models.ImageField(upload_to='communication_pictures/posts/%Y/%m/%d/', blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    parent_theme = models.ForeignKey('Theme', on_delete=CASCADE, blank=True)
    author = models.ForeignKey('auth.User', to_field='username', on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('theme', kwargs={'theme_id': self.parent_theme})


class Theme(models.Model):
    header = models.TextField(max_length=200, db_index=True)
    media = models.ImageField(upload_to='communication_pictures/themes/%Y/%m/%d/', blank=True)
    text = models.TextField(max_length=5000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', to_field='username', on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def get_absolute_url(self):
        return reverse('theme', kwargs={'theme_id': self.pk})