from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    return JsonResponse(return_dict)
