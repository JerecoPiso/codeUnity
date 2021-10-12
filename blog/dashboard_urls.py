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
     url(r'^developers', dashboard_views.developers, name="Home"),
     url(r'^logout', dashboard_views.logout, name="Home"),
     url(r'^userprofile', dashboard_views.userprofile, name="User Profile"),

     # updating database
     url(r'^updateLanguage', dashboard_views.updateLanguage, name="Update Language"),
     url(r'^updateFramework', dashboard_views.updateFramework, name="Update Framework"),
     url(r'^editQuestionCategory', dashboard_views.editQuestionCategory, name="Edit Question Category"),
     url(r'^editname', dashboard_views.editname, name="Edit Username"),
     url(r'^changedp', dashboard_views.changeDp, name="Change Profile"),
     url(r'^changepass', dashboard_views.changepass, name="Change Password"),
     
     # getting data to database
     url(r'^getQuestions', dashboard_views.getQuestions, name="Get Questions"),
     url(r'^getCategory', dashboard_views.getCategory, name="Get Category"),
     url(r'^getFrameworks', dashboard_views.getFrameworks, name="Get Frameworks"),
     url(r'^getLanguages', dashboard_views.getLanguages, name="Get Languages"),
     url(r'^getProjects', dashboard_views.getProjects, name="Get Projects"),
     url(r'^getMostDownloadedApp', dashboard_views.getMostDownloadedApp, name="getMostDownloadedApp"),
     url(r'^getMostViewedQuestions', dashboard_views.getMostViewedQuestions, name="getMostViewedQuestions"),
     url(r'^getDevs', dashboard_views.getDevs, name="getDevs"),
     url(r'^getAdminInfo', dashboard_views.getAdminInfo, name="Get Admin Info"),
     url(r'^getDevices', dashboard_views.getDevices, name="getDevs"),
     url(r'^yearlyVisitors', dashboard_views.getYearlyVisitors, name="Yearly Visitors"),

     # adding data to database
     url(r'^addCategory', dashboard_views.addCategory, name="Add Category"),
     url(r'^addLanguage', dashboard_views.addLanguage, name="Add Language"),
     url(r'^addFramework', dashboard_views.addFramework, name="Add Framework"),
     url(r'^setDevice', dashboard_views.setDevice, name="Add Device"),

     # deleting data to database
     url(r'^deleteLanguage', dashboard_views.deleteLanguage, name="Delete Language"),
     url(r'^deleteFramework', dashboard_views.deleteFramework, name="Delete Language"),
     url(r'^deleteQuestionCategory', dashboard_views.deleteQuestionCategory, name="Delete Question Category"),


  
]
