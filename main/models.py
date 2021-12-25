from django.db import models
from datetime import datetime

class article_form(models.Model):
    title = models.CharField(max_length=30, default=' ', null= False)
    date = models.DateTimeField(default=datetime.now())
    comments = models.CharField(max_length=500, default=' ', null= False)
    rnk = models.CharField(max_length=100)
    num = models.CharField(max_length=100)
    per = models.CharField(max_length=100)

class tags(models.Model):
    tag_name = models.TextField(default=' ', null=True)
    
    def __str__(self):
        return self.tag_name

#class users(models.Model):

