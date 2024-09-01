from django.db import models
from django.contrib.auth.models import User

class InfluencerInfo(models.Model):

    username=models.CharField(primary_key=True,max_length=30)
    first_name=models.CharField(max_length=30,default='none')
    last_name=models.CharField(max_length=40,default='none')
    email=models.EmailField(max_length=30)
    class Meta:
        db_table="InfluencerInfo"

class SponsorInfo(models.Model):
    
     username=models.CharField(primary_key=True,max_length=40)
     first_name=models.CharField(max_length=30,default='none')
     last_name=models.CharField(max_length=40,default='none')
     

     class Meta:
         db_table="SponsorInfo"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)



# Create your models here.
