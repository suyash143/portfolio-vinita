from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    section=Section.objects.all()
    achievements=Achievement.objects.all()
    videos=Video.objects.all()
    return render(request,'index.html',{'achievements':achievements,'section':section,'videos':videos})