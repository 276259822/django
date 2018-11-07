from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('write/', views.write, name='write'),
]

