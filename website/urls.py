from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
     path('privacy.html',views.privacy,name="privacy"),
     path('aboutus.html',views.aboutus,name="aboutus"),
     path('contactus.html',views.contactus,name="contactus"),
     path('clients.html',views.clients,name="clients"),
     path('services.html',views.services,name="services"),
     
]