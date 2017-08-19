from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Product
# Create your views here.
def store_page(request):

	form = SubscriberForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		print(form.cleaned_data)
		data = form.cleaned_data
		print (request.POST)
		print (data["name"])
		form.save()
	return render(request, 'store/store_page.html', {'form':form})


def home(request):
	product = Product.objects.filter(is_active=True)
	return render(request, 'store/home.html', {'product':product})
