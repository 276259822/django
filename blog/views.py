from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from .models import Article, Category, Tag
from .forms import ArticleForm


def index(request):
    return render(request, 'blog/index.html')


def write(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article()
            article.title = form.cleaned_data['title']
            article.body = form.cleaned_data['body']
            article.excerpt = form.cleaned_data['excerpt']
            article.category = Category.objects.get(
                pk=form.cleaned_data['category'].pk)
            article.author = request.user
            article.save()
            tags = Tag.objects.get(pk=form.cleaned_data['tags'].first().pk)
            article.tags.add(tags)
            return redirect('users:accounts')
    else:
        form = ArticleForm()
    return render(request, 'blog/write.html', locals())


def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('users:accounts')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/edit.html', locals())


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    return render(request, 'blog/detail.html', locals())
