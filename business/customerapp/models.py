"""
The models.py contains various models under the customer app.
"""
from django.db import models


class Customer(models.Model):
    """
    Store Customer data like first name, last name, phone number and email id. 
    """
    first_name = models.CharField('First Name', max_length=64, blank=True)
    last_name = models.CharField('Last Name', max_length=64, blank=True)
    phone = models.CharField('Primary Phone', max_length=12, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)

    def __str__(self):
        return self.first_name 
