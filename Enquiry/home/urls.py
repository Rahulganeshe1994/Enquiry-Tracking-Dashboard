from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addcourse', views.addcourse),
    path('showcourse', views.showcourse),
    path('showstudents', views.showstudents),
    path('payamount', views.payamount),
    path('showam', views.showam),
    path('searchenquiry', views.searchenquiry),
]