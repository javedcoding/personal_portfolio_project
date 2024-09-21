from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Expertise(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    icon = models.CharField(max_length=150, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Certificate(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.URLField()
    icon = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title