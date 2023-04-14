#We are now in our application. This File that takes us to different views.

#django stuff that processes urlpatterns
from django.urls import path

#Connects us to view.py file
from . import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Takes us to views in views.py
    #path('<str:UID>/<str:Model>/<str:UTC>/<str:TKN_ID>/<str:TAMP_CHCK>/', views.scanPage, name="scanPage"),
    path('', views.kickDScanPage, name="kickDScanPage"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)