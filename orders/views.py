from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from  .models import ProductInCard
# Create your views here.
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)

    ProductInCard.objects.get(session_key=session_key)
    return JsonResponse(return_dict)
