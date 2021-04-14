from django.conf.urls import url
from .views import dashboard_views

urlpatterns = [

     url(r'^$', dashboard_views.index, name='Home'),
     url(r'^projects', dashboard_views.projects, name="Projects"),
     url(r'^questions', dashboard_views.questions, name="Questions"),
     url(r'^languages', dashboard_views.languages, name="Languages"),
     url(r'^getLanguages', dashboard_views.getLanguages, name="Get Languages"),
     url(r'^getProjects', dashboard_views.getProjects, name="Get Projects"),
     url(r'^getQuestions', dashboard_views.getQuestions, name="Get Questions"),
     url(r'^getCategory', dashboard_views.getCategory, name="Get Category"),
     url(r'^addLanguage', dashboard_views.addLanguage, name="Add Language"),
     url(r'^deleteLanguage', dashboard_views.deleteLanguage, name="Delete Language"),
     url(r'^deleteQuestionCategory', dashboard_views.deleteQuestionCategory, name="Delete Question Category"),
     url(r'^addCategory', dashboard_views.addCategory, name="Add Category"),
     url(r'^editQuestionCategory', dashboard_views.editQuestionCategory, name="Edit Question Category")
  
]
