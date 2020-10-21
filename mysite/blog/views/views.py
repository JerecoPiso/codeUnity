from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import User, Developers
from django.core.files.storage import FileSystemStorage
import os, datetime, json, zipfile, tempfile, mimetypes
from django.conf import settings
from django.contrib import messages
import io, smtplib, ssl
from django.contrib.auth.models import User
from django.core.paginator import Paginator
rootDir = ""
message = "www"
resp = ""

def sendEmail(request):
 
      port = 465  # For SSL
      smtp_server = "smtp.gmail.com"
      sender_email = "jamesjerecopiso@gmail.com"  # Enter your address
      receiver_email = "jerecojamespiso@gmail.com"  # Enter receiver address
      password = "prograpper20"
      # message = """\
      # codeUnity



      # This message is sent from Python."""

      message = 'Subject: {}\n\n{}'.format("Verify Account", "Verify")
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
          server.login(sender_email, password)
          server.sendmail(sender_email, receiver_email, message)
   
      return HttpResponse("sended")

def folderUpload(request):
     return render(request, "html/upload.html")

def download(request, folder):
    project_name="public"
     # FIXME: Change this (get paths from DB etc)
    filenames = []
    files= getfilenames(folder)
    for names in files:
    
      filenames.append(settings.MEDIA_ROOT +"\\"+folder+"\\"+names.strip("."))
    
    zip_subdir = "zip"# name of the zip file to be downlaoded
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = io.BytesIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")
    # print(filenames)
    for fpath in filenames:
    # Calculate path for file in zip
      fdir, fname = os.path.split(fpath)
      zip_path = os.path.join(zip_subdir, fpath[fpath.index("media", 0):len(fpath)])
  
      zf.write(fpath, zip_path)
     
    
    zf.close() 
  
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



def get(request):
    if request.method == 'POST':
        
        dir=request.FILES
        dirlist=dir.getlist('files')

        pathlist=request.POST.getlist('paths')
        # print(pathlist[0].find('/'))
        if not dirlist:
            return HttpResponse('files not found')
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

def index(request):
  # messages.error(request, 'Document deleted.')
  contact_list = Developers.objects.all()
  paginator = Paginator(contact_list, 5) # Show 25 contacts per page.
  # print(contact_list)
  page_number = request.GET.get('page')
  
  page_obj = paginator.get_page(page_number)
  request.session.title = "Code Unity"
  return render(request, 'html/index.html',{'page_obj': page_obj, 'contact': contact_list})

def login(request):
  if request.session.get("loggin"):
     request.session.title = "Login"
     return redirect('/codeunity/user')
  else:
     request.session.title = "Login"
     return render(request, 'html/login.html')

def verify(request):
  request.session.title = "Verify Account"
  return render(request, 'html/verify.html')

def projects(request):
  request.session.title = "Projects"
  return render(request, 'html/projects.html')

def questions(request):
  request.session.title = "Questions"
  return render(request, 'html/forum.html')

def userLogin(request):
    msg = ""

    if request.POST['email'] != "":

        if request.POST['password'] != "":

            checker = Developers.objects.filter(email__exact = request.POST['email'])

            if checker:
                user = Developers.objects.get(email__exact = request.POST['email'])

                if user.password == request.POST['password']:

                    request.session['loggin'] = True

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
                               user = Developers(email=request.POST["email"], password = request.POST["password"], photo='haha')
                               user.save()
                               msg = "Registered successfully"
                    
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
     request.session.title = "Signup"
     return render(request, "html/signup.html")

def jobs(request):
     request.session.title = "Jobs"
     return render(request, "html/jobs.html")