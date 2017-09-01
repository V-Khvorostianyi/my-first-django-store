from django.contrib import admin
from .models import *


# Register your models here.
class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0
#____________________________________________________________________
class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)
#__________________________________________________________________

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)
#_________________________________________________

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)
#_________________________________________________

class ProductInCardAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInCard._meta.fields]

    class Meta:
        model = ProductInCard

admin.site.register(ProductInCard, ProductInCardAdmin)
