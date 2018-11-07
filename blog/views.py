from django.shortcuts import render, redirect
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
            article.category = Category.objects.get(pk=form.cleaned_data['category'].pk)
            article.author = request.user
            article.save()
            tags = Tag.objects.get(pk=form.cleaned_data['tags'].first().pk)
            article.tags.add(tags)
            return redirect('blog:write')
    else:
        form = ArticleForm()
    return render(request, 'blog/write.html', locals())
