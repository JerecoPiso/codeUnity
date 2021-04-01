from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from pathlib import Path
import os
from blog.models import Projects, Questions
from django.conf import settings

rootDir = ""

def askQuestion(request):
    try:

        if request.method == "POST":
            ask = Questions(question=request.POST['question'], likes=0, asker_id=request.session['id'], code=request.POST['code'], language=request.POST['language'])
            ask.save()
            return HttpResponse('Added')

    except:
        
        return HttpResponse("Failed")

def index(request):
    request.session['title'] = "Home"
    if request.session.get("loggin"):
         project = Projects.objects.filter(uploader_id__exact=request.session['id']).count()
         question = Questions.objects.filter(asker_id__exact=request.session['id']).count()
         return render(request, 'html/user_pages/index.html', {'project_total': project, 'question_total': question})
    else:
         return redirect("/codeunity/login")

def projects(request):
        request.session['title'] = "Projects"
        count = Projects.objects.filter(uploader_id__exact=request.session['id']).count()
        proj = Projects.objects.filter(uploader_id__exact=request.session['id'])
        return render(request, 'html/user_pages/projects.html', {'myproject':proj, 'count': count})
# opening the file 
def readFile(request):

    path = request.POST['path']
    temp_path = path.replace(request.POST['fname'], "temporary")
    new_path = temp_path.replace("%", "\\")
    cd = os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'\\'+new_path.replace("temporary", request.POST['fname']))
    # cwd = cd
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
    request.session['title'] = "Questions"
    total_question = Questions.objects.filter(asker_id__exact=request.session['id']).count()
    myquestion = Questions.objects.all()
    return render(request, 'html/user_pages/questions.html', {'myquestions': myquestion, 'total_question': total_question})

def getQuestions(request):
    try:
        ques = Questions.objects.filter(asker_id__exact=request.session['id']).values()
        return JsonResponse(list(ques), safe=False)

    except:

        return HttpResponse("Failed")

def deleteQuestion(request):
    try:
        ques = Questions.objects.get(id=request.POST['id'])
        ques.delete()
        return HttpResponse("Deleted successfully")
    
    except:
        return HttpResponse("An error has occurred!")

# uploading project
def uploadProject(request):
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
            project = Projects(project_name=request.POST['project_name'], uploader_id=request.session['id'], downloads = 0, about=request.POST['about'], language=request.POST['language'], views = 0)
            project.save()       
            return HttpResponse("Uploaded successfully")
      
 
    return HttpResponse("An error has occurred!")
# user logout
def logout(request):
    try:
        del request.session['loggin']
        del request.session['id']
        del request.session['username']

    except:
        pass

    return redirect('/codeunity/login')

def settings(request):
    request.session['title'] = "Settings"
    return render(request, 'html/user_pages/settings.html')

def getProject(request):
    projects = Projects.objects.filter(uploader_id__exact=request.session['id']).values()
    return JsonResponse(list(projects), safe=False)