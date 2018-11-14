from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('write/', views.write, name='write'),
    path('edit/<int:article_pk>/', views.edit, name='edit'),
    path('detail/<int:article_pk>/', views.detail, name='detail'),
    path('category/<int:category_pk>/', views.category, name='category'),
    path('tag/<int:tag_pk>/', views.tag, name='tag'),
    path('dates/<int:year>/<int:month>/', views.dates, name='dates'),
    path('delete/<int:article_pk>/', views.delete, name='delete'),
]
