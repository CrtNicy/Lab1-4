from django.contrib import admin

from .models import Owner
from .models import Car
from .models import DrivingLicense
from .models import CustomUser
from .models import Ownership
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(DrivingLicense)
admin.site.register(Ownership)
admin.site.register(CustomUser)