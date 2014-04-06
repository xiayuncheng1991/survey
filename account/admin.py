from django.contrib import admin

from account.models import UserStatistics
from stationary.admin import ChoiceInline


# Register your models here.
class UserStatisticsAdmin(admin.ModelAdmin):
    fields=['username']
    inlines=[ChoiceInline]
    list_display=('username','get_groupname','last_login','is_staff')
    list_filter=['username']
    
admin.site.register(UserStatistics, UserStatisticsAdmin)