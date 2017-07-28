from django.shortcuts import render
from .forms import SubscribersForm
# Create your views here.
def store_page(request):
	c = {}
	name = "Slava"
	form = SubscribersForm(request.POST or None)
	if request.method == 'POST':
		print (request.POST)
		new_form = form.save()
	return render(request, 'store/store_page.html', {'form':form})
