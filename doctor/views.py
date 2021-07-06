from django.shortcuts import render, redirect
from doctor.models import Doctor
from django.db.models import Q
from account.decorators import user_only

#decorator
@user_only
# index page
def index(request):
  return render(request, "doctor/index.html")

# Listing all Doctors
def list_doc(request):
  query = " "
  context = {}
  if (request.GET):
    query = request.GET['q']

  doctor = get_data_queryset(query)
  context['doctors'] = doctor
  return render(request, 'doctor/search_doctor.html', context)

# search query for doctors
def get_data_queryset(query=None):
  queryset = []
  queries = query.split(' ')
  for q in queries:
    doctors = Doctor.objects.filter(Q(name__icontains=q))

    for doctor in doctors:
      queryset.append(doctor)
  return list(set(queryset))