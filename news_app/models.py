from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils import timezone
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)

class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images', blank=True)
    image_url = models.CharField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE
                                 )
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                              )
    
    class Meta:
        ordering = ['-publish_time']

    published = PublishedManager()
    objects = models.Manager()

    def __str__(self):
        return self.title
    
    def get_photo(self):
        if self.image_url is None:
            return f'http://127.0.0.1:8000/media/{self.image}'
        return self.image_url
    
    def get_absolute_url(self):
        return reverse("full_news", args=[self.slug])
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email