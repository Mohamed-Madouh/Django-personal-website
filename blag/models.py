from django.db import models
from django.utils import timezone
# Create your models here.
class post (models.Model):
    titel = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')
    puplish_date = models.DateTimeField(default=timezone.now )
    content = models.TextField(max_length=100000)

    def __str__(self):
        return self.titel


