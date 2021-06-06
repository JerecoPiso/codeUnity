from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from pathlib import Path
import os, datetime, json
from blog.models import Projects, Questions, Question_Category, Developers, Replies, Comments
from django.conf import settings
from django.core.files.storage import FileSystemStorage

rootDir = ""

# asking question
def askQuestion(request):
    try:

        if request.method == "POST":
            # months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
            # d = int(datetime.datetime.now().strftime("%m"))
            
            datenow =  datetime.datetime.now().strftime("%Y") + "-" + datetime.datetime.now().strftime("%m") + "-"+ datetime.datetime.now().strftime("%d") + " " + datetime.datetime.now().strftime("%H")+ ":" + datetime.datetime.now().strftime("%M")+ ":" + datetime.datetime.now().strftime("%S")
            ask = Questions(question=request.POST['question'], views=0, category = request.POST['category'], asker_id=request.session['id'], date = datenow, code=request.POST['code'], language=request.POST['language'], comments = 0, tags = request.POST['tags'])
            ask.save()
            return HttpResponse('Asked successfully')

    except:
        
        return HttpResponse("Failed")
# main page of the user
def index(request):
    request.session['title'] = "Home"
    if request.session.get("loggin"):
         project = Projects.objects.filter(uploader_id__exact=request.session['id']).count()
         question = Questions.objects.filter(asker_id__exact=request.session['id']).count()
         return render(request, 'html/user_pages/index.html', {'project_total': project, 'question_total': question})
    else:
         return redirect("/login/user")

# projects of the user
def projects(request):
    if request.session.get("loggin"):
        request.session['title'] = "Projects"
        count = Projects.objects.filter(uploader_id__exact=request.session['id']).count()
        proj = Projects.objects.filter(uploader_id__exact=request.session['id'])
        return render(request, 'html/user_pages/projects.html', {'myproject':proj, 'count': count})
    else:
         return redirect("/login/user")

# opening the file from a project
def readFile(request):

    path = request.POST['path']
    temp_path = path.replace(request.POST['fname'], "temporary")
    new_path = temp_path.replace("%", "\\")
    cd = os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'\\'+new_path.replace("temporary", request.POST['fname']))

    os.chdir(cd.replace(request.POST['fname'], ""))
    file = open(request.POST['fname'], "r+")
    ret = file.read()
    file.close()
    os.chdir(os.path.join(Path(__file__).resolve().parent.parent.parent))
    return HttpResponse(str(ret))

# getting the directories and files the users project
def project_files(request, folder):
    request.session['title'] = folder
    context = {}
    folder_checker = folder.find("%")
    if folder_checker < 0:
        request.session['app'] = folder
        total = Projects.objects.get(project_name__exact=folder)
        request.session['total_download'] = total.downloads

    rep = folder.replace("%", "\\")
    subFolders = []
    files = []
    folder_name = []
    file_name = []
    rootDir = os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'\\'+rep.replace('project_files/', '')+'\\')
    dirs = os.listdir(rootDir)
   
    for file in dirs:
      ctr = file.rfind('.', 0, len(file))
      if ctr < 0:
        subFolders.append(rep.replace("\\","%")+'%'+file)
        folder_name.append(file)
      else:
        files.append(rep.replace("\\","%")+'%'+file)
        file_name.append(file)
    
    
    context['folders'] = subFolders
    context['files'] = files
    context['folder_name'] = folder_name
    context['file_name'] = file_name
    context['projects'] = Projects.objects.all()

    return render(request, 'html/user_pages/project_files.html', context)

def questions(request):
    if request.session.get("loggin"):
        request.session['title'] = "Questions"
        total_question = Questions.objects.filter(asker_id__exact=request.session['id']).count()
        myquestion = Questions.objects.all()
        return render(request, 'html/user_pages/questions.html', {'myquestions': myquestion, 'total_question': total_question})
    else:
        return redirect("/login/user")    
  

