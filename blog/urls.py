from django.conf.urls import url
from .views import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     # url(r'^login', views.login, name="Login"),
     # url(r'^signup', views.signup, name="Signup"),
     url(r'^signup/(?P<redirectTo>.+)$', views.signup, name="Signup"),
     url(r'^register', views.register, name="Register"),
     url(r'^download/(?P<folder>.+)$', views.download, name="Download Project"),
     url(r'^verify', views.verify, name="Verify"),
     

     # url(r'^projects/language/(?P<toSearch>.+)$', views.filterProjects, name="Filter Projects"),
     # url(r'^projects/search/(?P<toSearch>.+)$', views.searchProject, name="Projects"),
     url(r'^projects/(?P<toGet>.+)/(?P<search>.+)$', views.getProjects, name="Filter Projects"),
     url(r'^projects', views.projects, name="Projects"),
   
     url(r'^logout/(?P<questionId>.+)$', views.logout, name="Projects"),
     # url(r'^questions/filter/(?P<filter>.+)$', views.filterQuestions, name="Search Question"),
     # url(r'^questions/tags/(?P<tag>.+)$', views.getQuestionByTags, name="Search Question"),
     
     url(r'^questions/(?P<toGetQuestion>.+)/(?P<value>.+)$', views.getQuestion, name="Search Question"),
     url(r'^question/(?P<id>.+)$', views.viewQuestion, name="View Question"),



     

     url(r'^questions', views.questions, name="Questions"),
     url(r'^error', views.error, name="Error"),
     url(r'^setAnswered', views.setAnswer, name="setAnsdfsdfswer"),
     url(r'^setUnanswered', views.setUnanswered, name="setAnsdfsdfswer"),
     url(r'^login/(?P<redirectTo>.+)$', views.login, name="Questions"),
     url(r'^userLogin/(?P<redirectTo>.+)$', views.userLogin, name="Questions"),
     url(r'^verified', views.verified, name="Verified"),
     url(r'^completeinfo', views.completeinfohtml, name="Complete Information HTML"),
     url(r'^setmoreinfo', views.setMoreInfo, name="Complete Information HTML"),
     url(r'^developers/rate/(?P<min>.+)/(?P<max>.+)$', views.searchDevsRate, name="Search"),

     # url(r'^userLogin', views.userLogin, name="User Login"),
     url(r'^developers/(?P<toGetDevelopers>.+)/(?P<value>.+)$', views.getDevelopers, name="Questions"),
     url(r'^developers', views.developers, name="Developers"),
     url(r'^addComment', views.addComment, name="Add Comment"),
     url(r'^getComment', views.getCom, name="Get Comments"),
     url(r'^getReply', views.getReply, name="Get Replies"),
     url(r'^deleteComment', views.deleteComment, name="Delete Comment"),
     url(r'^deleteReply', views.deleteReply, name="Delete Reply"),
     url(r'^reply', views.reply, name="Reply"),
     url(r'^project/(?P<project_name>.+)$', views.viewProject, name="View Project"),
     
     # url(r'^viewQuestion/(?P<id>.+)$', views.viewQuestion, name="View Question")
]
