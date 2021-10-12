from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect
from django.conf import settings
from blog.models import Users_Device, Language, Projects, Question_Category, Questions, User, Frameworks, Developers, Yearly_Visitors
from django.contrib.auth.hashers import make_password, check_password
from django.db import connection
from django.db.models import Count, Q
from django.core.files.storage import FileSystemStorage
import datetime, os
from pathlib import Path
# PAGES
def index(request):
	request.session['title'] = "Home"
	if request.session.get('admin_id'):
		return redirect('/dashboard/home')
	
	else:
		return render(request, 'html/dashboard/admin_login.html')

def home(request):
	request.session['title'] = "Main"
	totals = {}
	totals['total_apps'] = Projects.objects.all().count()
	totals['total_devs'] = Developers.objects.all().count()
	totals['total_questions'] = Questions.objects.all().count() 
	totals['total_languages'] = Language.objects.all().count() + Frameworks.objects.all().count()

	if request.session.get('admin_id'):
		return render(request, 'html/dashboard/index.html', totals)
	
	else:
		return redirect("/dashboard")
	

def logout(request):
	try:
		del request.session['admin_id']
		del request.session['admin_name']
	except:
		pass
	return redirect('/dashboard')

def projects(request):
	request.session['title'] = "Projects"
	projectsLanguage = Projects.objects.values(
    'language'
    ).annotate(language_count=Count('language')).filter(language_count__gt=0)
	# latestProjects = Projects.objects.filter(downloads__gt=0)[:10]
	latestProjects = Projects.objects.filter(Q(downloads__gt=0) & Q(date__contains=datetime.datetime.now().strftime("%Y"))).order_by("-id")
	if request.session.get('admin_id'):
		return render(request, 'html/dashboard/projects.html', {'projectsLanguage': projectsLanguage, 'latestProjects':latestProjects })
	
	else:
		return redirect("/dashboard")

def developers(request):
	request.session['title'] = "Developers"
	if request.session.get('admin_id'):
		return render(request, 'html/dashboard/developers.html')
	
	else:
		return redirect("/dashboard")

def questions(request):
	request.session['title'] = "Questions"
	if request.session.get('admin_id'):
		return render(request, 'html/dashboard/questions.html')
	
	else:
		return redirect("/dashboard")

def languages(request):
	request.session['title'] = "Language"
	if request.session.get('admin_id'):
		return render(request, 'html/dashboard/languages.html')
	
	else:
		return redirect("/dashboard")

def signup(request):
	# request.session['title'] = "Signup"
	if request.method == "POST":
	
		if request.POST['username'] != "" and request.POST['pass'] != "" and request.POST['pass2'] != "":
			if all(x.isalpha() or x.isspace() for x in request.POST['username']):

				if len(request.POST['pass']) >= 8:
					if request.POST['pass'] == request.POST['pass2']:
						hashed_pwd = make_password(request.POST['pass'], salt=None, hasher='default')
						admin = User(username = request.POST['username'], password = hashed_pwd, file='dp.jpg')
						admin.save()
						return HttpResponse("Success")
				
					else:
						return HttpResponse("Password didn't matched!")
				else:
					return HttpResponse("Password must contain at least 8 characters")
			else:

				return HttpResponse("Username must be contain letters and white spaces only!")
		else:
			return HttpResponse("All fields must be filled up!")	
		
	else:
		return HttpResponse("Method request should be POST!")


def login(request):
	if request.method == "POST":
		if request.POST['username'] != "" and request.POST['password'] != "":
		
				check_username = User.objects.filter(username__exact=request.POST['username'])
				if check_username:
					user = User.objects.get(username__exact = request.POST['username'])

					if check_password(request.POST['password'], user.password):
						request.session['admin_id'] = user.id
						request.session['admin_name'] = user.username

						return HttpResponse("Login")
					
					else:
						return HttpResponse("Incorrect Password")
				
				else:
					return HttpResponse("Username not exist!")
		else:
			return HttpResponse("All fields must be  filled  up!")
	

	else:
		return HttpResponse("Method request should be POST!")

# creating datas
def addLanguage(request):
	try:
		if request.POST['language'] != "" and request.POST['category'] != "":
			if Language.objects.filter(language=request.POST['language']):

				return HttpResponse("Language already exist!")

			else:
				lang = Language(language = request.POST['language'], category = request.POST['category'])
				lang.save()
				return HttpResponse("Language added successfuly")

		else:
			return HttpResponse("All fields must be filled up!")

	except:
		return HttpResponse("An error has occured!")

