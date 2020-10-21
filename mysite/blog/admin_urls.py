from django.conf.urls import url
from .views import user_views

urlpatterns = [

     url(r'^$', user_views.index, name='Home'),
     url(r'^projects', user_views.projects, name='Projects'),
     url(r'^get', user_views.get, name='Folder Upload'),
     url(r'^logout', user_views.logout, name='Logout'),
     url(r'^questions', user_views.questions, name='Questions'),
     url(r'^settings', user_views.settings, name='Settings')


   
]
