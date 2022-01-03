from django.core import validators
from django.conf import settings
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    username = models.CharField(_("username"), max_length=30, validators=[username_validator], blank=False, unique=True)
    user_id = models.CharField(_("user_id"), max_length=30, unique=True)
    email = models.EmailField(_("email_address"), unique=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_superuser = models.BooleanField(_("superuser status"), default=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    playfield = models.CharField(_("play field"), max_length=30, blank=True)
    rank = models.CharField(_("rank"), max_length=30, blank=False)
    twitter_id = models.CharField(_("twitter id"), max_length=100, blank=True)
    Youtube_url = models.CharField(_("YouTube CHANNEL"), max_length=100, blank=True)
    discord_id = models.CharField(_("discord"), max_length=100, blank=True)

    objects = UserManager()
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["user_id"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.username

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError('ユーザーidは必須です。')
        if not email:
            raise ValueError('Emailは必須です。')
        email = self.normalize_email(email)
        username = self.model.normalize_uername(username)
        user = self.model(username=username, email=email, user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('isstaff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('スタッフ権限を持っている必要があります。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('スーパーユーザー権限を持っている必要があります。')
        return self._create_user(username, email, password, **extra_fields)

class article_form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    #author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30, default=' ', null= False)
    comments = models.CharField(max_length=500, default=' ', null= False)
    rnk_min = models.CharField(max_length=100)
    rnk_max = models.CharField(max_length=100)
    num = models.CharField(max_length=100)
    per = models.CharField(max_length=100)
    hard = models.CharField(max_length=100)

