from django.conf.urls import url
from .views import dashboard_views

urlpatterns = [

     url(r'^$', dashboard_views.index, name='Home'),
     url(r'^projects', dashboard_views.projects, name="Projects"),
     url(r'^questions', dashboard_views.questions, name="Questions"),
     url(r'^languages', dashboard_views.languages, name="Questions"),
     url(r'^getLanguages', dashboard_views.getLanguages, name="get"),
     url(r'^getProjects', dashboard_views.getProjects, name="get"),
     url(r'^addLanguage', dashboard_views.addLanguage, name="lANGUGE"),
     url(r'^deleteLanguage', dashboard_views.deleteLanguage, name="lANGUGE")
  
]
