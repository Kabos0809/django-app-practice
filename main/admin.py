from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser, ThreadComments, ThreadModel, article_form, reportModel, article_comment

# Register your models here.
admin.site.register(reportModel)
admin.site.register(ThreadComments)

#募集

class articleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'comments', 'rnk_min', 'rnk_max', 'vc', 'num', 'per', 'hard')
    search_fields = ['id']

admin.site.register(article_form, articleAdmin)

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

    list_display = ('id', 'player_name', 'username', 'email', 'last_login')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {
            "fields": ('player_name', 'email', 'password', 'username', 'icon')}),
            ('Personal info', {'fields':('playfield', 'rank', 'discord_id', 'comments', 'character', 'last_login')}),
            ('Permissions',{'fields':('is_staff', 'is_superuser')})
    )
    add_fieldsetd = (
        (None,{
            'classes':('wide',),
            'fields':('id', 'icon', 'username', 'email', 'player_name', 'password1', 'playfield', 'rank', 'discord_id', 'comments', 'character', 'last_login')}
            ),
    )

    search_fields = ['id',]
    ordering = ('-last_login',)
    filter_horizonal = ()

admin.site.register(CustomUser, UserAdmin)