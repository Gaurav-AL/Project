from django.db import models

# Create your models here.

class UserDetails(models.Model):
    username = models.CharField(max_length=200)
    atm = models.CharField(max_length=12 , primary_key=True)
    atmpin = models.CharField(max_length=6 , default="")
    cvv = models.CharField(max_length=3)
