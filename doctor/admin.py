from django.contrib import admin
from doctor.models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
  '''Admin View for Doctor'''

  list_display = ['name', 'description']