from django.shortcuts import render
from .forms import SubscriberForm
# Create your views here.
def store_page(request):
	c = {}
	name = "Slava"
	form = SubscriberForm(request.POST or None)
	if request.method == 'POST':
		print (request.POST)
		new_form = form.save()
	return render(request, 'store/store_page.html', {'form':form})
