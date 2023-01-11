'''Imports for ProductOnOrder Model'''
from django.db import models
from .product import Product
from .order import Order

class ProductOnOrder(models.Model):
    '''ProductOnOrder Class'''
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    '''Line 8: When a product is trying to be deleted, a protect error will be triggered; thus, not allowing for the product to be deleted because the product is associated with an order. Product can be deleted after all associated orders are deleted first.'''
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    '''Line 10: When user is deleted, all associated orders will also be deleted'''
