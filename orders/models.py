from django.db import models
from products.models import Product
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=20, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Status of order'
        verbose_name_plural = 'Statuses of order'

class Order(models.Model):
    total_prise = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costomer_name = models.CharField(max_length=200, blank=True, default=None)
    custormer_email = models.EmailField(blank=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, default=None)
    customer_address = models.CharField(max_length=128, null = True, blank=True, default=None)
    comments = models.TextField(max_length=200, blank=True, null = True, default = None)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add = True,auto_now = False)
    updated = models.DateTimeField(auto_now_add = False,auto_now = True)


    def __str__(self):
    	return "Order %s Status %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, default=None)
    product = models.ForeignKey(Product, blank=True, default=None)
    qty = models.IntegerField(default=1)
    prise = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_prise = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add = True,auto_now = False)
    updated = models.DateTimeField(auto_now_add = False,auto_now = True)


    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Product in Order'
        verbose_name_plural = 'Products in Order'
