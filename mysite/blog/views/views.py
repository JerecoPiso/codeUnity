from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import User
from django.core.files.storage import FileSystemStorage
import os, datetime, json, zipfile, tempfile, mimetypes
from django.conf import settings
import io, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from zipfile import ZIP_DEFLATED
# from django_zipfile import TemplateZipFile
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

def download(request):
     # FIXME: Change this (get paths from DB etc)
    filenames = []
    files= getfilenames()
    for names in files:
    
      filenames.append(settings.MEDIA_ROOT +"\\haha\\"+names.strip("."))
    
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

def getfilenames():

    rootDir = settings.MEDIA_ROOT +"\\haha\\"

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
        print(pathlist)
    
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

def index(request):
     return render(request, 'html/index.html')

def login(request):
	return render(request, 'html/login.html')

def register(request):
     msg = ""
     if request.POST["name"] != "":
          if all(x.isalpha() or x.isspace() for x in request.POST["name"]):
               
               if request.POST["password"] != "" and request.POST["pass2"] != "":
                    if request.POST["password"] == request.POST["pass2"]:

                         if User.objects.filter(username__exact = request.POST["name"]):
                               msg = "Username already exist!"
                         else:
                               upload_file = request.FILES['image']
                               extension = os.path.splitext(upload_file.name)[1]
                               rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
                               fss = FileSystemStorage()
                               filename = fss.save(rename, upload_file)
                               user = User(username=request.POST["name"], password = request.POST["password"], file=rename)
                               user.save()
                    
                    else:
                         msg = "Password didn't matched!"
               else:
                    msg = "Password's are empty!"

          else:
               msg = "Name should be letters only!"

     else:
          msg = "Name cannot be empty!"

     return redirect(signup)
     
def signup(request):

     return render(request, "html/signup.html")