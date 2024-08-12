
from django.db import models
from django.contrib.auth.models import User

class InfluencerInfo(models.Model):

    username=models.CharField(primary_key=True,max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    email=models.EmailField(max_length=30)
    class Meta:
        db_table="InfluencerInfo"

class SponsorInfo(models.Model):
     id = models.IntegerField(primary_key=True)
     username=models.CharField(unique=True,max_length=40)
     class Meta:
         db_table="SponsorInfo"

# Create your models here.
