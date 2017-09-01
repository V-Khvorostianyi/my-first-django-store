from django.db import models
from products.models import Product
from django.db.models.signals import post_save


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
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
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

    def save(self, *args, **kwargs):


        super(Order, self).save(*args, **kwargs)



class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, default=None)
    product = models.ForeignKey(Product, blank=True, default=None)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add = True,auto_now = False)
    updated = models.DateTimeField(auto_now_add = False,auto_now = True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Product in Order'
        verbose_name_plural = 'Products in Order'

    def save(self, *args, **kwargs):

        self.price = self.product.price
        self.total_price = self.qty * self.price

        super(ProductInOrder, self).save(*args, **kwargs)

def product_post_save(sender, instance, **kwargs):

    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_post_save, sender=ProductInOrder)

class ProductInCard(models.Model):
    order = models.ForeignKey(Order, blank=True, default=None)
    product = models.ForeignKey(Product, blank=True, default=None)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add = True,auto_now = False)
    updated = models.DateTimeField(auto_now_add = False,auto_now = True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Product in Card'
        verbose_name_plural = 'Products in Card'


