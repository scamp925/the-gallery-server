'''Imports for User Model'''

from django.db import models

class User(models.Model):
    '''User Class'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    created_on = models.DateField()
    is_seller = models.BooleanField()
    uid = models.CharField(max_length=100)
