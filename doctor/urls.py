from django.urls import path
from doctor.views import index, list_doc

app_name = 'doctor'

urlpatterns = [
  path('', index, name='index'),
  path('doctor/', list_doc, name='list_doc'),
]