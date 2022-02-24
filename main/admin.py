from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser, NewsComments, NewsModel, article_form, reportModel

# Register your models here.
admin.site.register(reportModel)
admin.site.register(article_form)
admin.site.register(NewsModel)
admin.site.register(NewsComments)

class article_form(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('id')
        
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('player_name', 'username', 'playfield', 'rank', 'discord_id', 'comments', 'character', 'icon')
    list_filter = ('email', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {
            "fields": ('player_name', 'email', 'password', 'username', 'id', 'icon')}),
            ('Personal info', {'fields':('date', 'playfield', 'rank', 'discord_id', 'comments', 'character')}),
            ('Permissions',{'fields':('is_staff', 'is_superuser')})
    )
    add_fieldsetd = (
        (None,{
            'classes':('wide',),
            'fields':('id', 'icon', 'username', 'email', 'player_name', 'password1', 'playfield', 'rank', 'discord_id', 'comments', 'character')}
            ),
    )
    serach_fields = ('email','username')
    ordering = ('email',)
    filter_horizonal = ()

admin.site.register(CustomUser)