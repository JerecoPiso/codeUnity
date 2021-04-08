from django.conf.urls import url
from .views import user_views

urlpatterns = [

     url(r'^$', user_views.index, name='Home'),
     url(r'^projects', user_views.projects, name='Projects'),
     url(r'^uploadProject', user_views.uploadProject, name='Folder Upload'),
     url(r'^logout', user_views.logout, name='Logout'),
     url(r'^questions', user_views.questions, name='Questions'),
     url(r'^settings', user_views.settings, name='Settings'),
     url(r'^readFile', user_views.readFile, name='Read File'),
     url(r'^askQuestion', user_views.askQuestion, name='Read File'),
     url(r'^getProjects', user_views.getProject, name='Read File'),
     url(r'^getQuestions', user_views.getQuestions, name='Read File'),
     url(r'^deleteProject', user_views.deleteProject, name='Read File'),
     url(r'^deleteQuestion', user_views.deleteQuestion, name='Read File'),
     url(r'^project_files/(?P<folder>.+)$', user_views.project_files, name='Project Files')
]
