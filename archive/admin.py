from django.contrib import admin

from archive.models import StationaryArchive


# Register your models here.
# class StationaryArchiveAdmin(admin.ModelAdmin):
#     fields=['username']
#     inlines=[ChoiceInline]
#     list_display=('username','get_groupname','last_login','is_staff')
#     list_filter=['username']
admin.site.register(StationaryArchive,)