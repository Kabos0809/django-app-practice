from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser, ExchangeInfoModel, Thread, article_form, reportModel

# Register your models here.
admin.site.register(reportModel)
admin.site.register(article_form)
admin.site.register(ExchangeInfoModel)
admin.site.register(Thread)

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('player_name', 'username', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id', 'comments', 'character', 'icon')
    list_filter = ('email', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {
            "fields": ('player_name', 'email', 'password', 'username', 'id', 'icon')}),
            ('Personal info', {'fields':('date', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id', 'comments', 'character')}),
            ('Permissions',{'fields':('is_staff', 'is_superuser')})
    )
    add_fieldsetd = (
        (None,{
            'classes':('wide',),
            'fields':('id', 'icon', 'username', 'email', 'player_name', 'password1', 'playfield', 'rank', 'twitter_id', 'Youtube_url', 'discord_id', 'comments', 'character')}
            ),
    )
    serach_fields = ('email','username')
    ordering = ('email',)
    filter_horizonal = ()

admin.site.register(CustomUser)