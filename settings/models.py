from django.db import models

# Create your models here.
class About (models.Model):
    blag_name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='about')
    subtitle = models.TextField(max_length=500)
    li_in_link = models.URLField()
    githup_link = models.URLField()
    whats_app_link = models.URLField()
    aboutme = models.TextField(max_length=10000)

    

