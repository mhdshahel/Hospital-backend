from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=80)
    Email=models.EmailField(max_length=254)
    Username=models.CharField(max_length=60)
    Password=models.CharField(max_length=200)
    Section=models.CharField(max_length=40)
    Phone=models.CharField(max_length=50)
    

    #doctors

class Doctors (models.Model):
    NAME=models.CharField(max_length=30)
    DOB=models.DateField(null=True,blank=True)
    GENDER=models.CharField(max_length=40,null=True,blank=True)
    PHONE=models.CharField(max_length=50)
    AGE=models.IntegerField(null=True,blank=True)
    CATAGORY=models.CharField(max_length=40,null=True,blank=True)
    EMAIL=models.EmailField(max_length=30)
    ADDRESS=models.TextField(null=True,blank=True)
    DUTY_time=models.TimeField(null=True,blank=True)
    USERNAME=models.CharField(max_length=30)



   #staffs

class staffs (models.Model):
    NAME=models.CharField(max_length=30)
    ADDRESS=models.TextField()
    PHONE=models.CharField(max_length=50)
    GENDER=models.CharField(max_length=40)
    AGE=models.IntegerField()
    DOB=models.TimeField(null=True,blank=True)
    QUALIFITION=models.CharField(max_length=30)
    EMAIL=models.EmailField(max_length=40)
    USERNAME=models.CharField(max_length=20)
    Password=models.CharField(max_length=50)


   #patients

class patients (models.Model):
    NAME=models.CharField(max_length=70)
    AGE=models.IntegerField()
    ADDRESS=models.CharField(max_length=40)
    PHONE=models.CharField(max_length=50)
    DOB=models.TimeField(null=True,blank=True)
    GENDER=models.CharField(max_length=30)
    blood_group=models.CharField(max_length=40)

    #Booking


class booking (models.Model):
    NAME=models.CharField(max_length=30)
    AGE=models.IntegerField()
    PHONE=models.CharField(max_length=50)
    ADDRESS=models.CharField(max_length=50)
    TOKENNUMBER=models.IntegerField(default=1,null=True,blank=True)
    GENDER=models.CharField(max_length=60,null=True,blank=True)







