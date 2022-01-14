from django.db import models

# Create your models here.

class customer(models.Model):
    first_name = models.CharField('First Name', max_length=64, blank=True)
    last_name = models.CharField('Last Name', max_length=64, blank=True)
    phone = models.CharField('Primary Phone', max_length=12, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)