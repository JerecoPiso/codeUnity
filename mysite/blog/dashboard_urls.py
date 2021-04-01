from django.conf.urls import url
from .views import dashboard_views

urlpatterns = [

     url(r'^$', dashboard_views.index, name='Home'),
     url(r'^projects', dashboard_views.projects, name="Projects"),
     url(r'^questions', dashboard_views.questions, name="Questions"),
     url(r'^languages', dashboard_views.languages, name="Questions"),
     url(r'^getLanguages', dashboard_views.getLanguages, name="get"),
     url(r'^getProjects', dashboard_views.getProjects, name="get"),
     url(r'^getQuestions', dashboard_views.getQuestions, name="get"),
     url(r'^getCategory', dashboard_views.getCategory, name="get"),
     url(r'^addLanguage', dashboard_views.addLanguage, name="lANGUGE"),
     url(r'^deleteLanguage', dashboard_views.deleteLanguage, name="lANGUGE"),
     url(r'^deleteQuestionCategory', dashboard_views.deleteQuestionCategory, name="lANGUGE"),
     url(r'^addCategory', dashboard_views.addCategory, name="lANGUGE"),
     url(r'^editQuestionCategory', dashboard_views.editQuestionCategory, name="lANGUGE")
  
]
