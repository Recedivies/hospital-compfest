from django.urls import path
from account.views import (
  register_user,
  patient_login,
  patient_logout,
  logged_in,
  dashboard,

  addDoc,
  updateDoc,
  deleteDoc
)

app_name = "account"

urlpatterns = [
  path('register/', register_user, name='reg_patient'),
  path('login/', patient_login, name='patient_login'),
  path('logged_in/', logged_in, name='logged_in'),
  path('logout/', patient_logout, name='patient_logout'),
  path('dashboard/', dashboard, name='dashboard'),
  path('dashboard/add_doc', addDoc, name='addDoc'),
  path('dashboard/update/<int:pk>', updateDoc, name='updateDoc'),
  path('dashboard/delete/<int:pk>', deleteDoc, name='deleteDoc')
]