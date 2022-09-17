from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser, ThreadComments, ThreadModel, apex_recruit, reportModel, article_comment

# Register your models here.
admin.site.register(reportModel)
admin.site.register(ThreadComments)

#募集

class articleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'comments', 'rnk_min', 'rnk_max', 'vc', 'num', 'per', 'hard')
    search_fields = ['id']

admin.site.register(apex_recruit, articleAdmin)

#募集コメント

class commentAdimn(admin.ModelAdmin):
    list_display = ('id', 'article', 'user', 'date', 'comment')
    list_filter = ('date',)
    search_fields = ['id']

admin.site.register(article_comment, commentAdimn)

#掲示板スレッド

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'date')
    list_filter = ('date',)
    search_fields = ['id']

admin.site.register(ThreadModel, ThreadAdmin)

#ユーザー

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'username', 'player_name', 'email', 'last_login')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {
            "fields": ('email', 'password', 'username', 'player_name', 'icon')}),
            ('Personal info', {'fields':('playfield', 'rank', 'steam_url', 'origin_id', 'psn_id', 'switch_id', 'other_id','discord_id', 'comments', 'character', 'last_login')}),
            ('Permissions',{'fields':('is_staff', 'is_superuser', 'is_show_steam', 'is_show_origin', 'is_show_psn', 'is_show_switch', 'is_show_discord','is_show_other')})
    )
    add_fieldsetd = (
        (None,{
            'classes':('wide',),
            'fields':('id', 'icon', 'username', 'player_name', 'email', 'password1', 'playfield', 'rank', 'steam_url', 'origin_id', 'psn_id', 'switch_id', 'discord_id', 'comments', 'character', 'last_login')}
            ),
    )

    search_fields = ['id',]
    ordering = ('-last_login',)
    filter_horizonal = ()

admin.site.register(CustomUser, UserAdmin)