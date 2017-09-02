from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from  .models import ProductInCard
# Create your views here.
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    data = request.POST
    product_id = data.get('product_id')
    qty = data.get('qty')
    new_product = ProductInCard.objects.create(session_key=session_key,product_id=product_id,qty=qty )
    products_in_card = ProductInCard.objects.filter(session_key=session_key, is_active=True)
    products_total_qty = products_in_card.count()
    return_dict["products_total_qty"] = products_total_qty
    return JsonResponse(return_dict)
