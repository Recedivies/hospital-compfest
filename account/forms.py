from django import forms
from django.contrib.auth.models import User
from patient.models import Patient
from doctor.models import Doctor

# creating resgistration form using meta class
class RegisterForm(forms.ModelForm):
  password = forms.CharField(max_length=30, widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password')

# creating profile form for registration
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = ('age',)

# creating form for admin dashboard to add and update doctors  
class DashForm(forms.ModelForm):
  class Meta:
    model = Doctor
    fields = ('name', 'description')

# # creating form for admin dashboard to update doctors         
# class UpdateForm(forms.ModelForm):
#   class Meta:
#     model = Doctor
#     fields = ('name', 'description')
