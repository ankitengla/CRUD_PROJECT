from django.db import models

# Create your models here.
class SignupData(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.CharField(max_length=10)
    Password=models.CharField(max_length=50)
    confPassword=models.CharField(max_length=50)

class QueryData(models.Model):
    Query=models.CharField(max_length=200)
    QueryEmail=models.CharField(max_length=200)
    
    
