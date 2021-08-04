from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from blog.models import Notifications, Yearly_Visitors, Frameworks, User, Developers, Projects, Questions, Language, Question_Category, Comments, Replies
from django.core.files.storage import FileSystemStorage
import os, datetime, json, zipfile, tempfile, mimetypes
from django.conf import settings
from django.contrib import messages
import io, smtplib, ssl
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
import random, time, datetime
from django.db.models import Count
from django.db import connection
from django.db.models import Q
from django.core.mail import send_mail
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
    d_total = download_total.downloads + 1
    download_total.downloads = d_total
    download_total.save()
    hour = ""
    am_pm = ""
    if int(datetime.datetime.now().strftime("%H")) > 12:
       hour = int(datetime.datetime.now().strftime("%H")) - 12
       am_pm = " pm"
    else:
       hour = datetime.datetime.now().strftime("%H")
       am_pm = " pm"
    datenow =  datetime.datetime.now().strftime("%h") + "-" + datetime.datetime.now().strftime("%d") + "-"+ datetime.datetime.now().strftime("%Y") + " " + str(hour) + ":" + datetime.datetime.now().strftime("%M")+ ":" + datetime.datetime.now().strftime("%S") + "" + am_pm
    notification_content = "A user downloaded your <b>" + folder + "</b> project. It has now <b>" + str(d_total) + "</b> download/s."
    notify = Notifications(notification=notification_content, notified_id=download_total.uploader_id, date=datenow, status="unread")
    notify.save()
   #  months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
   #  d = int(datetime.datetime.now().strftime("%m"))
      #  print(months[int(datetime.datetime.now().strftime("%m"))])  
   
    
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
  year_now = datetime.datetime.now().strftime("%Y")
  # check if the current year exists in the data base 
  # if not add the current year
  check_if_yearnow_exists = Yearly_Visitors.objects.filter(year=year_now).exists()
  if check_if_yearnow_exists:
      yearly = Yearly_Visitors.objects.get(year=year_now)
      if yearly:
          yearly.total_visitors = yearly.total_visitors + 1
          yearly.save()
  else:
      # save the current year to database
      add_year_now = Yearly_Visitors(year=year_now, total_visitors=1)
      add_year_now.save()
  
  return render(request, 'html/index.html')

def verify(request):
 
  request.session.title = "Verify Account"
  # check if the session_ok is set
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
        ret_msg = "Email already exist!"
    
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
                request.session['loggin'] = True
                request.session['id'] = user.id
                route = request.session['redirectTo']
               
                goto = "/question/"+route[13:len(route)+1]
                
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
    
    del request.session['loggin']
    del request.session['id']
    del request.session['photo']
    del request.session['username']

    return redirect("/login/"+questionId)


def projects(request):

  project = Projects.objects.all()
  # lang = Projects.objects.values(
  #   'language'
  #   ).annotate(language_count=Count('language')).filter(language_count__gt=0)

  language = Language.objects.all()
  frameworks = Frameworks.objects.all()
  apps = Projects.objects.filter(downloads__gt=0).order_by('-downloads')[:10]
  newest_apps = Projects.objects.order_by('-id')[:10]
  if project.count() < 10 and project.count() > 1:
     paginator = Paginator(project, project.count())
  elif project.count() > 10:
     paginator = Paginator(project, 10)
  else:
     paginator = Paginator(project, 1)
  
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
  if project.count() < 10 and project.count() > 1:
     paginator = Paginator(project, project.count())
  elif project.count() > 10:
     paginator = Paginator(project, 10)
  else:
     paginator = Paginator(project, 1)
  
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

  if project.count() < 10 and project.count() > 1:
     paginator = Paginator(project, project.count())
  elif project.count() > 10:
     paginator = Paginator(project, 10)
  else:
     paginator = Paginator(project, 1)
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
  if questions.count() < 10 and questions.count() > 1:
     paginator = Paginator(questions, questions.count())
  elif questions.count() > 10:
     paginator = Paginator(questions, 10)
  else:
     paginator = Paginator(questions, 1)
  
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
  if questions.count() < 10 and questions.count() > 1:
     paginator = Paginator(questions, questions.count())
  elif questions.count() > 10:
     paginator = Paginator(questions, 10)
  else:
     paginator = Paginator(questions, 1)
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
      if value == "latest":
          questions = Questions.objects.filter().order_by('-id')[:10]
      elif value == "answered":
          questions = Questions.objects.filter(status='Answered').order_by('-id')
      else:
          questions = Questions.objects.filter(status='').order_by('-id')
  else:
    questions = Questions.objects.filter(category__contains=value).order_by('-id')


  if questions.count() < 10 and questions.count() > 1:
     paginator = Paginator(questions, questions.count())
  elif questions.count() > 10:
     paginator = Paginator(questions, 10)
  else:
     paginator = Paginator(questions, 1)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  total_questions = Questions.objects.all().count()
  request.session['title'] = "Questions"
  return render(request, 'html/questions.html', {'question_cat': category,'total_questions': total_questions, 'page_obj': page_obj, 'questions': page_obj})