def addFramework(request):
	try:
		if request.POST['framework'] != "" and request.POST['language_id'] != "":
			if Frameworks.objects.filter(framework=request.POST['framework']):

				return HttpResponse("Framework already exist!")

			else:
				frame = Frameworks(framework = request.POST['framework'], language_id = request.POST['language_id'], category = request.POST['category'])
				frame.save()
				return HttpResponse("Framework added successfuly")

		else:
			return HttpResponse("All fields must be filled up!")

	except:
		return HttpResponse("An error has occured!")

def setDevice(request):
	try:
		if request.POST['deviceName'] != "":
	
			if Users_Device.objects.filter(device_name=request.POST['deviceName']).count() > 0:
				device = Users_Device.objects.get(device_name__exact=request.POST['deviceName'])
				device.total_users = device.total_users + 1
				device.save()
				return HttpResponse("Updated")
			else:	
				dev = Users_Device(device_name=request.POST['deviceName'], total_users=1)
				dev.save()
			
				return HttpResponse("Device added successfuly")
		
		else:
			return HttpResponse("Device name must not be empty!")
	except:
		return HttpResponse("An error has occured!")
# creating datas
def addCategory(request):
	try:
		if request.POST['category'] != "":
			if Question_Category.objects.filter(category__exact=request.POST['category']):

				return HttpResponse("Question Category already exist!")

			else:
				cat = Question_Category(category = request.POST['category'])
				cat.save()
				return HttpResponse("Question Category added successfuly")

		else:
			return HttpResponse("All fields must be filled up!")

	except:
		return HttpResponse("An error has occured!")
# deleting datas
def deleteLanguage(request):
	try:
		lang = Language.objects.get(id=request.POST['id'])
		lang.delete()
		return HttpResponse("Deleted successfuly")

	except:

		return HttpResponse("An error has occured!")

# deleting datas
def deleteFramework(request):
	try:
		frame = Frameworks.objects.get(id=request.POST['id'])
		frame.delete()
		return HttpResponse("Deleted successfuly")

	except:

		return HttpResponse("An error has occured!")
# deleting datas
def deleteQuestionCategory(request):
	try:
		cat = Question_Category.objects.get(id=request.POST['id'])
		cat.delete()
		return HttpResponse("Deleted successfuly")

	except:

		return HttpResponse("An error has occured!")


def updateLanguage(request):
	try:
		lang = Language.objects.get(id=request.POST['id'])
		lang.language = request.POST['language']
		lang.category = request.POST['category']
		lang.save()
		return HttpResponse("Updated successfuly")
	except:

		return HttpResponse("An error has occured!")

def updateFramework(request):
	try:
		fw = Frameworks.objects.get(id=request.POST['id'])
		fw.language_id = request.POST['language_id']
		fw.framework = request.POST['framework']
		fw.category = request.POST['category']
		fw.save()
		return HttpResponse("Updated successfuly")
	except:

		return HttpResponse("An error has occured!")

def editQuestionCategory(request):
	try:
		if request.POST['category'] != "":
			cat = Question_Category.objects.get(id=request.POST['id'])
			cat.category = request.POST['category']
			print(request.POST['category'])
			cat.save()

			return HttpResponse("Updated successfully")
		
		else:

			return HttpResponse("Category must not be empty!")
	except:

		return HttpResponse("An error has occured!")		
# getting datas
def getLanguages(request):
	try:
		lang = Language.objects.all().order_by("-id").values()
		return JsonResponse(list(lang), safe=False)
		
	except:
		return HttpResponse("Failed")	

def getFrameworks(request):
	with connection.cursor() as cursor:
			try:
				cursor.execute("SELECT blog_Frameworks.id, blog_Frameworks.language_id, blog_Frameworks.framework, blog_Frameworks.category, blog_Language.language FROM blog_Frameworks LEFT JOIN blog_Language ON blog_Frameworks.language_id = blog_Language.id ORDER BY blog_Frameworks.id DESC")
				# framework = Frameworks.objects.all().values()
				return JsonResponse(list(dictfetchall(cursor)), safe=False)
			finally:
				cursor.close()
	

# getting datas
def getQuestions(request):
	try:
		question = Questions.objects.all().values()
		return JsonResponse(list(question), safe=False)
		
	except:
		return HttpResponse("Failed")	

def getDevs(request):
	try:
		devs = Developers.objects.all().values()
		return JsonResponse(list(devs), safe=False)

	except:
		return HttpResponse("Failed")	

def getDevices(request):
	try:
		devices = Users_Device.objects.all().values()
		return JsonResponse(list(devices), safe=False)
	except:
		return HttpResponse("Failed")	

