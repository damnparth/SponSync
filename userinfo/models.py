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

# Create your models here.
