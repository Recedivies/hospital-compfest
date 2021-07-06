from django.db import models

class Doctor(models.Model):
  doc_id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=20)
  description = models.CharField(max_length=255)

  def __str__(self):
    return self.name