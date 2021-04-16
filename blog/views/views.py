from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import User, Developers, Projects, Questions, Language, Question_Category
from django.core.files.storage import FileSystemStorage
import os, datetime, json, zipfile, tempfile, mimetypes
from django.conf import settings
from django.contrib import messages
import io, smtplib, ssl
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
import random, time

rootDir = ""
message = "www"
resp = ""
# download folder in a zip format
def download(request, folder):
    
    filenames = []
    files= getfilenames(folder)
    for names in files:
    
      filenames.append(settings.MEDIA_ROOT +"\\"+folder+"\\"+names.strip("."))
    
    # zip_subdir = "zip"# name of the zip file to be downlaoded
    zip_filename = "%s.zip" % folder

    # Open BytesO to grab in-memory ZIP contents
    s = io.BytesIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")
    # print(filenames)
    for fpath in filenames:
    # Calculate path for file in zip
      fdir, fname = os.path.split(fpath)
      zip_path = os.path.join(folder, fpath[fpath.index("media", 0):len(fpath)])
      zf.write(fpath, zip_path.replace("media\\",""))
     
    
    zf.close() 
    download_total = Projects.objects.get(project_name__exact=folder)
    download_total.downloads = download_total.downloads + 1

    download_total.save()
    
    resp = HttpResponse(s.getvalue())
    resp["Content-Disposition"] = "attachment; filename=%s" % zip_filename

    return resp

def getfilenames(folder):

    rootDir = settings.MEDIA_ROOT +"\\"+folder+"\\"

    fileSet = set()
    for dir_, _, files in os.walk(rootDir):
      for fileName in files:
        relDir = os.path.relpath(dir_, rootDir)
        relFile = os.path.join(relDir, fileName)
        fileSet.add(relFile)
    return list(fileSet)

def index(request):
 
  # del request.session['session_ok']
  request.session['title'] = "Home"
  total_devs = Developers.objects.all().count()
  if (total_devs / 1000) >= 1:
    devs = str(1000*(total_devs/1000))+"K+"
  elif (total_devs/100) >= 1:
    devs = str(100*(total_devs/100))+"H+"
  else:
    devs = str(total_devs)

  total_projects = Projects.objects.all().count()
  if (total_projects / 1000) >= 1:
    proj = str(1000*(total_projects/1000))+"K+"
  elif (total_projects  / 100) >= 1:
    proj = str(100*(total_projects/100))+"H+"
  else:
    proj = str(total_projects)

  developers = Developers.objects.all()

  request.session.title = "Code Unity"
  apps = Projects.objects.filter(downloads__gt=0).order_by('-downloads')[:10]
  context = {}
  context['apps'] = apps
  context['total_devs'] = devs.replace(".0", "")
  context['total_projects'] = proj
  context['developers'] = developers
  return render(request, 'html/index.html', context)

def login(request):
  if request.session.get("loggin"):
    #  request.session.title = "Login"
     return redirect('/user')
  else:
     request.session['title'] = "Login"
     return render(request, 'html/login.html')

def verify(request):
 
  request.session.title = "Verify Account"
 
  if request.session.get("session_ok"):
    return render(request, 'html/verify.html')
  
  else:
    return redirect('/')

def verified(request):
  ret_msg = ""
  if request.session.get('code') != request.POST['code']:
    ret_msg = "Incorrect code!"
  else:
    # return HttpResponse("HAHAHA")
    # saved new user's info to the db if the verification code match
    if Developers.objects.filter(email__exact = request.session.get('reg_email')):
        msg = "Email already exist!"
    
    else:

        hashed_pwd = make_password(request.session.get('reg_password'), salt=None, hasher='default')
        user = Developers(email=request.session.get('reg_email'), password = hashed_pwd, photo = "dep.jpg", uname = request.session.get('reg_username'))
        user.save()
        # save session for the users panel
        request.session['id'] = user.id
        request.session['loggin'] = True
        request.session['username'] = user.uname
        # del all sessions stored
        try:
          del request.session['code']
          del request.session['reg_password']
          del request.session['reg_email']
          del request.session['reg_username']
          del request.session['session_ok']
        except:
          pass

        ret_msg = "Correct"

    return HttpResponse(ret_msg)


