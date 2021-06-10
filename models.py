from django.db import models
from phone_field import PhoneField
import re
from django.core.validators import RegexValidator

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Employee(models.Model):
    fullname=models.CharField(max_length=30)
    emp_code=models.CharField(max_length=3)
    #mobile =PhoneField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$')
    mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    #mobile=models.CharField(max_length=10)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
