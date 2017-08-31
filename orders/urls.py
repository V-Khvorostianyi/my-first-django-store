from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
]
