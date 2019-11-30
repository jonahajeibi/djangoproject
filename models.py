from django.db import models

# Create your models here.

class Companies(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    img = models.ImageField(upload_to='pics')
    website = models.CharField(max_length=100)


class Companiess(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    img = models.ImageField(upload_to='pics')
    website = models.CharField(max_length=100)

class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()