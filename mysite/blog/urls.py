from django.conf.urls import url
from .views import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^login', views.login, name="Login"),
     url(r'^signup', views.signup, name="Signup"),
     url(r'^register', views.register, name="Register"),
     url(r'^upload', views.folderUpload, name="upload"),
     url(r'^get', views.get, name="Register"),
     url(r'^download/(?P<folder>.+)$', views.download, name="Download Project"),
     url(r'^sendEmail', views.sendEmail, name="sendEmail"),
     url(r'^verify', views.verify, name="Verify"),
     url(r'^projects', views.projects, name="Projects"),
     url(r'^jobs', views.jobs, name="Jobs"),
     url(r'^questions', views.questions, name="Questions"),
     url(r'^userLogin', views.userLogin, name="User Login")
]