def getProjects(request):
	with connection.cursor() as cursor:
			try:
				cursor.execute("SELECT blog_Projects.id, blog_Projects.project_name, blog_Projects.downloads, blog_Projects.language, blog_Developers.uname FROM blog_Projects LEFT JOIN blog_Developers ON blog_Projects.uploader_id = blog_Developers.id")
				# framework = Frameworks.objects.all().values()
				return JsonResponse(list(dictfetchall(cursor)), safe=False)
			finally:
				cursor.close()
	# try:
	# 	project = Projects.objects.all().values()
	# 	return JsonResponse(list(project), safe=False)

	# except:
	# 	return HttpResponse("Failed")

def getCategory(request):
	try:
		cat = Question_Category.objects.all().order_by('-id').values()
		return JsonResponse(list(cat), safe=False)

	except:
		return HttpResponse("Failed")


def getMostDownloadedApp(request):
	# Q(downloads__gt=0) & Q(status="unread")
	app = Projects.objects.filter(Q(downloads__gt=0) & Q(photo__contains=datetime.datetime.now().strftime("%Y"))).order_by('-downloads').values()[:10]
	return JsonResponse(list(app), safe=False)

def getMostViewedQuestions(request):
	ques = Questions.objects.filter(Q(views__gt=0) & Q(date__contains=datetime.datetime.now().strftime("%Y"))).order_by('-views').values()[:10]
	return JsonResponse(list(ques), safe=False)

def getYearlyVisitors(request):
	year_now = datetime.datetime.now().strftime("%Y")
	yearly = Yearly_Visitors.objects.filter(year=year_now).exists()
	if yearly:
		# add_year_now = Yearly_Visitors(year=2020, total_visitors=0)
		# add_year_now.save()
		ret_years = Yearly_Visitors.objects.all().order_by('year').values()
		# return HttpResponse("Exists")
	else:
		add_year_now = Yearly_Visitors(year=year_now, total_visitors=0)
		add_year_now.save()
		ret_years = Yearly_Visitors.objects.all().values()


	return JsonResponse(list(ret_years), safe=False)

def dictfetchall(cursor):
      columns = [col[0] for col in cursor.description]
      return [
          dict(zip(columns, row))
          for row in cursor.fetchall()
      ]

def userprofile(request):
	request.session['title'] = 'User Profile'
	request.session.set_expiry(0)
	return render(request, 'html/dashboard/user_profile.html')

def getAdminInfo(request):
	try:
		admin = User.objects.filter(id=request.session.get('admin_id')).values()
		return JsonResponse(list(admin), safe=False)
	except:
		return HttpResponse("Error")


# changing profile of the current user
def changeDp(request):
    if request.method == "POST":
        admin = User.objects.get(id__exact=request.session.get('admin_id')) 
        if os.path.exists(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+str(admin.file)):

            upload_file = request.FILES["photo"]
            extension = os.path.splitext(upload_file.name)[1]
            rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
            fss = FileSystemStorage()
            fss.save(rename, upload_file)
            # upload_file_path = fss.path(filename)
 
            if str(admin.file) != "dp.jpg":
                os.remove(os.path.join(Path(__file__).resolve().parent.parent.parent, 'media'+'/')+str(admin.file))
            admin.file = rename
            admin.save()

        else:

            return HttpResponse("Path did'nt exists!")

        return HttpResponse("Profile changed successfully")
    else:
        return HttpResponse("Error error has occurred")

def changepass(request):
	resposnseMsg = ''
	if request.method == "POST":
		if len(request.POST['password']) > 7:
			if request.POST['password'] == request.POST['pass2']:
				hashed_pwd = make_password(request.POST['password'], salt=None, hasher='default')
				admin = User.objects.get(id=request.session.get('admin_id'))
				admin.password = hashed_pwd
				admin.save()
				resposnseMsg = "Password changed successfully"
			else:
				resposnseMsg = "Password didn't matched!"
		else:
			resposnseMsg = "Password must be at least 8 characters!"

	else:
		resposnseMsg = "Something went wrong!"
	
	return HttpResponse(resposnseMsg)

def editname(request):
	responseMsg = ''
	if request.method == 'POST':
		if request.POST['username'] != "":
			if all(x.isspace() or x.isalpha() for x in request.POST['username']):
				
				if User.objects.filter(id=request.session.get('admin_id')).count() > 0:
					user = User.objects.get(id=request.session.get('admin_id'))
					user.username = request.POST['username']
					user.save()
					responseMsg = "Success"
				else:
					responseMsg = "User id not found!"

			else:
				responseMsg = "Username must be alphabet only!"
		else:
			responseMsg = "Username must not be empty!"
		
	else:
		responseMsg = "Something went wrong!"
	
	return HttpResponse(responseMsg)

