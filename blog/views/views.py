from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from blog.models import Frameworks, User, Developers, Projects, Questions, Language, Question_Category, Comments, Replies
from django.core.files.storage import FileSystemStorage
import os, datetime, json, zipfile, tempfile, mimetypes
from django.conf import settings
from django.contrib import messages
import io, smtplib, ssl
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
import random, time
from django.db.models import Count
from django.db import connection

# rootDir = ""
# message = "www"
# resp = ""
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
  if request.session.get('redirectTo'):
    del request.session['redirectTo']
  
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

# def login(request):
#   if request.session.get("loggin"):
  
#      return redirect('/user')
#   else:
#      request.session['title'] = "Login"
#      return render(request, 'html/login.html')

def verify(request):
 
  request.session.title = "Verify Account"
 
  if request.session.get("session_ok"):
    return render(request, 'html/verify.html')
  
  else:
    return redirect('/')

def verified(request):
  ret_msg = ""
  goto = ""
  if request.session.get('code') != request.POST['code']:
    ret_msg = "Incorrect code!"
  else:
    # return HttpResponse("HAHAHA")
    # saved new user's info to the db if the verification code match
    if Developers.objects.filter(email__exact = request.session.get('reg_email')):
        msg = "Email already exist!"
    
    else:

        hashed_pwd = make_password(request.session.get('reg_password'), salt=None, hasher='default')
        user = Developers(email=request.session.get('reg_email'), password = hashed_pwd, photo = "dp.jpg", uname = request.session.get('reg_username'))
        user.save()
        # save session for the users panel
       
      
        # del all sessions stored
        try:
          del request.session['code']
          del request.session['reg_password']
          del request.session['reg_email']
          del request.session['reg_username']
          del request.session['session_ok']
          del request.session['reg_photo']
        except:
          pass

        ret_msg = True
  if ret_msg == True:

            if request.session.get('redirectTo'):
              if request.session['redirectTo'] == "user":
                request.session['id'] = user.id
                request.session['loggin'] = True
                request.session['username'] = user.uname
                goto = "/user"
              else:
                request.session['viewQuestion'] = True
                request.session['questionViewerId'] = user.id
                route = request.session['redirectTo']
                goto = "/viewQuestion/"+route[13:len(route)+1]
                
            else:
                request.session['id'] = user.id
                request.session['loggin'] = True
                request.session['username'] = user.uname
                goto = "/user"
              

  else:
        
      goto = "/verify"
      messages.error(request, ret_msg)

  return redirect(goto)

# logout for the viewQuestionPage
def logout(request,questionId):

    del request.session['viewQuestion']
    del request.session['questionViewerId']
    del request.session['photo']
    del request.session['username']

    return redirect("/login/"+questionId)


def projects(request):

  project = Projects.objects.all()
  # language = Projects.objects.values(
  #   'language'
  #   ).annotate(language_count=Count('language')).filter(language_count__gt=0)

  language = Language.objects.all()
  frameworks = Frameworks.objects.all()
  apps = Projects.objects.filter(downloads__gt=0).order_by('-downloads')[:10]
  newest_apps = Projects.objects.order_by('-id')[:10]
  paginator = Paginator(project, 5)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  request.session['title'] = "Projects"
  return render(request, 'html/projects.html', {'frameworks': frameworks,'total_project': project.count(),'new_apps': newest_apps, 'projects': page_obj, 'languages': language, 'page_obj': page_obj, 'apps': apps})

def searchProject(request,toSearch):
 
  frameworks = Frameworks.objects.all()
  project = Projects.objects.filter(project_name__icontains=toSearch)

  # language = Projects.objects.values(
  #   'language'
  #   ).annotate(language_count=Count('language')).filter(language_count__gt=0)
  language = Language.objects.all()
  apps = Projects.objects.filter(downloads__gt=0).order_by('-downloads')[:10]
  newest_apps = Projects.objects.order_by('-id')[:10]
  paginator = Paginator(project, 3)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  request.session['title'] = "Projects"
  return render(request, 'html/search_project.html', {'frameworks': frameworks,'search': toSearch,'new_apps': newest_apps, 'projects': page_obj, 'languages': language, 'page_obj': page_obj, 'apps': apps})

def filterProjects(request, toSearch):
  frameworks = Frameworks.objects.all()
  project = Projects.objects.filter(language__contains=toSearch)
  # language = Projects.objects.values(
  #   'language'
  #   ).annotate(language_count=Count('language')).filter(language_count__gt=0)
  language = Language.objects.all()
  apps = Projects.objects.filter(downloads__gt=0).order_by('-downloads')[:10]
  newest_apps = Projects.objects.order_by('-id')[:10]
  paginator = Paginator(project, 4)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  request.session['title'] = "Projects"
  return render(request, 'html/filterProjects.html', {'frameworks': frameworks,'languages': language,'toSearch': toSearch, 'new_apps': newest_apps, 'projects': page_obj,'page_obj': page_obj, 'apps': apps})

