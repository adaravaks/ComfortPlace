from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import PostForm, ThemeForm
from .models import Theme, Post


def index(request):
    themes = Theme.objects.order_by('-id')
    context = {'title': 'Главная страница', 'themes': themes}
    return render(request, 'forum/index.html', context)


def theme(request, theme_id):
    main_theme = Theme.objects.get(pk=theme_id)
    posts_related = Post.objects.filter(parent_theme_id=theme_id)
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        parent_theme = Theme.objects.get(pk=theme_id)
        author = User.objects.get(pk=request.user.id)
        form.instance.parent_theme = parent_theme
        form.instance.author = author
        if form.is_valid():
            form.save()
            return redirect(parent_theme)
        else:
            error = 'Неверный ввод'

    form = PostForm()
    context = {
        'theme_id': theme_id,
        'main_theme': main_theme,
        'posts_related': posts_related,
        'error': error,
        'form': form
    }
    return render(request, 'forum/theme.html', context)


def new_theme(request):
    error = ''
    if request.method == 'POST':
        form = ThemeForm(request.POST, request.FILES)
        author = User.objects.get(pk=request.user.id) if request.user.is_authenticated else None
        form.instance.author = author
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = ThemeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'forum/new-theme.html', context)