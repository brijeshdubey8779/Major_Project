from django.urls import path
from . import views


urlpatterns = [
    path("doctordashboard", views.doctordashboard, name="doctordashboard"),
    path("patientdashboard", views.patientdashboard, name="patientdashboard"),
]