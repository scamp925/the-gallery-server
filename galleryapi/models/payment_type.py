'''Imports for PaymentType Model'''

from django.db import models
from .user import User

class PaymentType(models.Model):
    '''PaymentType Class'''
    label = models.CharField(max_length=50)
    account_number = models.IntegerField()
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
