from django.urls import path
from patient.views import (
  list_appointment,
  create_appointment,
  update_appointment,
  delete_appointment,
)

app_name = "patient"

urlpatterns = [
  path('appointment/', list_appointment, name='list'),
  path('appointment/create/<int:pk>', create_appointment, name='create_appointment'),
  path('update/<int:pk>/', update_appointment, name='update_appointment'),
  path('appointment/<int:pk>/', delete_appointment, name='delete_appointment'),
]