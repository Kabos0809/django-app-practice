from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser, article_form

# Register your models here.
admin.site.register(article_form)

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'user_id', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id')
    list_filter = ('email', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {
            "fields": ('email', 'password', 'username', 'user_id')}),
            ('Personal info', {'fields':('date', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id')}),
            ('Permissions',{'fields':('is_staff', 'is_superuser')})
    )
    add_fieldsetd = (
        (None,{
            'classes':('wide',),
            'fields':('username', 'email', 'user_id', 'password1', 'password2', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id')}
            ),
    )
    serach_fields = ('email',)
    ordering = ('email',)
    filter_horizonal = ()

admin.site.register(CustomUser)