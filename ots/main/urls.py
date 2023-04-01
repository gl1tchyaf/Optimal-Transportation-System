#from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'articles'


urlpatterns = [
    path('', views.homepage, name="list"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('bolaka/', views.bolaka, name="bolaka"),
    path('offers_page/', views.offers, name="offers_page"),
    path('bolakareview/', views.bolakareview, name="bolakareview"),
    path('ticket/', views.ticket, name="ticket"),
    path('deletebalaka/<str:pk>/', views.deletebalaka, name="deletebalaka"),
    path('ticket_page/', views.ticket_page, name="ticket_page"),


    # Air
    path('Air_Biman_Bangladesh/', views.Air_Biman_Bangladesh, name="Air_Biman_Bangladesh"),
    path('Air_Novoair/', views.Air_Novoair, name="Air_Novoair"),
    path('Air_US_Bangla/', views.Air_US_Bangla, name="Air_US_Bangla"),

    # Bus
    path('Bus_Akash/', views.Bus_Akash, name="Bus_Akash"),
    path('Bus_Alif/', views.Bus_Alif, name="Bus_Alif"),
    path('Bus_Anabil/', views.Bus_Anabil, name="Bus_Anabil"),
    path('Bus_BRTC/', views.Bus_BRTC, name="Bus_BRTC"),
    path('Bus_Green_Dhaka/', views.Bus_Green_Dhaka, name="Bus_Green_Dhaka"),
    path('Bus_Raida/', views.Bus_Raida, name="Bus_Raida"),
    path('Bus_Skyline/', views.Bus_Skyline, name="Bus_Skyline"),
    path('Bus_Supravat/', views.Bus_Supravat, name="Bus_Supravat"),
    path('Bus_VIP/', views.Bus_VIP, name="Bus_VIP"),

    # Train
    path('Train_Chitra_Express/', views.Train_Chitra_Express, name="Train_Chitra_Express"),
    path('Train_Ekota_Express/', views.Train_Ekota_Express, name="Train_Ekota_Express"),
    path('Train_Mahanagar_Godhuli/', views.Train_Mahanagar_Godhuli, name="Train_Mahanagar_Godhuli"),
    path('Train_Suborno_Express/', views.Train_Suborno_Express, name="Train_Suborno_Express"),
    path('Train_Tista_Express/', views.Train_Tista_Express, name="Train_Tista_Express"),

    path('(?P<slug>[\w-]+)/', views.homepage, name="list"),
]
