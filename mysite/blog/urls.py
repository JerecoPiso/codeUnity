from django.conf.urls import url
from .views import views
urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^login', views.login, name="Login"),
     url(r'^signup', views.signup, name="Signup"),
     url(r'^register', views.register, name="Register"),
     url(r'^upload', views.folderUpload, name="Register"),
     url(r'^get', views.get, name="Register"),
     url(r'^download', views.download, name="Register"),
     url(r'^sendEmail', views.sendEmail, name="sendEmail")
]
