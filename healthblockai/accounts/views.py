from django.shortcuts import render

# Create your views here.

def patientlogin(request):
   # Get the username and password from the user.
#    username = request.form.get('username')
#    password = request.form.get('password')

#     # Check if the user is already logged in.
#    if current_user:
#     return redirect(url_for('home'))

#    # Check if the username and password are valid.
#    user = User.query.filter_by(username=username, password=password).first()
#    if user is None:
#     return redirect(url_for('login'))
    
#     # log the user in.
#     login_user(user)

#     # Redirect the user to the home page.
#     return redirect(url_for('home'))\
    return render(request, "login/patientlogin.html")

def docterlogin(request):
    # Get the username and password from the user.
    # username = request.form.get('username')
    # password = request.form.get('password')
    return render(request, "login/docterlogin.html")

def adminlogin(request):
    return render(request, "login/adminlogin.html")
def logout_user():
    pass
def patientRegister(request):
    return render(request, "registration/patientRegister.html")
def docterRegister(request):
    return render(request, "registration/docterRegister.html")

def dashboard():
    pass