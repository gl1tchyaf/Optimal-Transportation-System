
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^main/', include('main.urls')),
    url(r'^$', views.homepage),
    url(r'^about/$', views.about),

]

urlpatterns += staticfiles_urlpatterns()
