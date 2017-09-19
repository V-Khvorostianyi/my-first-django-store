from django.conf.urls import url, include
from orders import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]
