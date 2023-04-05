from django.db import models


# Create your models here.
class PagePosts(models.Model):
    url = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    heading = models.CharField(max_length=500)
    body = models.TextField()
