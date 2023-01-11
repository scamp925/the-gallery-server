'''Imports for ProductOnOrder Model'''
from django.db import models
from .product import Product
from .order import Order

class ProductOnOrder(models.Model):
    '''ProductOnOrder Class'''
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
