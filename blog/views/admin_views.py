from django.http import HttpResponse
from blog.models import User

def index(request):
    return HttpResponse("hahaha")