from django.contrib import admin
from django.db import models

from .models import Doctor, Address, Place, Day_Of, Schedule

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1

class PlaceAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    list_display = ('name',)

    def has_delete_permission(self, request, obj=None):
        return False

class Day_OfAdmin(admin.ModelAdmin):
    fields = ['doctor', 'day_of']
    list_display = ('doctor', 'day_of')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'admission_date', 'active')

    def has_delete_permission(self, request, obj=None):
        return False

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'place', 'date')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Day_Of, Day_OfAdmin)
admin.site.register(Schedule, ScheduleAdmin)
