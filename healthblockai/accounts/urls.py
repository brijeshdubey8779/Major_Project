from django.urls import path
from . import views


urlpatterns = [
    path("patientlogin", views.patientlogin, name="patientlogin"),
    path("docterlogin", views.docterlogin, name="docterlogin"),
    path("adminlogin", views.adminlogin, name="adminlogin"),
    path("patientRegister", views.patientRegister, name="patientRegister"),
    path("docterRegister", views.docterRegister, name="docterRegister"),
    path("logout", views.logout_user, name="logout"),
    # path("dashboard", views.dashboard, name="dashboard"),
]