from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from  django.contrib.auth.models import User
from utils.main import disable_for_loaddata
import zeep

wsdl = 'https://dr-hml.neurotech.com.br/services/soap/porting?wsdl'
zeep.Client(wsdl=wsdl)


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
    user = models.ForeignKey(User, blank=True,null = True,default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costomer_name = models.CharField(max_length=200, blank=True, default=None)
    custormer_email = models.EmailField(blank=True, null = True,default=None)
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

        self.price = self.product.price_per_item
        self.total_price = int(self.qty) * self.price

        super(ProductInOrder, self).save(*args, **kwargs)

@disable_for_loaddata
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
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Product in Card'
        verbose_name_plural = 'Products in Card'

    def save(self, *args, **kwargs):

        self.price = self.product.price_per_item
        self.total_price = int(self.qty) * self.price

        super(ProductInCard, self).save(*args, **kwargs)
