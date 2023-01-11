'''Imports for Order Model'''
from django.db import models
from .user import User
from .payment_type import PaymentType
class Order(models.Model):
    '''Order Class'''
    customer_id = models.ForeignKey(User, on_delete=models.PROTECT)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    is_closed = models.BooleanField()

@property
def total_cost_display(self):
    '''Custom property to add the dollar sign ($) to the total cost amount'''
    return "$%s" % self.total_cost
