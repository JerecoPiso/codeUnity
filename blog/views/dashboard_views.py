from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from blog.models import Language, Projects, Question_Category, Questions

# PAGES
def index(request):
	request.session['title'] = "Home"
	return render(request, 'html/dashboard/index.html')

def projects(request):
	request.session['title'] = "Projects"
	return render(request, 'html/dashboard/projects.html')

def questions(request):
	request.session['title'] = "Questions"
	return render(request, 'html/dashboard/questions.html')

def languages(request):
	request.session['title'] = "Language"
	return render(request, 'html/dashboard/languages.html')

# creating datas
def addLanguage(request):
	try:
		if request.POST['language'] != "" and request.POST['category'] != "":
			if Language.objects.filter(language__exact=request.POST['language']):

				return HttpResponse("Language already exist!")

			else:
				lang = Language(language = request.POST['language'], category = request.POST['category'])
				lang.save()
				return HttpResponse("Language added successfuly")

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