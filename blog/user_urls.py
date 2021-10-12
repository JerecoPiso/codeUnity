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
     url(r'^askQuestion', user_views.askQuestion, name='Ask Question'),

     # getting
     url(r'^getUserInfo', user_views.getUserInfo, name='Get Users Info'),
     url(r'^getProjects', user_views.getProject, name='Get Projects'),
     url(r'^getQuestions', user_views.getQuestions, name='Get Questions'),
     url(r'^getNotifications', user_views.getNotifications, name='Get Notifications'),
   

     # updating 
     url(r'^updateQuestion', user_views.updateQuestion, name="Update Question"),
     url(r'^editUsername', user_views.editUsername, name="Update Username"),
     url(r'^editPassword', user_views.editPassword, name="Update Password"),
     url(r'^updateInfo', user_views.updateInfo, name='Update More Info of the User'),
     url(r'^editProjectInfo', user_views.editProjectInfo, name='Update More Info of the User'),
     url(r'^editCode', user_views.editCode, name='Update File Code'),
     url(r'^changeDp', user_views.changeDp, name='Change Profile'),
     url(r'^updateResume', user_views.updateResume, name='Update Resume'),

     # deleting
     url(r'^deleteProject', user_views.deleteProject, name='Delete Project'),
     url(r'^deleteQuestion', user_views.deleteQuestion, name='Delete Question'),
     url(r'^deleteFile', user_views.deleteFile, name='Delete Question'),
     url(r'^clearnotifications', user_views.clearNotifs, name="Clear Notifications"),
     url(r'^deletenotification', user_views.deleteNotif, name="Clear Notifications"),
     url(r'^project_files/(?P<folder>.+)$', user_views.project_files, name='Project Files')
]
