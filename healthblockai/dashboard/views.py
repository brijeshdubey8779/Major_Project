from django.shortcuts import render

# Create your views here.

def doctordashboard(request):
    return render(request, "dashboard/DoctorDashboard.html")

def patientdashboard(request):
    return render(request, "dashboard/patientdashboard.html")