from django.contrib import admin

from .models import Booking, Passenger, Flight,Comment

# Register your models here.
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Booking)
admin.site.register(Comment)
