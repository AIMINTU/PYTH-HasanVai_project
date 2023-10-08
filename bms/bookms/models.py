from django.db import models

# Create your models here.
from django.db import models
class Books(models.Model):
    bId=models.CharField(max_length=50,unique=True)
    bName=models.CharField(max_length=50)
    bAuthor=models.CharField(max_length=20)
    bPublish=models.CharField(max_length=15)
    class Meta:
        db_table="bookms"