def getDevelopers(request, toGetDevelopers, value):
  dev_cat = Developers.objects.values('expertise').annotate(expertise_count=Count('expertise')).filter(expertise_count__gt=0)
  if toGetDevelopers == "skills":
    devs = Developers.objects.filter(skills__contains=value).order_by("-id")
  else:
    devs = Developers.objects.filter(expertise__contains=value).order_by("-id")
  
  if devs.count() < 10 and devs.count() > 1:
     paginator = Paginator(devs, devs.count())
  elif devs.count() > 10:
     paginator = Paginator(devs, 25)
  else:
     paginator = Paginator(devs, 1)
  request.session['title'] = "Developers"
  # devs = Developers.objects.all()
  frameworks = Frameworks.objects.all()
  total_devs = Developers.objects.all().count()
  language = Language.objects.all()
  paginator = Paginator(devs, 10)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'html/developers.html', {"categor": dev_cat,'search': value,'page_obj': page_obj, 'devs': page_obj,'frameworks': frameworks, 'total': total_devs, 'languages': language})

def searchDevs(request, search):
  
  devs = Developers.objects.filter(Q(skills__contains=search) | Q(expertise__contains=search)).order_by("-id")
  dev_cat = Developers.objects.values('expertise').annotate(expertise_count=Count('expertise')).filter(expertise_count__gt=0)
  if devs.count() < 10 and devs.count() > 1:
     paginator = Paginator(devs, devs.count())
  elif devs.count() > 10:
     paginator = Paginator(devs, 25)
  else:
     paginator = Paginator(devs, 1)
  request.session['title'] = "Developers"
  
  frameworks = Frameworks.objects.all()
  total_devs = Developers.objects.all().count()
  language = Language.objects.all()
  paginator = Paginator(devs, 10)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'html/developers.html', {"categor": dev_cat,'page_obj': page_obj, 'devs': page_obj,'frameworks': frameworks, 'total': total_devs, 'languages': language, 'search': search})

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

                    request.session['id'] = user.id
                    request.session['loggin'] = True
                    request.session['username'] = user.uname
                    request.session['photo'] = json.dumps(str(user.photo))
                    request.session['toLogout'] = redirectTo 
                    if redirectTo == "user":

                     
                        # print(redirectTo[0:(len(redirectTo)+1)])
                    
                        redirectedTo = "/user"
                    elif redirectTo == "ask":
                        redirectedTo = "/user/questions"
                    elif redirectTo == "upload-project":
                        redirectedTo = "/user/projects"
                    else:
                        # request.session['viewQuestion'] = True
                        # request.session['questionViewerId'] = user.id
                        # request.session['photo'] = json.dumps(str(user.photo))
                        # request.session['username'] = user.uname
                        # request.session['id'] = user.id
                        # request.session['loggin'] = True
                        # request.session['username'] = user.uname
                        # request.session['photo'] = json.dumps(str(user.photo))

                        question = Questions.objects.get(id=(redirectTo[13:len(redirectTo)+1]))
                        question.views = question.views + 1
                        
                        question.save()
                        # request.session.set_expiry(60)
                        redirectedTo = "/question/"+(redirectTo[13:len(redirectTo)+1])
                       
                    
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
      elif redirectTo == "ask":
        redirectedTo = "/login/ask"
      elif redirectTo == "upload-project":
        redirectedTo = "/login/upload-project"
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
                              #  port = 465  
                              #  smtp_server = "smtp.gmail.com"
                              #  sender_email = "jamesjerecopiso@gmail.com" 
                              #  receiver_email = request.POST['email'] 
                              #  password = "PHPprogrammer20"
                              
                              #  message = 'Subject: {}\n\n{}'.format("Verify Account", "Verification code : " + code)
                              #  context = ssl.create_default_context()
                              #  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                              #      server.login(sender_email, password)
                              #      server.sendmail(sender_email, receiver_email, message)
                               receiver = request.POST['email'] 
                               send_mail(
                                 'Verify Account',
                                 'Verification code : ' + code,
                                 'CodeUnity',
                                 [receiver],
                                 fail_silently=True,
                               )
                              
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
        print(msg)

     return redirect(route)

