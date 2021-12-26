from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    phone_name = models.CharField('phone_name', max_length=50)

