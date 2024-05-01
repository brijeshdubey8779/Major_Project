from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Patient, Doctor


def patientlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        patient = authenticate(request, email=email, password=password)

        if patient is not None:
            # If the user is authenticated, log them in
            login(request, patient)
            return redirect('patientdashboard')  # Redirect to the patient dashboard
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password.')
            return redirect('patientlogin')  # Redirect back to the dashboard

    # If request method is GET, render the login page
    return render(request, "login/patientlogin.html")


def docterlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        doctor = authenticate(request, username=username, password=password)

        if doctor is not None:
            # If the user is authenticated, log them in
            login(request, doctor)
            return redirect('dashboard:doctordashboard')  # Redirect to the doctor dashboard
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password.')
            return redirect('doctorlogin')  # Redirect back to the login page

    # If the request method is not POST, render the login page
    return render(request, 'login/docterlogin.html')


def adminlogin(request):
    # Add logic for admin login if required
    pass


def patientRegister(request):
    if request.method == 'POST':
        # Extract data from the form
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date_of_birth = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone')
        health_insurance = request.POST.get('insurance')

        # Create and save Patient object
        patient = Patient.objects.create(
            full_name=full_name,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            address=address,
            phone_number=phone_number,
            health_insurance=health_insurance
        )

        return redirect('patientlogin')  # Redirect to the patient login page after registration

    return render(request, "registration/patientRegister.html")


def docterRegister(request):
    if request.method == 'POST':
        # Extract data from the form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        license_number = request.POST.get('license_number')
        specialization = request.POST.get('specialization')
        clinic_hospital = request.POST.get('clinic_hospital')
        phone = request.POST.get('phone')

        # Create and save Doctor object
        doctor = Doctor.objects.create(
            full_name=full_name,
            email=email,
            password=password,
            medical_license_number=license_number,
            specialization=specialization,
            clinic_hospital_name=clinic_hospital,
            phone_number=phone
        )

        return redirect('doctor_login')  # Redirect to the doctor login page after registration

    return render(request, "registration/docterRegister.html")


# @login_required(login_url="patientlogin")
def patientdashboard(request):
    return render(request, "login/patnetdashboard.html")

def logout_user(reqeust):
    pass