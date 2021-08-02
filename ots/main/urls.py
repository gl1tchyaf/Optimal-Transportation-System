from django.conf.urls import url
from . import views

app_name = 'articles'


urlpatterns = [
    url(r'^$', views.homepage, name="list"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^(?P<slug>[\w-]+)/$', views.bus_details, name="detail"),
]
