from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from .models import InfluencerInfo, SponsorInfo
from django.http import HttpResponse

@csrf_exempt
def register(request):
    return HttpResponse('hello world')
   # username=request.POST["username"]
    #first_name=request.POST["first_name"]
    #last_name=request.POST["last_name"]
    #password=request.POST["password"]
    #user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password)
# Create your views here.
