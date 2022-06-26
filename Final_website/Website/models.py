from types import NoneType
from urllib.parse import MAX_CACHE_SIZE
from django.db import models

# Create your models here.
class userDetail(models.Model):
    username = models.CharField(max_length=200,primary_key=True,default="Already Exists")
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    dob = models.CharField(max_length=40)
    descr = models.TextField(default="Not Added")
    gender = models.CharField(max_length=200)

class contactsInfo(models.Model):
    email = models.EmailField(max_length = 200,primary_key=True)
    phone_no = models.CharField(max_length = 10)
    query = models.TextField(max_length=300)

class billInfo(models.Model):
    name = models.CharField(max_length=100)
    Items = models.CharField(max_length=100)
    total = models.IntegerField()

