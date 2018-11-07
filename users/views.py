from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, SettingsForm
from .models import User
from blog.models import Article

# 注册账号


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)

# 设置 - 帐号信息 - 展示


def settings(request):
    return render(request, 'users/settings.html')

# 设置 - 帐号信息 - 编辑
# 为解决问题 - form表单默认值


def settings_form(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:settings')
    else:
        form = SettingsForm(instance=user)

    context = {
        'form': form
    }
    return render(request, 'users/settings_form.html', context)

# 设置 - 帐号信息 - 展示


def accounts(request):
    article_list = Article.objects.filter(author=request.user)
    return render(request, 'users/accounts.html', locals())
