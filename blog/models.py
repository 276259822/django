from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=60)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=60)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class Article(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    views = models.PositiveIntegerField(default=0)
    flower = models.PositiveIntegerField(default=0)
    collection = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    is_delete = models.BooleanField(default=False)

    objects = ArticleManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views',])

    def delete(self, using=None, soft=True, *args, **kwargs):
        if soft:
            self.is_delete = True
            self.save(using=using)
        else:
            return super(Article, self).delete(using=using, *args, **kwargs)
