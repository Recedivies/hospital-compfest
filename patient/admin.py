from django.contrib import admin
from patient.models import Patient, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
  '''Admin View for Patient'''

  list_display = ('user',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
  '''Admin View for Appointment'''

  list_display = ('patient_id', 'doc_id')