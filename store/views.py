from django.shortcuts import render

import orders
from .forms import SubscriberForm
from products.models import *
from orders.views import *


# Create your views here.
def store_page(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(form.cleaned_data)
        data = form.cleaned_data
        print(request.POST)
        print(data["name"])
        form.save()
    return render(request, 'store/store_page.html', {'form': form})


def home(request):
    product_image = ProductImage.objects.filter(is_active=True, is_main=True, product__category__is_active=True)
    product_image_phone = ProductImage.objects.filter(product__category_id=1, is_active=True, is_main=True,
                                                      product__category__is_active=True)
    product_image_laptop = ProductImage.objects.filter(product__category__id=2, is_active=True, is_main=True,
                                                       product__category__is_active=True)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    return render(request, 'store/home.html', locals())
