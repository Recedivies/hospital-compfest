from django.shortcuts import render, redirect
from patient.models import Patient, Appointment
from doctor.models import Doctor
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.decorators import user_only
from django.contrib import messages

@login_required(login_url='account:patient_login')
@user_only
#create appointment
def create_appointment(request, pk=None):
  if (request.method == "POST"):
    p = Patient.objects.get(user_id=request.user.id)
    a = Appointment(patient_id_id=p.id)
    d = Doctor.objects.get(pk=pk)
    if (Appointment.objects.filter(doc_id=pk).exists()):
      messages.info(request, f"Doctor with name {d.name} is fully Registered")
      return redirect('doctor:list_doc')      
    a.doc_id_id = pk
    a.save()
    return redirect('patient:list')
  return render(request, "patient/appointment.html")

@login_required(login_url='account:patient_login')
@user_only
# listing all the created appointments
def list_appointment(request):
  p = Patient.objects.get(user_id=request.user.id)
  appointment = Appointment.objects.filter(patient_id_id=p.id)
  return render(request, "patient/list.html", {
    "appointments": appointment
  })

@login_required(login_url='account:patient_login')
@user_only
# Update Appointment
def update_appointment(request, pk=None):
  if (request.method == "POST"):
    a = Appointment.objects.get(pk=pk)
    a.save()
    return redirect('patient:list')
  return render(request, "patient/update_appointment.html")

@login_required(login_url='account:patient_login')
@user_only
# Delete Appointment
def delete_appointment(request, pk=None):
  appointment = Appointment.objects.get(pk=pk)
  appointment.delete()
  return redirect('patient:list')