from django import template
from blog.models import Article, Category, Tag

register = template.Library()

@register.simple_tag()
def get_date_list():
    article_list = Article.objects.dates('created_time', 'month', order='DESC')
    return article_list

@register.simple_tag()
def get_catagory_list():
    category_list = Category.objects.all()
    return category_list

@register.simple_tag()
def get_tag_list():
    tag_list = Tag.objects.filter()
    return tag_list
