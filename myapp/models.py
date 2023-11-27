from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length= 10) 
    password = models.CharField(max_length = 10)
    

class Admin(models.Model):
    username = models.CharField(max_length =50)
    password=models.CharField(max_length=10) 
    


class Citizens(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    dob = models.CharField(max_length =20)
    fdob = models.CharField(max_length = 20)
    pob = models.CharField(max_length = 20)
    fpob = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 20)
    cob = models.CharField(max_length = 20)
    nrc = models.CharField(max_length=20)
    postal = models.CharField(max_length = 20)
    province =models.CharField(max_length =20)
    village =models.CharField(max_length=20)
    chief = models.CharField(max_length=20)
    district = models.CharField(max_length =20)
