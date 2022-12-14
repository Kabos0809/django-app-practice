from email.policy import default
from django.conf import settings
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
import re

class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Emailは必須です。')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('スタッフ権限を持っている必要があります。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('スーパーユーザー権限を持っている必要があります。')
        return self._create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    username = models.CharField(_("username"), max_length=30, validators=[username_validator], blank=False, unique=True)
    player_name = models.CharField(_("player name"), max_length=50)
    steam_url = models.CharField(_("steam id"), max_length=200, blank=True, null=True)
    is_show_steam = models.BooleanField(_("show steam id"), default=False)
    origin_id = models.CharField(_("origin id"), max_length=200, blank=True, null=True)
    is_show_origin = models.BooleanField(_("show origin id"), default=False)
    psn_id = models.CharField(_("PSN id"), max_length=200, blank=True, null=True)
    is_show_psn = models.BooleanField(_("show psn id"), default=False)
    switch_id = models.CharField(_("switch id"), max_length=200, blank=True, null=True)
    is_show_switch = models.BooleanField(_("show switch id"), default=False)
    other_id = models.CharField(_('other id'), max_length=200, blank=True, null=True)
    is_show_other = models.BooleanField(_('show other id'), default=False)
    icon = models.ImageField(_("icon"), upload_to='user_icon/', blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_superuser = models.BooleanField(_("superuser status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    playfield = models.CharField(_("ply_f"), max_length=30, blank=True, null=True, default="設定なし")
    rank = models.CharField(_("rank"), max_length=30, blank=False)
    discord_id = models.CharField(_("discord"), max_length=100, blank=True)
    is_show_discord = models.BooleanField(_("show discord id"), default=False)
    comments = models.CharField(_("comments"), max_length=300, blank=True, default="自己紹介はありません")
    character = models.CharField(_("character"), max_length=2000, blank=True, null=True, default="設定なし")

    objects = MyUserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username", "player_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ['-last_login']


    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def split_playfield(self):
        a = self.playfield
        a = re.sub(r'[\]\[\']', '', a)
        a = a.split(',')
        return a

    def split_character(self):
        a = self.character
        a = re.sub(r'[\]\[\']', '', a)
        a = a.split(',')
        return a

    def __str__(self):
        return self.username

class apex_recruit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30, default=' ', null= False)
    comments = models.CharField(max_length=500, default=' ', null= False)
    rnk_min = models.CharField(max_length=100)
    rnk_max = models.CharField(max_length=100)
    num = models.CharField(max_length=100)
    per = models.CharField(max_length=100)
    hard = models.CharField(max_length=100)
    vc = models.CharField(max_length=100, default='なし')

    def __str__(self):
        return str(self.id)

class article_comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    article = models.ForeignKey(apex_recruit, editable=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=140, default=' ')

    def __str__(self):
        return str(self.id)

class reportModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE)
    article_id = models.ForeignKey(apex_recruit, editable=False, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(default=timezone.now)
    matters = models.CharField(max_length=100, blank=True)
    not_mischief = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)


#掲示板カテゴリー

#class ThreadCategory(models.Model):
#   id = models.UUIDField(primary_key=True, editable=False, default=uuid)
#   name = models.CharField(max_length=50)
#   def __str__(self):
#       return str(self.name)

class ThreadModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title
    
class ThreadComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE)
    news = models.ForeignKey(ThreadModel, editable=False, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now())
    comment = models.CharField(max_length=140)

    def __str__(self):
        return self.comment

#DM機能実装するかは未定

#class DirectMessage(models.Model):
#    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE)
#    for_user = models.ForeignKey(CustomUser, editable=False, on_delete=models.CASCADE)
#    time = models.TimeField(default=timezone.now())
#    mes =models.CharField(max_length=2000)
#    def __str__(self):
#        return self.mes
