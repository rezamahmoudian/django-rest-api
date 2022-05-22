from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=160, default=None)
    link = models.URLField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
