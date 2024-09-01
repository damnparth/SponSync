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
        if(data['last_name']=='influencer'):
             user = InfluencerInfo.objects.create(username=data['username'],first_name=data['first_name'],last_name=data['last_name'])
        elif(data['last_name']=='sponsor'):
           user=SponsorInfo.objects.create(username=data['username'],first_name=data['first_name'],last_name=data['last_name'])
      
       
        return JsonResponse({
            'username':'username'
        })
    else:
        return JsonResponse({
            'message':'hello world'

        })
    

@csrf_exempt
def login_user(request):
    if request.method=='POST':
        login_data=json.loads(request.body)
        user = authenticate(request,username=login_data['username'],password=login_data['passText'])
        
        if user is not None:
            login(request,user)
            if user.last_name == "sponsor":
                return JsonResponse({"userType": "sponsor","username":user.username})
            elif user.last_name == "influencer":
                return JsonResponse({"userType": "influencer","username":user.username})
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)
    
    return JsonResponse({"message": "Method not allowed"}, status=405)


@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({'message' : "Hello world"})

            
            
                
            
        




        
    
        


    



   
# Create your views here.
