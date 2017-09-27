
from django.shortcuts import render
from products.models import *
from orders.views import *
from .forms import *

def product(request, product_id):
    form = SetQtyProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
    product = Product.objects.get(id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    return render(request, 'products/product.html', locals())

