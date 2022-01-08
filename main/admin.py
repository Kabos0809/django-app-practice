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

    list_display = ('user_id', 'username', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id', 'comments', 'character')
    list_filter = ('email', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {
            "fields": ('user_id', 'email', 'password', 'username', 'id')}),
            ('Personal info', {'fields':('date', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id', 'comments', 'character')}),
            ('Permissions',{'fields':('is_staff', 'is_superuser')})
    )
    add_fieldsetd = (
        (None,{
            'classes':('wide',),
            'fields':('id', 'username', 'email', 'user_id', 'password1', 'password2', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id', 'comments', 'character')}
            ),
    )
    serach_fields = ('email','username')
    ordering = ('email',)
    filter_horizonal = ()

admin.site.register(CustomUser)