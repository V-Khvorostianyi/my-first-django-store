from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
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
        ProductInCard.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInCard.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, defaults={'qty':qty} )
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
        product_dict["qty"] = item.qty
        product_dict["id"] = item.id
        product_dict["total_price"] = item.total_price
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)
