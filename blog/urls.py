from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('write/', views.write, name='write'),
    path('edit/<int:article_pk>/', views.edit, name='edit'),
    path('detail/<int:article_pk>/', views.detail, name='detail'),
]
