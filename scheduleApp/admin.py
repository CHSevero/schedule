from django.contrib import admin
from django.db import models

from .models import Doctor, Address, Place, Day_Of, Schedule

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1

class PlaceAdmin(admin.ModelAdmin):
    
    inlines = [AddressInline]
    list_display = ('name',)


admin.site.register(Doctor)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Day_Of)
admin.site.register(Schedule)