def getQuestions(request):
    try:
        ques = Questions.objects.filter(asker_id__exact=request.session['id']).values()
        return JsonResponse(list(ques), safe=False)

    except:

        return HttpResponse("Failed")

def getOtherInfo(request):
    try:
        infos = Developers.objects.filter(id=request.session['id']).values()
        
        return JsonResponse(list(infos), safe=False)

    except:

        return HttpResponse("Failed")

def deleteQuestion(request):
    try:
        ques = Questions.objects.get(id=request.POST['id'])
        ques.delete()
        dell = Developers.objects.get(id=16)
        dell.delete()
        return HttpResponse("Deleted successfully")
    
    except:
        return HttpResponse("An error has occurred!")

def deleteProject(request):
    try:
        project = Projects.objects.get(id=request.POST['id'])
        
        if os.path.exists(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+project.project_name):

            for root, dirs, files in  os.walk(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+project.project_name, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+project.project_name)
            project.delete()

        else:
            return HttpResponse("Path didn't exists!")

        return HttpResponse("Deleted successfully")
    
    except:
        return HttpResponse("An error has occurred!"+str(os.rmdir(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/'))))

# uploading project
def uploadProject(request):
    folderSize = 0
    if request.method == 'POST':
        
        dir=request.FILES
        dirlist=dir.getlist('files')

        pathlist=request.POST.getlist('paths')
        
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
              
            for root, dirs, files in  os.walk(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+request.POST['project_name'], topdown=False):
                for name in files:
                    folderSize = int(os.path.getsize(os.path.join(root, name))) + folderSize
              

            if folderSize > 10457600:
                return HttpResponse("File size must not be greater than 10MB!!")
            else:
                upload_file = request.FILES['photo']  
                extension = os.path.splitext(upload_file.name)[1]
                rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
                fss = FileSystemStorage()
                filename = fss.save(rename, upload_file)
                upload_file_path = fss.path(filename)
                project = Projects(project_name=request.POST['project_name'], uploader_id=request.session['id'], downloads = 0, about=request.POST['about'], photo = rename, language=request.POST['language'], views = 0, more = request.POST['more'])
                project.save()     
                return HttpResponse("Uploaded successfully")
      
 
    return HttpResponse("An error has occurred!")
def changeDp(request):
    if request.method == "POST":
        dev = Developers.objects.get(id__exact=request.session['id']) 
        if os.path.exists(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+str(dev.photo)):

            upload_file = request.FILES["photo"]
            extension = os.path.splitext(upload_file.name)[1]
            rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
            fss = FileSystemStorage()
            filename = fss.save(rename, upload_file)
            upload_file_path = fss.path(filename)
            if dev.photo != "dp.jpg":
                os.remove(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+str(dev.photo))
            dev.photo = rename
            dev.save()

        else:

            return HttpResponse("Path did'nt exists!")

        return HttpResponse("Saved")
    else:
        return HttpResponse("eRROR")


# user logout
def logout(request):
    try:
        del request.session['loggin']
        del request.session['id']
        del request.session['username']

    except:
        pass

    return redirect('/login/user')

def settings(request):
    if request.session.get("loggin"):
        request.session['title'] = "Settings"
        return render(request, 'html/user_pages/settings.html')
    else:
        return redirect("/login/user")   

def getProject(request):
    projects = Projects.objects.filter(uploader_id__exact=request.session['id']).values()
    return JsonResponse(list(projects), safe=False)

def getUser(request):
    user = Developers.objects.filter(id__exact=request.session['id']).values()
    return JsonResponse(list(user), safe=False)

def updateInfo(request):
    try:
        info = Developers.objects.get(id=request.session['id'])
        info.skills = request.POST['skills']
        info.expertise = request.POST['expertise']
        info.aboutme = request.POST['aboutme']
        info.save()
        return HttpResponse("Success")
    except:
        return HttpResponse("Failed")