'''Imports for PaymentType Model'''

from django.db import models
from .user import User

class PaymentType(models.Model):
    '''PaymentType Class'''
    label = models.CharField(max_length=50)
    account_number = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    '''Line 10: When user is deleted, all associated payment types will also be deleted'''
