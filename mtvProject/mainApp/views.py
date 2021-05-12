from django.shortcuts import render
from .models import Blog
from .models import Team
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def home(request):
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams':teams})

