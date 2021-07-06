from django.shortcuts import render, redirect
from account.forms import (
  RegisterForm,
  ProfileForm,
  DashForm,
)
from django.contrib.auth import (
  login,
  authenticate,
  logout,
)
from django.contrib import auth
from django.contrib.auth.models import User
from doctor.models import Doctor
from django.contrib.auth.decorators import login_required
from account.decorators import admin_only

# User Registration
def register_user(request):
  if (request.method == "POST"):
    form = RegisterForm(data=request.POST)
    formProfile = ProfileForm(data=request.POST)
    if (form.is_valid() and formProfile.is_valid()):
      user = form.save()
      user.set_password(user.password)
      user.save()
      profile = formProfile.save(commit=False)
      profile.user = User.objects.get(pk=user.id)
      profile.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      email = form.cleaned_data.get('email')
      user = authenticate(username=username, email=email, password=password)
      login(request, user)
      return redirect('account:logged_in')
    else:
      return render(request, 'account/register.html', {
        'error': "Username/Email already in use. Please try another username/email!"
      })
  else:
    form = RegisterForm()
    formProfile = ProfileForm()
    return render(request, "account/register.html", {"form":form,"formProfile":formProfile})

# User Login
def patient_login(request):
  if (request.method == "POST"):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if (user is not None):
      auth.login(request, user)
      return redirect('account:dashboard')
    return render(request, 'account/login.html', {
      'error': "Invalid Username or Password"
    })
  return render(request, "account/login.html")

# User Logout
def patient_logout(request):
  logout(request)
  return render(request, "doctor/index.html", {
    "patient_logout": patient_logout
  })

# User Login display after logging in
def logged_in(request):
  return render(request, "account/logged_in.html", {
    "logged_in": logged_in
  })

# Admin Dashboard
def dashboard(request):
  return render(request, "account/dashboard.html", {
    "doctor": Doctor.objects.all()
  })

@login_required(login_url='account:patient_login')
@admin_only
# Add Doctor from admin site
def addDoc(request):
  form = DashForm(request.POST, request.FILES)
  if (form.is_valid()):
    doc_id = form.cleaned_data.get('doc_id')
    name = form.cleaned_data.get('name')
    description = form.cleaned_data.get('description')
    form.save()
    return redirect('account:dashboard')
  form = DashForm()
  return render(request, "account/addDoc.html", {
    "form": form
  })

@login_required(login_url='account:patient_login')
@admin_only
# Update Doctor from admin site
def updateDoc(request, pk=None):
  if (request.method == "POST"):
    form = DashForm(request.POST, request.FILES)
    if (form.is_valid()):
      d = Doctor.objects.get(pk=pk)
      d.name = form.cleaned_data['name']
      d.description = form.cleaned_data['description']
      d.save()
      return redirect('account:dashboard')
  form = DashForm()
  return render(request, "account/updateDoc.html", {
    "form": form
  })

@login_required(login_url='account:patient_login')
@admin_only
# Delete Doctor from admin site
def deleteDoc(request, pk=None):
  d = Doctor.objects.get(pk=pk)
  d.delete()
  return redirect('account:dashboard')