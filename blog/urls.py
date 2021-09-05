from django.conf.urls import url
from .views import views

urlpatterns = [
     # landing page
     url(r'^$', views.index, name='index'),
     # for the users action
     url(r'^signup/(?P<redirectTo>.+)$', views.signup, name="Signup"),
     url(r'^register', views.register, name="Register"),
     url(r'^login/(?P<redirectTo>.+)$', views.login, name="Login"),
     url(r'^userLogin/(?P<redirectTo>.+)$', views.userLogin, name="Login API"),
     url(r'^verified', views.verified, name="Verified"),
     url(r'^completeinfo', views.completeinfohtml, name="Complete Information HTML"),
     url(r'^setmoreinfo', views.setMoreInfo, name="Set Information HTML"),
     url(r'^verify', views.verify, name="Verify"),

     # logout for view question page
     url(r'^logout/(?P<questionId>.+)$', views.logout, name="Projects"),
     
     # for projects
     url(r'^projects/(?P<toGet>.+)/(?P<search>.+)$', views.getProjects, name="Filter Projects"),
     url(r'^projects', views.projects, name="Projects"),
     
     # view project
     url(r'^project/(?P<project_name>.+)$', views.viewProject, name="View Project"),

     # for questions
     url(r'^questions/(?P<toGetQuestion>.+)/(?P<value>.+)$', views.getQuestion, name="Get Question"),
     url(r'^questions', views.questions, name="Questions"),

     # view question
     url(r'^question/(?P<id>.+)$', views.viewQuestion, name="View Question"),
     url(r'^resume/(?P<owner>.+)/(?P<resume>.+)$', views.viewResume, name="View Question"),

     # setting the question to answered or unanswered
     url(r'^setAnswered', views.setAnswer, name="setAnswered"),
     url(r'^setUnanswered', views.setUnanswered, name="setUnAnswered"),

     # crud operation for the question
     url(r'^addComment', views.addComment, name="Add Comment"),
     url(r'^getComment', views.getCom, name="Get Comments"),
     url(r'^getReply', views.getReply, name="Get Replies"),
     url(r'^deleteComment', views.deleteComment, name="Delete Comment"),
     url(r'^deleteReply', views.deleteReply, name="Delete Reply"),
     url(r'^reply', views.reply, name="Reply"),

     # for developers
     url(r'^developers/rate/(?P<min>.+)/(?P<max>.+)$', views.searchDevsRate, name="Develoepers Rate"),
     url(r'^developers/(?P<toGetDevelopers>.+)/(?P<value>.+)$', views.getDevelopers, name="Get Developers"),
     url(r'^developers', views.developers, name="Developers"),

     # download project
     url(r'^download/(?P<folder>.+)$', views.download, name="Download Project"),

     # footer links
     url(r'^aboutus', views.aboutus, name="Download Project"),
     url(r'^termsandcontions', views.termsandconditions, name="Terms and Condition"),

     # for the error page
     url(r'^error', views.error, name="Error"),
    
]
