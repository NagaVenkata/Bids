'''
Created on Aug 17, 2016

@author: Umapathi
'''
from django.conf.urls import url

from Bids import views

urlpatterns = [
   
    url(r'^$',views.main),
    url(r'^login/$',views.loginUser,name="login"),
    url(r'^logout$',views.logoutUser,name="logout"),
    url(r'^register/$',views.register,name="register"),
    url(r'^addItems$',views.addItem,name="addItems"),
    url(r'^bidItems/$',views.bidItem,name="bidItems"),
]