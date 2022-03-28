from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from sympy import false
from tables import Description
# Create your models here.




class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    compelte=models.BooleanField(default=false)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'title{self.title}'

class Meta:
            ordering=['complete']
