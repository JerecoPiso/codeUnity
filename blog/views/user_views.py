from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from pathlib import Path
import os, datetime, json
from blog.models import Projects, Questions, Question_Category, Developers, Replies, Comments, Notifications
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from django.db.models import Q
rootDir = ""

# asking question
def askQuestion(request):
    try:

        if request.method == "POST":
            # months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
            # d = int(datetime.datetime.now().strftime("%m"))
            
            # datenow =  datetime.datetime.now().strftime("%Y") + "-" + datetime.datetime.now().strftime("%m") + "-"+ datetime.datetime.now().strftime("%d") + " " + datetime.datetime.now().strftime("%H")+ ":" + datetime.datetime.now().strftime("%M")+ ":" + datetime.datetime.now().strftime("%S")
            ask = Questions(question=request.POST['question'], views=0, category = request.POST['category'], asker_id=request.session['id'], date = request.POST['date'], code=request.POST['code'], language=request.POST['language'], comments = 0, tags = request.POST['tags'])
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
        #  Notifications.objects.filter(Q(notified_id__exact=request.session['id']) & Q(status="unread"))
         total_notifications = Notifications.objects.filter(Q(notified_id__exact=request.session['id']) & Q(status="unread")).count()
         
         return render(request, 'html/user_pages/index.html', {'total_notifications': total_notifications,'project_total': project, 'question_total': question})
    else:
         return redirect("/login/user")

# projects of the user
def projects(request):
    # pro  = Projects.objects.get(id=95)
    # pro.delete()
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
    # print(cd)
    os.chdir(cd.replace(request.POST['fname'], ""))
    file = open(request.POST['fname'], "r+")
    ret = file.read()
    file.close()
    # os.chdir(os.path.join(Path(__file__).resolve().parent.parent.parent))
    return JsonResponse({'code': str(ret), 'filename': cd})
    # return HttpResponse(str(ret))

# delete file
def deleteFile(request):
    ret_msg = ""
    try:
        cd = os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'\\'+request.POST['filename'])
        # os.remove(cd)
        if os.path.exists(cd):
           os.remove(cd)
           ret_msg = "Success"
        else:
           ret_msg = "File doesn't exists!"
        
    except: 
        ret_msg = "Unable to delete file!"
    return HttpResponse(ret_msg)
# edit the file code
def editCode(request):
    try:
         fileCode =  open(request.POST['filePath'], "w")
         fileCode.write(request.POST['code'])
         fileCode.close()
         return HttpResponse("File updated successfully")
    except:
         return HttpResponse("Unable to update file!")


# getting the directories and files the users project
def project_files(request, folder):
    request.session['title'] = "Project Files"
    context = {}
    getProjectName = folder.find("%", 0, len(folder))
   
    folder_checker = folder.find("%")
    if folder_checker < 0:
        request.session['app'] = folder
        if getProjectName == -1:
            proj = Projects.objects.get(project_name__exact=folder)
        else:
            proj = Projects.objects.get(project_name__exact=folder[0:getProjectName])
        
        request.session['total_download'] = proj.downloads
        request.session['language'] = proj.language
        


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

# questions page of the user
def questions(request):
    if request.session.get("loggin"):
        request.session['title'] = "Questions"
        total_question = Questions.objects.filter(asker_id__exact=request.session['id']).count()
        myquestion = Questions.objects.all()
        return render(request, 'html/user_pages/questions.html', {'myquestions': myquestion, 'total_question': total_question})
    else:
        return redirect("/login/user")    
  
# get the questions asked by the current user
def getQuestions(request):
    try:
        ques = Questions.objects.filter(asker_id__exact=request.session['id']).values()
        return JsonResponse(list(ques), safe=False)

    except:

        return HttpResponse("Failed")

# get the users info of the current user
def getUserInfo(request):
    try:
        infos = Developers.objects.filter(id=request.session['id']).values()
        
        return JsonResponse(list(infos), safe=False)

    except:

        return HttpResponse("Failed")

# deleting question
def deleteQuestion(request):
    try:
        ques = Questions.objects.get(id=request.POST['id'])
        ques.delete()
        return HttpResponse("Deleted successfully")
    
    except:
        return HttpResponse("An error has occurred!")

# deleting project
def deleteProject(request):
    try:
        project = Projects.objects.get(id=request.POST['id'])
        # project = Projects.objects.filter(uploader_id=request.session['id'])
        # project.delete()
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
        return HttpResponse("An error has occurred!")

def editProjectInfo(request):
    try:
        if request.POST['project_name'] != "" and request.POST['language'] != "" and request.POST['id'] != 0:
            project = Projects.objects.get(id=request.POST['id'])
            project.project_name = request.POST['project_name']
            project.language = request.POST['language']
            project.more = request.POST['more']
            project.about = request.POST['about']
            project.save()
            return HttpResponse("Success")
        else:
            return HttpResponse("Failed to update!")
    except:
        return HttpResponse("An error has occured!")
