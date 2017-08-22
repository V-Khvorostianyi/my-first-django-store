from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    short_description = models.TextField(max_length=200, blank=True, null = True, default = None)
    description = models.TextField(max_length=200, blank=True, null = True, default = None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "%s %s" % (self.name, self.price)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class ProductImage(models.Model):

    product= models.ForeignKey(Product,blank=True, default=None)
    image = models.ImageField(upload_to = 'product_img')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
