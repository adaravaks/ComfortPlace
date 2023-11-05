from django.forms import ModelForm, TextInput, Textarea, FileInput
from .models import Post, Theme


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'post_picture')
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Пост'}),

            'post_picture':  FileInput(attrs={
                'class': '',
                'placeholder': 'Изображение (необязательно)'})
        }


class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ('header', 'text', 'media')
        widgets = {
            'header': TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Заголовок'}),

            'text': Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Тема'}),

            'media': FileInput(attrs={
                'class': '',
                'placeholder': 'Изображение (необязательно)'})
        }
