from django.db import models
import uuid

class Doctor(models.Model):
  doc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=20)
  description = models.CharField(max_length=255)

  def __str__(self):
    return self.name