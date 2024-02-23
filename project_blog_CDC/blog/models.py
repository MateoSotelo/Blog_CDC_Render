from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    imageURL = models.CharField(null = True, max_length=50)

    def __str__(self):
        return self.title