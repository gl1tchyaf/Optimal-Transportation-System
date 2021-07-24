
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^main/', include('main.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),

]

urlpatterns += staticfiles_urlpatterns()
