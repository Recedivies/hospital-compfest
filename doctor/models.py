from django.db import models

class Doctor(models.Model):
  name = models.CharField(max_length=20, unique=True)
  description = models.CharField(max_length=255)

  def __str__(self):
    return self.name