from django.contrib import admin

from .models import *
# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)


# it'll tell django's admin app that i would like to use the admin
#  to be able to manipulate flights and airports
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)