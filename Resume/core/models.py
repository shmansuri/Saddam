from django.db import models

# Create your models here.

class Mymodel(models.Model):
    name = models.CharField(max_length=30)
    email= models.EmailField(max_length=100)
    sub = models.CharField(max_length=200)
    msg= models.TextField(max_length=500)
