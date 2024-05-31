from django.db import models

# Create your models here.
class uploader(models.Model):
    Name=models.CharField(max_length=100)
    About=models.CharField(max_length=500)
    File=models.FileField(upload_to="file")

class files(models.Model):
    Date=models.CharField(max_length=30 ,null=True,blank=True)
    ACCNO=models.CharField(max_length=30,null=True,blank=True)
    CustState=models.CharField(max_length=100,null=True,blank=True)
    CustPin=models.IntegerField(null=True,blank=True)
    DPD=models.IntegerField(null=True,blank=True)