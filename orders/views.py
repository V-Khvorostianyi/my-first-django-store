from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from  django.contrib.auth.models import User
# Create your views here.
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    data = request.POST
    product_id = data.get('product_id')
    qty = data.get('qty')
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInCard.objects.filter(id = product_id).update(is_active=False)

    else:
    #     some code
        new_product, created = ProductInCard.objects.get_or_create(session_key=session_key,is_active = True, product_id=product_id,defaults={'qty':qty} )
        if not created:
            new_product.qty +=int(qty)
            new_product.save(force_update=True)

    products_in_card = ProductInCard.objects.filter(session_key=session_key, is_active=True)
    products_total_qty = products_in_card.count()
    return_dict["products_total_qty"] = products_total_qty

    return_dict["products"] = list()

    for item in products_in_card:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["id"] = item.id
        product_dict["qty"] = item.qty
        product_dict["total_price"] = item.total_price
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)

def checkout(request):
    session_key = request.session.session_key
    product_in_card = ProductInCard.objects.filter(session_key=session_key,is_active = True)
    form = CheckoutContactForm(request.POST or None)
    if (request.POST):
        print(request.POST)
        if (form.is_valid()):
            print("yes")
            data = request.POST
            phone = data['phones']
            name = data['name']
            user, created = User.objects.get_or_create(username = phone, defaults={"first_name":name})

            # for item in data:
            #     if item.startwith("")
        else:
            print("no")
    return render(request, 'orders/checkout.html', locals())