
#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('accounts/', include('accounts.urls')),
    path('main/', include('main.urls')),
    path('', views.homepage),

]

urlpatterns += staticfiles_urlpatterns()