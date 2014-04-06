from django.contrib import admin

from stationary.models import Choice, StationaryType


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
 
class StationaryAdmin(admin.ModelAdmin):
    fieldsets = [
              (None, {'fields': ['name']}),
              ('Image Show',{'fields':['image']}),
              ('Max Quantity',{'fields':['quantity_max']}),
              ('details information', {'fields': ['details'], 'classes': ['collapse']}),
         ]
    inlines = [ChoiceInline]
    list_display = ('name', 'details', 'sum',)
    list_filter = ['name']
      
admin.site.register(StationaryType, StationaryAdmin)
