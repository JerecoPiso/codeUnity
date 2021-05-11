from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from blog.models import Language, Projects, Question_Category, Questions, User, Frameworks
from django.contrib.auth.hashers import make_password, check_password
from django.db import connection
# PAGES
def index(request):
	request.session['title'] = "Home"
	if request.session.get('admin_id'):
		return redirect('/dashboard/home')
	
	else:
		return render(request, 'html/dashboard/admin_login.html')

def home(request):
	request.session['title'] = "Main"
	if request.session.get('admin_id'):
		return render(request, 'html/dashboard/index.html')
	
	else:
		return redirect("/dashboard")
	

def logout(request):
	del request.session['admin_id']
	del request.session['admin_name']

	return redirect('/dashboard')

def projects(request):
	request.session['title'] = "Projects"
	if request.session.get('admin_id'):
		return render(request, 'html/dashboard/projects.html')
	
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

			if request.POST['pass'] == request.POST['pass2']:
				hashed_pwd = make_password(request.POST['pass'], salt=None, hasher='default')
				admin = User(username = request.POST['username'], password = hashed_pwd)
				admin.save()
				return HttpResponse("Sign up successfully")
		
			else:
				return HttpResponse("Password didn't matched!")

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
				frame = Frameworks(framework = request.POST['framework'], language_id = request.POST['language_id'])
				frame.save()
				return HttpResponse("Framework added successfuly")

		else:
			return HttpResponse("All fields must be filled up!")

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
		lang = Language.objects.all().values()
		return JsonResponse(list(lang), safe=False)
		
	except:
		return HttpResponse("Failed")	

def getFrameworks(request):
	with connection.cursor() as cursor:
			try:
				cursor.execute("SELECT blog_Frameworks.id, blog_Frameworks.framework, blog_Language.language FROM blog_Frameworks LEFT JOIN blog_Language ON blog_Frameworks.language_id = blog_Language.id")
				# framework = Frameworks.objects.all().values()
				return JsonResponse(list(dictfetchall(cursor)), safe=False)
			finally:
				cursor.close()
	
def dictfetchall(cursor):
      columns = [col[0] for col in cursor.description]
      return [
          dict(zip(columns, row))
          for row in cursor.fetchall()
      ]

# getting datas
def getQuestions(request):
	try:
		question = Questions.objects.all().values()
		return JsonResponse(list(question), safe=False)
		
	except:
		return HttpResponse("Failed")	

def getProjects(request):
	try:
		project = Projects.objects.all().values()
		return JsonResponse(list(project), safe=False)

	except:
		return HttpResponse("Failed")

def getCategory(request):
	try:
		cat = Question_Category.objects.all().order_by('-id').values()
		return JsonResponse(list(cat), safe=False)

	except:
		return HttpResponse("Failed")