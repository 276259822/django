from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
    path('settings/form/', views.settings_form, name='settings_form'),
    path('accounts/', views.accounts, name='accounts'),
]