def projects(request):
  project = Projects.objects.all()
  language = Language.objects.all()
  apps = Projects.objects.filter(downloads__gt=0).order_by('-downloads')[:10]
  newest_apps = Projects.objects.order_by('-id')[:10]
  paginator = Paginator(project, 4)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  request.session['title'] = "Projects"
  return render(request, 'html/projects.html', {'new_apps': newest_apps, 'projects': page_obj, 'languages': language, 'page_obj': page_obj, 'apps': apps})

def questions(request):
  languages = Language.objects.all()
  question_cat = Question_Category.objects.all()  
  questions = Questions.objects.all()
  paginator = Paginator(questions, 5)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  total_questions = Questions.objects.all().count()
  request.session['title'] = "Questions"
  return render(request, 'html/questions.html', {'question_cat': question_cat, 'total_questions': total_questions, 'page_obj': page_obj, 'questions': page_obj, 'languages': languages})

def userLogin(request):
    request.session['title'] = "Login"
    msg = ""

    if request.POST['email'] != "":

        if request.POST['password'] != "":

            checker = Developers.objects.filter(email__exact = request.POST['email'])

            if checker:
                user = Developers.objects.get(email__exact = request.POST['email'])

                if check_password(request.POST['password'], user.password):
                    request.session['id'] = user.id
                    request.session['loggin'] = True
                    request.session['username'] = user.uname
                    request.session['photo'] = json.dumps(str(user.photo))
        

                    msg = "Success"


                else:
                    msg = "Incorrect password!"

            else:
                msg = "Email doesn't exist!"

        else:
            msg = "Password cannot be empty!"

    else:
        msg = "Email cannot be empty!"


    return HttpResponse(msg)

def register(request):
     msg = ""
     if request.POST["email"] != "":
          # if all(x.isalpha() or x.isspace() for x in request.POST["email"]):
               
               if request.POST["password"] != "" and request.POST["password2"] != "":
                    if request.POST["password"] == request.POST["password2"]:

                         if Developers.objects.filter(email__exact = request.POST["email"]):
                               msg = "Email already exist!"
                         else:
                               # upload_file = request.FILES['image']
                               # extension = os.path.splitext(upload_file.name)[1]
                               # rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
                               # fss = FileSystemStorage()
                               # filename = fss.save(rename, upload_file)
                               code = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
                               request.session['reg_email'] = request.POST['email']
                               request.session['reg_password']  = request.POST['password']
                               request.session['reg_photo'] = "haha"
                               request.session['reg_username'] = request.POST['username']
                               request.session['code'] = code
                               request.session['session_ok'] = True
                               request.session.set_expiry(300)
                               port = 465  # For SSL
                               smtp_server = "smtp.gmail.com"
                               sender_email = "jamesjerecopiso@gmail.com"  # sites email
                               receiver_email = request.POST['email']  # receivers email
                               password = "PHPprogrammer20"
                              
                               message = 'Subject: {}\n\n{}'.format("Verify Account", "Verification code : " + code)
                               context = ssl.create_default_context()
                               with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                                   server.login(sender_email, password)
                                   server.sendmail(sender_email, receiver_email, message)

                               msg = "Success"
                    
                    else:
                         msg = "Password didn't matched!"
               else:
                    msg = "Password's are empty!"

          # else:
          #      msg = "Name should be letters only!"

     else:
          msg = "Email cannot be empty!"

     return HttpResponse(msg)
     
def signup(request):
     request.session['title'] = "Signup"
     return render(request, "html/signup.html")

def developers(request):
     request.session['title'] = "Developers"
     return render(request, 'html/developers.html')

def viewProject(request, id):
      request.session['title'] = "viewProject"
      project = Projects.objects.get(id=id)
      project.views = project.views + 1
      project.save()
      return render(request, "html/view_project.html", {'project': project})

def viewQuestion(request, id):
      request.session['title'] = "viewQuestion"
      question = Questions.objects.get(id=id)
      return render(request, "html/view_question.html", {'question': question})