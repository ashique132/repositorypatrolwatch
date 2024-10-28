from django.db import models

# Create your models here.

class RegisterTable(models.Model):
    Username = models.CharField(max_length=30, null=True, blank=True)
    Password = models.CharField(max_length=30,null=True, blank=True)
    Name=models.CharField(max_length=30,null=True,blank=True)
    Dob=models.DateField()
    
class CriminalTable(models.Model):
    Criminalname= models.CharField(max_length=30, null=True, blank=True)
    Image= models.FileField(null=True, blank=True)
    Type=models.CharField(max_length=30,null=True,blank=True)
    Details=models.CharField(max_length=30,null=True,blank=True)
    Address=models.CharField(max_length=30,null=True,blank=True)

