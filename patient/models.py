from django.db import models
from doctor.models import Doctor
from django.contrib.auth.models import User

class Patient(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  age = models.PositiveIntegerField()
  doc_id = models.ManyToManyField(Doctor)

  def __str__(self):
    return self.user.username

class Appointment(models.Model):
  patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
  doc_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

  def __str__(self):
    return self.doc_id.name