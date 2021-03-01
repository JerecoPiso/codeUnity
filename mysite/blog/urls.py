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
     url(r'^questions', views.questions, name="Questions"),
     url(r'^verified', views.verified, name="Verified"),
     url(r'^userLogin', views.userLogin, name="User Login")
]
