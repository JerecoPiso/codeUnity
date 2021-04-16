from django.conf.urls import url
from .views import admin_views

urlpatterns = [

     url(r'^$', admin_views.index, name='Home'),
  
  
]
