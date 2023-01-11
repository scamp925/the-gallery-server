'''Imports for Product Model'''

from django.db import models
from .user import User

class Product(models.Model):
    '''Product Class'''
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    '''Line 13: When user is deleted, all associated products will also be deleted'''

@property
def price_display(self):
    '''Custom property to add the dollar sign ($) to the price amount'''
    return '$%s' % self.price
