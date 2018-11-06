from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, SettingsForm
from .models import User

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
        form = SettingsForm(request.POST)
        if form.is_valid():
            user.nickname = form.cleaned_data['nickname']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('users:settings')
    else:
        form = SettingsForm()
    
    context = {
        'form': form
    }
    return render(request, 'users/settings_form.html', context)

# 设置 - 帐号信息 - 展示
def accounts(request):
    return render(request, 'users/accounts.html')
