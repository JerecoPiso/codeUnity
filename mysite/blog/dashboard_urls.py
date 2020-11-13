from django.conf.urls import url
from .views import dashboard_views

urlpatterns = [

     url(r'^$', dashboard_views.index, name='Home'),
  
]
