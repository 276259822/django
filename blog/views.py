from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Article, Category, Tag
from .forms import ArticleForm


def index(request):
    return render(request, 'blog/index.html')

@login_required
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

@login_required
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

@login_required
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.increase_views()
    return render(request, 'blog/detail.html', locals())

@login_required
def category(request, category_pk):
    cate = Category.objects.get(pk=category_pk)
    article_list = Article.objects.filter(category=cate)
    return render(request, 'users/accounts.html', locals())

@login_required
def tag(request, tag_pk):
    tag = Tag.objects.get(pk=tag_pk)
    article_list = Article.objects.filter(tags=tag)
    return render(request, 'users/accounts.html', locals())

@login_required
def dates(request, year, month):
    article_list = Article.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'users/accounts.html', locals())
