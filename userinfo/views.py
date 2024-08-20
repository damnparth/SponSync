from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from .models import InfluencerInfo, SponsorInfo
from django.http import HttpResponse,JsonResponse

@csrf_exempt
def register(request):

    if(request.method=='POST'):
        data=json.loads(request.body)
        user = User.objects.create_user(username=data['username'],first_name=data['first_name'],last_name=data['last_name'],password=data['password'])
        if(data['userType']=='influencer'):
             user = InfluencerInfo.objects.create(username=data['username'],first_name=data['first_name'],last_name=data['last_name'])
        elif(data['userType']=='sponsor'):
           user=SponsorInfo.objects.create(username=data['username'],first_name=data['first_name'],last_name=data['last_name'])

       
        return JsonResponse({
            'username':'username'
        })
    else:
        return JsonResponse({
            'message':'hello world'

        })

    



   # username=request.POST["username"]
    #first_name=request.POST["first_name"]
    #last_name=request.POST["last_name"]
    #password=request.POST["password"]
    #user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password)
# Create your views here.
