from django.db import models

# Create your models here.
class Std(models.Model):
    sname = models.CharField(max_length=10)
    snum = models.IntegerField()
    scourse = models.CharField(max_length=100)
    sadd = models.CharField(max_length=200)
    

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
        
