from django.conf.urls import url
from . import views

urlpatterns = [
       	url(r'^info$', views.GetInfo.as_view(), name='info'),

     ]