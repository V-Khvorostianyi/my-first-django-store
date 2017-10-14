from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^landing/$', views.store_page, name='store_page'),

              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

