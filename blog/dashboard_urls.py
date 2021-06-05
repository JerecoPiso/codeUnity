from django.conf.urls import url
from .views import dashboard_views

urlpatterns = [

     url(r'^$', dashboard_views.index, name='Home'),
     url(r'^projects', dashboard_views.projects, name="Projects"),
     url(r'^signup', dashboard_views.signup, name="Signup"),
     url(r'^questions', dashboard_views.questions, name="Questions"),
     url(r'^languages', dashboard_views.languages, name="Languages"),
     url(r'^login', dashboard_views.login, name="Login"),
     url(r'^home', dashboard_views.home, name="Home"),
     url(r'^logout', dashboard_views.logout, name="Home"),

     # updating database
     url(r'^updateLanguage', dashboard_views.updateLanguage, name="Update Language"),
     url(r'^updateFramework', dashboard_views.updateFramework, name="Update Framework"),
     url(r'^editQuestionCategory', dashboard_views.editQuestionCategory, name="Edit Question Category"),
     
     # getting data to database
     url(r'^getQuestions', dashboard_views.getQuestions, name="Get Questions"),
     url(r'^getCategory', dashboard_views.getCategory, name="Get Category"),
     url(r'^getFrameworks', dashboard_views.getFrameworks, name="Get Frameworks"),
     url(r'^getLanguages', dashboard_views.getLanguages, name="Get Languages"),
     url(r'^getProjects', dashboard_views.getProjects, name="Get Projects"),

     # adding data to database
     url(r'^addCategory', dashboard_views.addCategory, name="Add Category"),
     url(r'^addLanguage', dashboard_views.addLanguage, name="Add Language"),
     url(r'^addFramework', dashboard_views.addFramework, name="Add Framework"),

     # deleting data to database
     url(r'^deleteLanguage', dashboard_views.deleteLanguage, name="Delete Language"),
     url(r'^deleteFramework', dashboard_views.deleteFramework, name="Delete Language"),
     url(r'^deleteQuestionCategory', dashboard_views.deleteQuestionCategory, name="Delete Question Category"),

  
]
