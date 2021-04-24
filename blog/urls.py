from django.conf.urls import url
from .views import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^login', views.login, name="Login"),
     url(r'^signup', views.signup, name="Signup"),
     url(r'^register', views.register, name="Register"),
     url(r'^download/(?P<folder>.+)$', views.download, name="Download Project"),
     url(r'^verify', views.verify, name="Verify"),
     url(r'^projects', views.projects, name="Projects"),
     url(r'^filterProjects/(?P<toSearch>.+)$', views.filterProjects, name="Filter Projects"),
     url(r'^questions', views.questions, name="Questions"),
     url(r'^verified', views.verified, name="Verified"),
     url(r'^userLogin', views.userLogin, name="User Login"),
     url(r'^developers', views.developers, name="Developers"),
     url(r'^addComment', views.addComment, name="Add Comment"),
     url(r'^getComment', views.getCom, name="Get Comments"),
     url(r'^getReply', views.getReply, name="Get Replies"),
     url(r'^deleteComment', views.deleteComment, name="Delete Comment"),
     url(r'^deleteReply', views.deleteReply, name="Delete Reply"),
     url(r'^reply', views.reply, name="Reply"),
     url(r'^viewProject/(?P<id>.+)$', views.viewProject, name="View Project"),
     url(r'^viewQuestion/(?P<id>.+)$', views.viewQuestion, name="View Question")
]