def signup(request, redirectTo):
     request.session['title'] = "Signup"
     request.session['redirectTo'] = redirectTo
     print(request.session['redirectTo'])
     return render(request, "html/signup.html")
     
def login(request, redirectTo):
    #  messages.warning(request, 'Your account expires in three days.')
     request.session['title'] = "Login"
     if request.session.get("loggin"):
          if redirectTo == "user":
             return redirect("/user/")
          elif redirectTo == "ask":
             return redirect("/user/questions")
          elif redirectTo == "upload-project":
             return redirect("/user/projects")
          else:
             return redirect("/questions/"+(redirectTo[13:len(redirectTo)+1]))
     else:
          return render(request, "html/login.html", {'redirect': redirectTo})

def developers(request):
     dev_cat = Developers.objects.values('expertise').annotate(expertise_count=Count('expertise')).filter(expertise_count__gt=0)
     request.session['title'] = "Developers"
     devs = Developers.objects.all()
     frameworks = Frameworks.objects.all()
     total_devs = Developers.objects.all().count()
     language = Language.objects.all()
     if devs.count() < 10 and devs.count() > 1:
        paginator = Paginator(devs, devs.count())
     elif devs.count() > 10:
        paginator = Paginator(devs, 25)
     else:
        paginator = Paginator(devs, 1)
    
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     return render(request, 'html/developers.html', {'categor': dev_cat,'page_obj': page_obj, 'devs': page_obj,'frameworks': frameworks,'total': total_devs, 'languages': language})

def viewProject(request, id):
      request.session['title'] = "viewProject"
      project = Projects.objects.get(id=id)
      project.views = project.views + 1
      project.save()
      return render(request, "html/view_project.html", {'project': project})

def viewQuestion(request, id):
      request.session['title'] = "viewQuestion"
      # if request.session.get("loggin"):
      question = Questions.objects.get(id=id)
      asker_name = Developers.objects.get(id=question.asker_id)
  
      return render(request, "html/view_question.html", {'question': question, 'post_id': id, 'poster_name': asker_name.uname})

      # else:
      #     question = Questions.objects.get(id=id)
      #     return render(request, "html/view_question.html", {'question': question, 'post_id': id})

def addComment(request):
   
      if request.method == "POST":
        try:
            comment = Comments(commentor = request.session['id'], post_id = request.POST['post_id'], comment = request.POST['comment'], date = request.POST['date'], answer = request.POST['answer'])
            comment.save()
            com = Questions.objects.get(id = request.POST['post_id'])
           
            com.comments = com.comments + 1
            com.save()
            hour = ""
            am_pm = ""
            if int(datetime.datetime.now().strftime("%H")) > 12:
               hour = int(datetime.datetime.now().strftime("%H")) - 12
               am_pm = " pm"
            else:
               hour = datetime.datetime.now().strftime("%H")
               am_pm = " pm"
            datenow =  datetime.datetime.now().strftime("%h") + "-" + datetime.datetime.now().strftime("%d") + "-"+ datetime.datetime.now().strftime("%Y") + " " + str(hour) + ":" + datetime.datetime.now().strftime("%M")+ ":" + datetime.datetime.now().strftime("%S") + "" + am_pm
            notification_content = "<b>" + request.session['username'] + "</b> commented on your question " + "<b>" + com.question + "</b>."
            notify = Notifications(notification=notification_content, notified_id=com.asker_id, date=datenow, status="unread")
            notify.save()
            return HttpResponse("Commented succesfully.")
        
        except:

            return HttpResponse("An error has occurred!")
      
      else:

        return HttpResponse("Request method should be POST!")

