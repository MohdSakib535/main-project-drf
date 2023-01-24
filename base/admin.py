from django.contrib import admin
from .models import Appointment,Billing,Doctor

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Billing)
