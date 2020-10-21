from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import User, Developers
from django.core.files.storage import FileSystemStorage
import os, datetime, json, zipfile, tempfile, mimetypes
from django.conf import settings
from django.contrib import messages
import io, smtplib, ssl

def index(request):

    if request.session.get("loggin"):
         return render(request, 'html/user_pages/index.html')
    else:
         return redirect("/codeunity/login")

def projects(request):
	return render(request, 'html/user_pages/projects.html')

def questions(request):
    return render(request, 'html/user_pages/questions.html')

def get(request):
    if request.method == 'POST':
        
        dir=request.FILES
        dirlist=dir.getlist('files')

        pathlist=request.POST.getlist('paths')
        # print(pathlist[0].find('/'))

    
        if not dirlist:
            return HttpResponse( 'files not found')
        else:
 
            for file in dirlist:
                position = os.path.join(os.path.abspath(os.path.join(os.getcwd(),'media')),'/'.join(pathlist[dirlist.index(file)].split('/')[:-1]))
                
                if not os.path.exists(position):
                    os.makedirs(position)
                storage = open(position+'/'+file.name, 'wb+')    
                for chunk in file.chunks():          
                    storage.write(chunk)
                storage.close()                 
            return HttpResponse("1")
      
 
    return HttpResponse("hha")

def logout(request):
    try:
        del request.session['loggin']

    except:
        pass

    return redirect('/codeunity/login')

def settings(request):
    return render(request, 'html/user_pages/settings.html')