'''Imports for Order Model'''
from django.db import models
from .user import User
from .payment_type import PaymentType
class Order(models.Model):
    '''Order Class'''
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    is_closed = models.BooleanField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    '''Line 9: When user is deleted, all associated orders will also be deleted'''
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    '''Line 11: When a payment type is trying to be deleted, a protect error will be triggered; thus, not allowing for the payment type to be deleted because the payment type is associated with an order. Payment type can be deleted after all associated orders are deleted first.'''

@property
def total_cost_display(self):
    '''Custom property to add the dollar sign ($) to the total cost amount'''
    return "$%s" % self.total_cost
