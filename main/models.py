from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class article_form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30, default=' ', null= False)
    comments = models.CharField(max_length=500, default=' ', null= False)
    rnk_min = models.CharField(max_length=100)
    rnk_max = models.CharField(max_length=100)
    num = models.CharField(max_length=100)
    per = models.CharField(max_length=100)
    hard = models.CharField(max_length=100)

#class user():
