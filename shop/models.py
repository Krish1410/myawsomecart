from ast import mod
from distutils.command.upload import upload
import email
from email.policy import default
from msilib import PID_CHARCOUNT
from django.db import models

# Create your models here.
class Product(models.Model):
    p_id=models.AutoField
    p_img=models.ImageField(upload_to="shop/images",default="")
    p_category=models.CharField(max_length=50,default="")
    p_subcategory=models.CharField(max_length=50,default="")
    p_price=models.IntegerField(default=0)
    p_name=models.CharField(max_length=102)
    p_des=models.TextField()
    p_date=models.DateField()

    def __str__(self):
        return self.p_name

class Contect(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=10)
    desc=models.CharField(max_length=1000)

    def __str__(self):
        return self.name