def questions(request):
  # languages = Language.objects.all()
  # frameworks = Frameworks.objects.all() 
  category = Questions.objects.values(
  'category'
  ).annotate(category_count=Count('category')).filter(category_count__gt=0)

  questions = Questions.objects.all().order_by('-id')
  paginator = Paginator(questions, 15)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  total_questions = Questions.objects.all().count()
  request.session['title'] = "Questions"
  return render(request, 'html/questions.html', {'question_cat': category,'total_questions': total_questions, 'page_obj': page_obj, 'questions': page_obj})


def searchQuestion(request, toSearch):
  category = Questions.objects.values(
  'category'
  ).annotate(category_count=Count('category')).filter(category_count__gt=0)

  questions = Questions.objects.filter(question__contains=toSearch)
  paginator = Paginator(questions, 15)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  total_questions = Questions.objects.all().count()
  request.session['title'] = "Questions"
  return render(request, 'html/questions.html', {'question_cat': category,'toSearch': toSearch,'total_questions': total_questions, 'page_obj': page_obj, 'questions': page_obj})

def getQuestion(request, toGetQuestion, value):
  category = Questions.objects.values(
  'category'
  ).annotate(category_count=Count('category')).filter(category_count__gt=0)

  if toGetQuestion == "tags":
    questions = Questions.objects.filter(tags__contains=value).order_by('-id')
  elif toGetQuestion == "filter":
    questions = Questions.objects.filter().order_by('-id')[:10]
  else:
    questions = Questions.objects.filter(category__contains=value).order_by('-id')

  paginator = Paginator(questions, 15)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  total_questions = Questions.objects.all().count()
  request.session['title'] = "Questions"
  return render(request, 'html/questions.html', {'question_cat': category,'total_questions': total_questions, 'page_obj': page_obj, 'questions': page_obj})

def getDevelopers(request, toGetDevelopers, value):
  if toGetDevelopers == "skills":
    devs = Developers.objects.filter(skills__contains=value).order_by("-id")
  else:
    devs = Developers.objects.filter(expertise__contains=value).order_by("-id")
  
  request.session['title'] = "Developers"
  # devs = Developers.objects.all()
  frameworks = Frameworks.objects.all()
  total_devs = Developers.objects.all().count()
  language = Language.objects.all()
  paginator = Paginator(devs, 10)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'html/developers.html', {'page_obj': page_obj, 'devs': page_obj,'frameworks': frameworks, 'total': total_devs, 'languages': language})


def userLogin(request, redirectTo):
    request.session['title'] = "Login"
    msg = ""
    redirectedTo = ""

    if request.POST['email'] != "":

        if request.POST['password'] != "":

            checker = Developers.objects.filter(email__exact = request.POST['email'])

            if checker:
                user = Developers.objects.get(email__exact = request.POST['email'])

                if check_password(request.POST['password'], user.password):

                    if redirectTo == "user":

                        request.session['id'] = user.id
                        request.session['loggin'] = True
                        request.session['username'] = user.uname
                        request.session['photo'] = json.dumps(str(user.photo))
                        # print(redirectTo[0:(len(redirectTo)+1)])
                    
                        redirectedTo = "/user"

                    else:
                        request.session['viewQuestion'] = True
                        request.session['questionViewerId'] = user.id
                        request.session['photo'] = json.dumps(str(user.photo))
                        request.session['username'] = user.uname
                    
                        # request.session.set_expiry(60)
                        redirectedTo = "/viewQuestion/"+(redirectTo[13:len(redirectTo)+1])
                    
                    msg = True

                else:
                    msg = "Incorrect password!"
                  
            else:
                msg = "Email doesn't exist!"
              
        else:
            msg = "Password cannot be empty!"
           
    else:
        msg = "Email cannot be empty!"
       
    
    
        
    if msg != True:
      if redirectTo == "user":
                      
        redirectedTo = "/login/user"

      else:

        redirectedTo = "/login/viewQuestion/"+(redirectTo[13:len(redirectTo)+1])
      messages.error(request, msg)

    return redirect(redirectedTo)


def register(request):
     msg = ""
     if request.POST["email"] != "":
          # if all(x.isalpha() or x.isspace() for x in request.POST["email"]):
               
               if request.POST["password"] != "" and request.POST["password2"] != "":
                    if request.POST["password"] == request.POST["password2"]:

                         if Developers.objects.filter(email__exact = request.POST["email"]):
                               msg = "Email already exist!"
                         else:
                            
                               code = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
                               request.session['reg_email'] = request.POST['email']
                               request.session['reg_password']  = request.POST['password']
                               request.session['reg_photo'] = "dp.jpg"
                               request.session['reg_username'] = request.POST['username']
                               request.session['code'] = code
                               request.session['session_ok'] = True
                               request.session.set_expiry(300)
                               port = 465  
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
     
     if msg == "Success":
          route = "/verify"
          
     else:

       if request.session.get('redirectTo'):
          route = "/signup/"+request.session['redirectTo']
       else:
          route = "/"
    
     if msg != "Success":
        messages.error(request, msg)

     return redirect(route)

