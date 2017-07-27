from django.shortcuts import render

# Create your views here.
def store_page(request):
	c = {}
	name = "Slava"
	return render(request, 'store/store_page.html', locals())