# saved reply
def reply(request):
    try:  
        reply = Replies(commentor = request.session['id'], post_id = request.POST['post_id'], comment_id = request.POST['comment_id'], reply = request.POST['reply'], date = request.POST['date'])
        reply.save()
        ques = Questions.objects.get(id = request.POST['post_id'])
        ques.comments = ques.comments + 1
        ques.save()
        return HttpResponse("Replied successfully")
    except:
        return HttpResponse("An error has occurred!")
     
# get comments
def getCom(request):
     with connection.cursor() as cursor:
       try:
          cursor.execute("SELECT blog_Comments.id, blog_Comments.commentor, blog_Comments.post_id, blog_Comments.comment, blog_Comments.date, blog_Comments.answer, blog_Comments.status, blog_Developers.photo,  blog_Developers.uname  FROM blog_Comments LEFT JOIN blog_Developers ON blog_Comments.commentor = blog_Developers.id WHERE blog_Comments.post_id = "+request.POST['question_id'])
          return JsonResponse(list(dictfetchall(cursor)), safe=False)
       finally:
          cursor.close()

# get replies
def getReply(request):
    with connection.cursor() as cursor:
        try:
           
          cursor.execute("SELECT blog_Replies.id, blog_Replies.post_id, blog_Replies.commentor, blog_Replies.comment_id, blog_Replies.reply, blog_Replies.date, blog_Developers.uname, blog_Developers.photo FROM blog_Replies LEFT JOIN blog_Developers ON blog_Replies.commentor = blog_Developers.id  WHERE blog_Replies.post_id = "+request.POST['question_id']+" ORDER BY blog_Replies.id DESC")
          return JsonResponse(list(dictfetchall(cursor)), safe=False)
        finally:
          cursor.close()


def setAnswer(request):
    # print(request.POST['category'])
    
    question = Questions.objects.get(id=request.POST['question_id'])
    question.status = "Answered"
    question.save()
    if request.POST['category'] == 'comment':
       comment = Comments.objects.get(id=request.POST['id'])
       comment.status = "Answer"
       comment.save()
       return HttpResponse("Done")
    else:
    
       return HttpResponse("Error")

def setUnanswered(request):
    # print(request.POST['category'])
   
    if request.POST['category'] == 'comment':
       comment = Comments.objects.get(id=request.POST['id'])
       comment.status = ""
       comment.save()
       check_if_answered = Comments.objects.filter(Q(status="Answer") & Q(post_id=request.POST['question_id']))
    
       if check_if_answered.count() == 0:
          question = Questions.objects.get(id=request.POST['question_id'])
          question.status = ""
          question.save()

       return HttpResponse("Done")
    else:
  
       return HttpResponse("Error")    

def deleteReply(request):
    try:
        reply = Replies.objects.get(id=request.POST['id'])
        reply.delete()
        ques = Questions.objects.get(id = request.POST['post_id'])
        ques.comments = ques.comments - 1
        ques.save()
        return HttpResponse("Reply deleted successfully")
    except:
        return HttpResponse("Something went wrong!")
# set the raw query result to  dict
def dictfetchall(cursor):
      columns = [col[0] for col in cursor.description]
      return [
          dict(zip(columns, row))
          for row in cursor.fetchall()
      ]

# delete comment
def deleteComment(request):
    try:

        total_reply_of_comment = Replies.objects.filter(comment_id=request.POST['id']).count()
        comment = Comments.objects.get(id=request.POST['id'])
        comment.delete()
        reply = Replies.objects.filter(comment_id=request.POST['id'])
        reply.delete()
        ques = Questions.objects.get(id = request.POST['post_id'])
        ques.comments = ques.comments - (total_reply_of_comment + 1)
        ques.save()
        return HttpResponse("Comment deleted successfully")
    except:
        return HttpResponse("Something went wrong!")

        