def signup(request, redirectTo):
     request.session['title'] = "Signup"
     request.session['redirectTo'] = redirectTo
     print(request.session['redirectTo'])
     return render(request, "html/signup.html")

def login(request, redirectTo):
    #  messages.warning(request, 'Your account expires in three days.')
     request.session['title'] = "Signup"
  
     return render(request, "html/login.html", {'redirect': redirectTo})

def developers(request):
     request.session['title'] = "Developers"
     devs = Developers.objects.all()
     frameworks = Frameworks.objects.all()
     total_devs = Developers.objects.all().count()
     language = Language.objects.all()
     paginator = Paginator(devs, 1)
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     return render(request, 'html/developers.html', {'page_obj': page_obj, 'devs': page_obj,'frameworks': frameworks,'total': total_devs, 'languages': language})

def viewProject(request, id):
      request.session['title'] = "viewProject"
      project = Projects.objects.get(id=id)
      project.views = project.views + 1
      project.save()
      return render(request, "html/view_project.html", {'project': project})

def viewQuestion(request, id):
      request.session['title'] = "viewQuestion"
   
      question = Questions.objects.get(id=id)

      return render(request, "html/view_question.html", {'question': question, 'post_id': id})

      # else:
      #     question = Questions.objects.get(id=id)
      #     return render(request, "html/view_question.html", {'question': question, 'post_id': id})

def addComment(request):
   
      if request.method == "POST":
        try:
            comment = Comments(commentor = request.session['questionViewerId'], post_id = request.POST['post_id'], comment = request.POST['comment'], date = request.POST['date'], answer = request.POST['answer'])
            comment.save()
            com = Questions.objects.get(id = request.POST['post_id'])
            com.comments = com.comments + 1
            com.save()
            return HttpResponse("Commented succesfully.")
        
        except:

            return HttpResponse("An error has occurred!")
      
      else:

        return HttpResponse("Request method should be POST!")

# saved reply
def reply(request):
     reply = Replies(commentor = request.session['questionViewerId'], post_id = request.POST['post_id'], comment_id = request.POST['comment_id'], reply = request.POST['reply'], date = request.POST['date'])
     reply.save()
     ques = Questions.objects.get(id = request.POST['post_id'])
     ques.comments = ques.comments + 1
     ques.save()
     return HttpResponse("Replied successfully")
   

# get comments
def getCom(request):
     with connection.cursor() as cursor:
       try:
          cursor.execute("SELECT blog_Comments.id, blog_Comments.commentor, blog_Comments.post_id, blog_Comments.comment, blog_Comments.date, blog_Comments.answer, blog_Developers.photo,  blog_Developers.uname  FROM blog_Comments LEFT JOIN blog_Developers ON blog_Comments.commentor = blog_Developers.id WHERE blog_Comments.post_id = "+request.POST['question_id'])
          return JsonResponse(list(dictfetchall(cursor)), safe=False)
       finally:
          cursor.close()

# get replies
def getReply(request):
    with connection.cursor() as cursor:
        try:
           
          cursor.execute("SELECT blog_Replies.id, blog_Replies.post_id, blog_Replies.commentor, blog_Replies.comment_id, blog_Replies.reply, blog_Replies.date, blog_Developers.uname, blog_Developers.photo FROM blog_Replies LEFT JOIN blog_Developers ON blog_Replies.commentor = blog_Developers.id WHERE blog_Replies.post_id = "+request.POST['question_id'])
          return JsonResponse(list(dictfetchall(cursor)), safe=False)
        finally:
          cursor.close()

 

def deleteReply(request):
    reply = Replies.objects.get(id=request.POST['id'])
    reply.delete()
    ques = Questions.objects.get(id = request.POST['post_id'])
    ques.comments = ques.comments - 1
    ques.save()
    return HttpResponse("Reply deleted successfully")
# set the raw query result to  dict
def dictfetchall(cursor):
      columns = [col[0] for col in cursor.description]
      return [
          dict(zip(columns, row))
          for row in cursor.fetchall()
      ]

# delete comment
def deleteComment(request):
    total_reply_of_comment = Replies.objects.filter(comment_id=request.POST['id']).count()
   
  
    comment = Comments.objects.get(id=request.POST['id'])
    comment.delete()
    reply = Replies.objects.filter(comment_id=request.POST['id'])
    reply.delete()
    ques = Questions.objects.get(id = request.POST['post_id'])
    ques.comments = ques.comments - (total_reply_of_comment + 1)
    ques.save()
  
    return HttpResponse("Comment deleted successfully")