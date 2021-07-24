from django.conf.urls import url
from . import views

app_name = 'articles'


urlpatterns = [
    url(r'^$', views.homepage, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.articles_details, name="detail"),
]
