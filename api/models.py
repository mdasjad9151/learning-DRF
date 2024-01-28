from django.db import models

# Create your models here.
class Todo(models.Model):
    title =  models.CharField(max_length=100, default="")
    body = models.CharField(max_length=500, default= "")
    createDate = models.DateField(null=True)
    updateDate  = models.DateField(null=True)