# uploading project
def uploadProject(request):
    folderSize = 0
    if request.method == 'POST':
        # check if folder name already exists
        checkFolderName = Projects.objects.filter(project_name__exact=request.POST['project_name']).count()
    
        if checkFolderName == 0:

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
                    fss.save(rename, upload_file)
                    # filename = 
                    # upload_file_path = fss.path(filename)
                    project = Projects(project_name=request.POST['project_name'], uploader_id=request.session['id'], downloads = 0, about=request.POST['about'], photo = rename, language=request.POST['language'], date = request.POST['date'], views = 0, more = request.POST['more'])
                    project.save()     
                    return HttpResponse("Uploaded successfully")
        else:
            return HttpResponse("Folder name aldready exists.")
 
    return HttpResponse("An error has occurred!")

# changing profile of the current user
def changeDp(request):
    if request.method == "POST":
        dev = Developers.objects.get(id__exact=request.session['id']) 
        if os.path.exists(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+str(dev.photo)):

            upload_file = request.FILES["photo"]
            extension = os.path.splitext(upload_file.name)[1]
            rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
            fss = FileSystemStorage()
            fss.save(rename, upload_file)
            # upload_file_path = fss.path(filename)
 
            if str(dev.photo) != "dp.jpg":
                os.remove(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+str(dev.photo))
            dev.photo = rename
            dev.save()

        else:

            return HttpResponse("Path did'nt exists!")

        return HttpResponse("Saved")
    else:
        return HttpResponse("Error")


# user logout
def logout(request):
    toLogout = request.session['toLogout']
    try:
        del request.session['loggin']
        del request.session['id']
        del request.session['username']
        del request.session['photo']
        del request.session['toLogout']
    except:
        pass

    return redirect('/login/'+toLogout)

def settings(request):
    if request.session.get("loggin"):
        request.session['title'] = "Settings"
        return render(request, 'html/user_pages/settings.html')
    else:
        return redirect("/login/user")   

def getProject(request):
    projects = Projects.objects.filter(uploader_id__exact=request.session['id']).values()
    return JsonResponse(list(projects), safe=False)

def getNotifications(request):
    notify = Notifications.objects.filter(notified_id__exact=request.session['id']).order_by("-id").values()[:25]
    setToRead = Notifications.objects.filter(notified_id=request.session['id'])
    for noti in setToRead:
        noti.status = "read"
        noti.save()
    return JsonResponse(list(notify), safe=False)

# update more info of the user
def updateInfo(request):
    try:
        info = Developers.objects.get(id=request.session['id'])
        info.skills = request.POST['skills']
        info.expertise = request.POST['expertise']
        info.aboutme = request.POST['aboutme']
        info.rate = request.POST['rate']
        info.country = request.POST['country']
        info.countryAbbr = request.POST['countryAbbr']+".png"
        info.save()
        return HttpResponse("Success")
    except:
        return HttpResponse("Failed")

def updateResume(request):
    currentResume = ''
    try:
        resume = request.FILES['resume']
        extension = os.path.splitext(resume.name)[1]
        rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
        fss = FileSystemStorage()
        filename = fss.save(rename, resume)
        devinfo = Developers.objects.get(id=request.session['id'])
        currentResume = devinfo.resume
        devinfo.resume = rename
        devinfo.save()
        # os.remove(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+str(currentResume))
        return HttpResponse("Success")

    except:
        return HttpResponse("Failed")

# update asked question
def updateQuestion(request):
	try:

		ques = Questions.objects.get(id=request.POST["id"])
		ques.question = request.POST['question']
		ques.language = request.POST['language']
		ques.category = request.POST['category']
		ques.save()
		return HttpResponse("Success")

	except: 

		return HttpResponse("Error")
# edit username
def editUsername(request):
    try:
        info = Developers.objects.get(id=request.session['id'])
        info.uname = request.POST['username']
        info.save()
        return HttpResponse("Username updated successfully")
    except:
        return HttpResponse("Error")

#update password 
def editPassword(request):
    try:
       
        hashed_pwd = make_password(request.POST['password'], salt=None, hasher='default')
        info = Developers.objects.get(id=request.session['id'])
        info.password = hashed_pwd
        info.save()
        return HttpResponse("Password updated successfully")

    except:
        return HttpResponse("Error")

def clearNotifs(request):
    try:
        notif = Notifications.objects.filter(notified_id=request.session['id'])
        if notif.count() == 0:
            return HttpResponse("Nothing to delete!")
        else:
            notif.delete()
            return HttpResponse("Notifications cleared successfully")

    except:

        return HttpResponse("An error has occurred! Please try again.")
def deleteNotif(request):
    try:
        notif = Notifications.objects.get(id=request.POST['id'])
        print(request.POST['id'])
        notif.delete()
        return HttpResponse("Notification deleted successfully")

    except:

        return HttpResponse("An error has occurred! Please try again.")